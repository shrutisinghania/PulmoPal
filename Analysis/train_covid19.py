# import the necessary packages
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import AveragePooling2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelBinarizer, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2
import os
from flask import Flask, request
import os


app = Flask(__name__)

@app.route('/trainModel', methods=['GET'])
def analyze():
    ap = argparse.ArgumentParser()
    #dir = os.path.dirname(__file__)
    ap.add_argument("-p", "--plot", type=str, default="plot.png",
    	help="path to output loss/accuracy plot")
    ap.add_argument("-m", "--model", type=str, default="covid19.model",
    	help="path to output loss/accuracy plot")
    args = vars(ap.parse_args())
    INIT_LR = 1e-3
    EPOCHS = 1
    BS = 8
    print("[INFO] loading images...")
    bp_path = 'C:/Users/ss067504/OneDrive - Cerner Corporation/Desktop/work/ship_it/2020/github_repo/ShipItVII/Analysis/dataset/BacterialPneumonia'
    normal_path = 'C:/Users/ss067504/OneDrive - Cerner Corporation/Desktop/work/ship_it/2020/github_repo/ShipItVII/Analysis/dataset/Normal'
    covid_path = 'C:/Users/ss067504/OneDrive - Cerner Corporation/Desktop/work/ship_it/2020/github_repo/ShipItVII/Analysis/dataset/COVID-19'
    vp_path = 'C:/Users/ss067504/OneDrive - Cerner Corporation/Desktop/work/ship_it/2020/github_repo/ShipItVII/Analysis/dataset/ViralPneumonia'
    labels_covid = []
    data_covid = []
    
    imagePaths = list(paths.list_images(covid_path))
    
    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (224, 224))
        data_covid.append(image)
        labels_covid.append('covid')
    
    labels_norm = []
    
    data_norm = []
    
    imagePaths = list(paths.list_images(normal_path))
    
    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (224, 224))
        data_norm.append(image)
        labels_norm.append('normal')
    
    labels_vp = []
    
    data_vp = []
    
    imagePaths = list(paths.list_images(vp_path))
    
    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (224, 224))
        data_vp.append(image)
        labels_vp.append('ViralPneumonia')
    
    labels_bp = []
    
    data_bp = []
    
    imagePaths = list(paths.list_images(bp_path))
    
    
    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (224, 224))
        data_bp.append(image)
        labels_bp.append('BacterialPneumonia')
    
    data = data_covid + data_bp + data_vp + data_norm
    
    labels = labels_covid + labels_bp + labels_vp + labels_norm 
    
    print(labels)
    '''filename = os.path.join(dir, 'dataset')
    imagePaths = list(paths.list_images(filename))
    data = []
    labels = []
    for imagePath in imagePaths:
    label = imagePath.split(os.path.sep)[-2]
    	# load the image, swap color channels, and resize it to be a fixed 224x224 pixels while ignoring aspect ratio
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    data.append(image)
    labels.append(label)'''
    
    # convert the data and labels to NumPy arrays while scaling the pixel intensities to the range [0, 1]
    data = np.array(data) / 255.0
    labels = np.array(labels)
    # perform one-hot encoding on the labels
    lb = LabelEncoder()
    labels = lb.fit_transform(labels)
    labels = to_categorical(labels)
    (trainX, testX, trainY, testY) = train_test_split(data, labels,
    	test_size=0.20, stratify=labels, random_state=42)
    # initialize the training data augmentation object
    trainAug = ImageDataGenerator(
    	rotation_range=15,
    	fill_mode="nearest")
    
    # load the VGG16 network, ensuring the head FC layer sets are left off
    baseModel = VGG16(weights="imagenet", include_top=False,
    	input_tensor=Input(shape=(224, 224, 3)))
    baseModel.summary()
    # construct the head of the model that will be placed on top of the base model
    headModel = baseModel.output
    headModel = AveragePooling2D(pool_size=(4, 4))(headModel)
    headModel = Flatten(name="flatten")(headModel)
    headModel = Dense(64, activation="relu")(headModel)
    headModel = Dropout(0.5)(headModel)
    headModel = Dense(4, activation="softmax")(headModel)
    # place the head FC model on top of the base model (this will become the actual model we will train)
    model = Model(inputs=baseModel.input, outputs=headModel)
    # loop over all layers in the base model and freeze them so they will *not* be updated during the first training process
    for layer in baseModel.layers:
    	layer.trainable = False
    
    # compile our model
    print("[INFO] compiling model...")
    opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
    model.compile(loss="categorical_crossentropy", optimizer=opt,
    	metrics=["accuracy"])
    model.summary()
    # train the head of the network
    print("[INFO] training head...")
    H = model.fit_generator(
    	trainAug.flow(np.array(trainX), np.array(trainY), batch_size=BS),
    	steps_per_epoch=len(trainX) // BS,
    	validation_data=(np.array(testX), np.array(testY)),
    	validation_steps=len(testX) // BS,
    	epochs=EPOCHS)
    
    # make predictions on the testing set
    print("[INFO] evaluating network...")
    predIdxs = model.predict(testX, batch_size=BS)
    print(type(testX))
    print(testX)
    # for each image in the testing set we need to find the index of the label with corresponding largest predicted probability
    predIdxs = np.argmax(predIdxs, axis=1)
    # show a nicely formatted classification report
    print(classification_report(testY.argmax(axis=1), predIdxs,
    	target_names=lb.classes_))
    
    # compute the confusion matrix and and use it to derive the raw accuracy, sensitivity, and specificity
    cm = confusion_matrix(testY.argmax(axis=1), predIdxs)
    total = sum(sum(cm))
    acc = (cm[0, 0] + cm[1, 1]) / total
    sensitivity = cm[0, 0] / (cm[0, 0] + cm[0, 1])
    specificity = cm[1, 1] / (cm[1, 0] + cm[1, 1])
    # show the confusion matrix, accuracy, sensitivity, and specificity
    print(cm)
    print("acc: {:.4f}".format(acc))
    print("sensitivity: {:.4f}".format(sensitivity))
    print("specificity: {:.4f}".format(specificity))
    
    '''N = EPOCHS
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
    plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, N), H.history["accuracy"], label="train_acc")
    plt.plot(np.arange(0, N), H.history["val_accuracy"], label="val_acc")
    plt.title("Training Loss and Accuracy on COVID-19 Dataset")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend(loc="lower left")
    plt.savefig(args["plot"])'''
    
    # serialize the model to disk
    print("[INFO] saving COVID-19 detector model...")
    model.save(args["model"], save_format="h5")
    return "Model training complted...", 200

@app.route("/ping")
def hello():
    return "Ping succesful!"

@app.route('/uploadImage', methods=['POST'])
def test():
   imagefile = request.files.get('imagefile', '')
   imagefile.save('test_image.jpg')
   return "File Uploaded Succesfully...", 200




if __name__ == "__main__":
    print("Running...")
    app.run(host = '0.0.0.0',port=5000)
    #analyze()