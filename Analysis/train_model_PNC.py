#!/usr/bin/env python
# coding: utf-8

# In[1]:
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
import numpy as np
from tqdm import tqdm
import math

from tensorflow.keras import backend as K

covid_path = 'dataset/COVID-19/'
covid_files = os.listdir(covid_path)

labels_covid = []
data_covid = []

for file in tqdm(covid_files):
    imagePath = covid_path + file
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    data_covid.append(image)
    labels_covid.append('covid')


pne_path = 'dataset/Pneumonia/'
pne_files = os.listdir(pne_path)

labels_pne = []

data_pne = []

for file in tqdm(pne_files):
    imagePath = pne_path + file
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    data_pne.append(image)
    labels_pne.append('pneum')


norm_path = 'dataset/Normal/'
norm_files = os.listdir(norm_path)


labels_norm = []

data_norm = []

for file in tqdm(norm_files):
    imagePath = norm_path + file
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    data_norm.append(image)
    labels_norm.append('normal')
    
data = data_covid + data_pne + data_norm

labels = labels_covid + labels_pne + labels_norm  
  

data = np.array(data) / 255.0
labels = np.array(labels)
# perform one-hot encoding on the labels

lb = LabelEncoder()
labels = lb.fit_transform(labels)
labels = to_categorical(labels); print(labels)    
print(lb.classes_)
print(lb.inverse_transform([0,1,2]))
    
   
# partition the data into training and testing splits using 80% of
# the data for training and the remaining 20% for testing
(trainX, testX, trainY, testY) = train_test_split(data, labels,
	test_size=0.20, stratify=labels, random_state=42)

# initialize the training data augmentation object
trainAug = ImageDataGenerator(
	rotation_range=15,
	fill_mode="nearest")

# load the VGG16 network, ensuring the head FC layer sets are left
# off
baseModel = VGG16(weights="imagenet", include_top=False,
	input_tensor=Input(shape=(224, 224, 3)))
baseModel.summary()
# construct the head of the model that will be placed on top of the
# the base model
headModel = baseModel.output
headModel = AveragePooling2D(pool_size=(4, 4))(headModel)
headModel = Flatten(name="flatten")(headModel)
headModel = Dense(64, activation="relu")(headModel)
headModel = Dropout(0.5)(headModel)
headModel = Dense(3, activation="softmax")(headModel)

# place the head FC model on top of the base model (this will become
# the actual model we will train)
model = Model(inputs=baseModel.input, outputs=headModel)

# loop over all layers in the base model and freeze them so they will
# *not* be updated during the first training process
for layer in baseModel.layers:
	layer.trainable = False

# #### Transfer Learning

#### Downloading the Pre-trained Model
#mobnet_model = keras.applications.mobilenet.MobileNet()



lr_opt =1e-3

epochs = 46
batch_size = 8
 

# compile our model
print("[INFO] compiling model...")
opt = Adam(lr=lr_opt, decay= lr_opt/epochs)


model.compile(loss="categorical_crossentropy",optimizer=opt,metrics=["accuracy"])

model.summary()

# train the head of the network
# import keras
#lr=keras.callbacks.LearningRateScheduler(step_decay,verbose=1)
#checkpoint= keras.callbacks.ModelCheckpoint('./Checkpoint_normal', monitor='val_acc', 
#                                               verbose=0, save_best_only=True, 
#                                               save_weights_only=False, 
#                                               mode='auto',
#                                               period=1)

print("[INFO] training head...")

H = model.fit_generator(
                trainAug.flow(np.array(trainX), np.array(trainY), batch_size=batch_size),
                steps_per_epoch=len(trainX) // batch_size,
                validation_data=(np.array(testX), np.array(testY),),
                validation_steps=len(testX) // batch_size,
                epochs=epochs)


# serialize the model to disk
print("[INFO] saving COVID-19 detector model...")
model.save("model_covid_vs_pneumonia_vs_normal.h5")

print("[INFO] evaluating network...")
predIdxs = model.predict(testX, batch_size=batch_size)

# for each image in the testing set we need to find the index of the
# label with corresponding largest predicted probability
predIdxs = np.argmax(predIdxs, axis=1)

# show a nicely formatted classification report

print(classification_report(testY.argmax(axis=1), predIdxs,target_names=['covid', 'normal', 'pneum']))

# compute the confusion matrix and and use it to derive the raw
# accuracy, sensitivity, and specificity
cm = confusion_matrix(testY.argmax(axis=1), predIdxs)

# show the confusion matrix, accuracy, sensitivity, and specificity
print(cm)          
predIdxs = model.predict(np.array(testX), batch_size=8)
predIdxs = np.argmax(predIdxs, axis=1)
print(predIdxs)




