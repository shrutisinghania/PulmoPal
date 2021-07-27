# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:15:09 2020

@author: SS067504
"""

#import pika, os, json
from matplotlib import pyplot as plt
from pymongo import MongoClient
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import base64
import requests
import matplotlib.pyplot as plt


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

client = MongoClient("mongodb+srv://ShipIt:root@cluster0.cey16.mongodb.net/ShipIt?retryWrites=true&w=majority")
db = client.get_database('ShipIt')
mycol = db["Analysis"]


font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
font1 = {'family': 'serif',
        'weight': 'normal',
        'size': 14,
        }
@app.route('/maleDist', methods=['GET'])
@cross_origin()
def distOfMale():
    mp = 0
    mn = 0
    mc = 0
    for x in mycol.find():
        if(x['gender'] == 'Male'):
            if(x['predictionResult'] == 'Covid'):
                mc = mc + 1
            if(x['predictionResult'] == 'Pneumonia'):
                mp = mp + 1   
            if(x['predictionResult'] == 'Normal'):
                mn = mn + 1             
    disease = ['Covid','Pneumonia','Normal']
    male_distribution = [mc,mp,mn]
    plt.title('Detection of Pneumonia and Covid amongst Male',fontdict=font)
    a = [0 , 0 , 0.1]
    plt.pie(male_distribution,explode = a,labels = disease,textprops={'fontsize': 14},autopct='%1.1f%%', shadow=True, startangle=140)
    plt.savefig('Male.png')
    plt.close()
    with open("Male.png", "rb") as image_file:
        encoded_string_graph = base64.b64encode(image_file.read())
    return jsonify({'Encoded_Image_Graph':str(encoded_string_graph)})


@app.route('/femaleDist', methods=['GET'])
@cross_origin()
def distOfFemale():
    fp = 0
    fn = 0
    fc = 0
    for x in mycol.find(): 
        if(x['gender'] == 'Female'):
            if(x['predictionResult'] == 'Covid'):
                fc = fc + 1
            if(x['predictionResult'] == 'Pneumonia'):
                fp = fp + 1   
            if(x['predictionResult'] == 'Normal'):
                fn = fn + 1  
    disease = ['Covid','Pneumonia','Normal']
    female_distribution = [fc,fp,fn]
    plt.title('Detection of Pneumonia and Covid amongst Female',fontdict=font)
    a = [0 , 0 , 0.1]
    plt.pie(female_distribution,explode = a, labels = disease,textprops={'fontsize': 14},autopct='%1.1f%%', shadow=True, startangle=140)
    plt.savefig('Female.png')
    plt.close()
    with open("Female.png", "rb") as image_file:
        encoded_string_graph = base64.b64encode(image_file.read())
    return jsonify({'Encoded_Image_Graph':str(encoded_string_graph)})

@app.route('/ageDist', methods=['GET'])
@cross_origin()
def distAge():
    disease = request.args.get('disease')
    listOfAge=[]
    for x in mycol.find(): 
        if(x['predictionResult'] == disease):
            listOfAge.append(x['age'])

    listOfAge = list(filter(lambda x: x != 'NODATA', listOfAge)) 
    listOfAge= [int(i)for i in listOfAge]



    print(listOfAge)
    dict_Of_age = {i:listOfAge.count(i) for i in listOfAge}
    
    
    plt.xlabel("Age in years")
    plt.ylabel("No of cases")
    plt.bar(range(len(dict_Of_age)), list(dict_Of_age.values()), color = (0.5,0.1,0.5,0.6))

    
    plt.savefig('AgeDist_'+disease+'.png')
    plt.show()
    with open("AgeDist_"+disease+".png", "rb") as image_file:
        encoded_string_graph = base64.b64encode(image_file.read())
    return jsonify({'Encoded_Image_Graph':str(encoded_string_graph)})

if __name__ == "__main__":
    print("Running...")
    app.run(host = '0.0.0.0',port=5007)


