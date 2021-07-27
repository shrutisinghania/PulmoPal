# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:37:07 2020

@author: SS067504,PD055552
"""

import numpy as np
import cv2
from keras.models import load_model
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import base64
from matplotlib import pyplot as plt
from tensorflow.keras import backend as K
from pymongo import MongoClient
from PIL import Image

import tensorflow as tf

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/uploadImage', methods=['POST'])
@cross_origin()
def predictionOnCXRImage():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    gender = request.form['gender']
    location = request.form['location']
    dictionary = dict([('first_name', first_name), ('last_name', last_name), ('age',age), ('gender',gender), ('location',location)])
    imagefile = request.files.get('imagefile', '')
    imagefile.save('test_image_file.jpg')
    BS = 8
    predictionResult=""
    
    data = []
    model = load_model('model_covid_vs_pneumonia_vs_normal.h5')
   
    ima = cv2.imread('test_image_file.jpg')
    image = cv2.cvtColor(ima, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    
    
    img = np.expand_dims(image,axis=0)
       
    data.append(image)
    
    testX = np.array(data) / 255.0

    lower_black = np.array([0,0,0], dtype = "uint16")
    upper_black = np.array([70,70,70], dtype = "uint16")
    black_mask = cv2.inRange(ima, lower_black, upper_black)
    cv2.imwrite('img.jpg',black_mask)
            
    im1 = Image.open("test_image_file.jpg")
    im2 = Image.open("img.jpg")
    
    newimg = Image.blend(im1, im2, alpha=0.5)
    newimg.save("blended.jpg")
    
    image = cv2.imread('blended.jpg', 0)
    colormap = plt.get_cmap('inferno')
    heatmap = (colormap(image) * 2**16).astype(np.uint16)[:,:,:3]
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_RGB2BGR)
    cv2.imwrite('heatmap.png', heatmap)
    
    predIdxs = model.predict(testX, batch_size=BS)
    predIdxs = np.argmax(predIdxs, axis=1)
    print("The ids are",predIdxs)
    
    if(predIdxs == 1):
        print('Normal')
        predictionResult = "Normal"
    elif(predIdxs == 0):
        print('Covid')
        predictionResult = "Covid"
    elif(predIdxs == 2):
        print('Pneumonia')
        predictionResult = "Pneumonia"
        
    dictionary['predictionResult'] = predictionResult
    print(dictionary)
    client = MongoClient("mongodb+srv://ShipIt:root@cluster0.cey16.mongodb.net/ShipIt?retryWrites=true&w=majority")
    db = client.get_database('ShipIt')
    records = db.Analysis
    records.insert_one(dictionary)
    print('Added to db')
    im = Image.open("heatmap.png")
    rgb_im = im.convert('RGB')
    rgb_im.save('heatmap.jpeg')
    with open("heatmap.jpeg", "rb") as image_file:
        encoded_string_heatmap = base64.b64encode(image_file.read())
        
    with open("test_image_file.jpg", "rb") as image_file_orig:
        encoded_string_original = base64.b64encode(image_file_orig.read())
    return jsonify({'Encoded_Image_Original':str(encoded_string_original),'Encoded_Image_HeatMap':str(encoded_string_heatmap),'Predicted_Result':predictionResult,'Status':'File Uploaded Succesfully and prediction is made...'})

if __name__ == "__main__":
    print("Running...")
    app.run(host = '0.0.0.0',port=5005)
