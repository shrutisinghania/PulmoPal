#Importing libraries
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

import requests
import base64

from bs4 import BeautifulSoup

import geopandas as gpd

from pymongo import MongoClient
   
from PIL import Image, ImageDraw, ImageFont

import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/getIndiaGraph', methods=['GET'])
@cross_origin()
def predictionOnCXRImage():
    
    #disease = request.form['disease']
    disease = request.args.get('disease')
    
    data_map = gpd.read_file('Indian_States.shp')
        
    data_map['st_nm'].iloc[25] 
        
    data_map.rename(columns = {'st_nm':'States'}, inplace = True)
        
    data_map['States'] =data_map['States'].str.replace('&','and')
        
    data_map['States'].iloc[0]  = 'Andaman and Nicobar Islands'
    
    data_map['States'].iloc[1] = 'Arunachal Pradesh'
        
    data_map['States'].iloc[6] = 'Dadar Nagar Haveli'
        
    data_map['States'].iloc[23] = 'Delhi'
        
    data_map['States'].iloc[29]='Telangana'
    
    client = MongoClient("mongodb+srv://ShipIt:root@cluster0.cey16.mongodb.net/ShipIt?retryWrites=true&w=majority")
    db = client.get_database('ShipIt')
    mycol = db["Analysis"]
    if (disease == 'Covid'):
        agg_result= mycol.aggregate([ {"$match":{"predictionResult": "Covid" }}, {"$group":{"_id":"$location", "Number":{"$sum":1}}} ,{ "$sort" : {"_id" : 1  }}] ) 
        imagetype = gragh(data_map, agg_result,1)
    elif (disease == 'Pneumonia'):
        agg_result= mycol.aggregate([ {"$match":{"predictionResult": "Pneumonia" }}, {"$group":{"_id":"$location", "Number":{"$sum":1}}} ,{ "$sort" : {"_id" : 1  }}] ) 
        imagetype = gragh(data_map, agg_result,2)
    with open(imagetype, "rb") as image_file_orig:
        encoded_string_original = base64.b64encode(image_file_orig.read())
    return jsonify({'Encoded_Graph':str(encoded_string_original),'Status':'File sent Succesfully...'})

def gragh(data_map, agg_result,indicator):
    covid_img_name = 'India_Covid_Graph.jpeg'
    pneum_img_name = 'India_Pneum_Graph.jpeg'
    stats = [] 
    for i in agg_result: 
        l = []
        l = list(i.values())
        stats.append(l)

    new_cols = ["States","Number"]
    state_data = pd.DataFrame(data = stats, columns = new_cols)
    state_data.head()

    merged = pd.merge(data_map, state_data, on = 'States')
    
    merged.head()
    
    #plotting coronavirus cases on map 
    
    fig, ax = plt.subplots(1, figsize=(20, 12))
    
    ax.axis('off')
    
    #Set the title of the map
    #ax.set_title('Coronavirus Cases In India', fontsize=40 )
    p = merged.plot(column = 'Number', linewidth=0.8, ax=ax, edgecolor='0.8', legend = True)
    
    if(indicator == 1):
        plt.savefig(covid_img_name)
        im = Image.open(covid_img_name)
    else:
        plt.savefig(pneum_img_name)
        im = Image.open(pneum_img_name)
    
    draw = ImageDraw.Draw(im)
    i =0
    h = []
    for item in stats:
        strConcat=""
        if('NODATA' in item):
            continue
        for i in item:
            strConcat = str(strConcat) + str(i) + '-'
        strConcat=strConcat[:-1]
        h.append(strConcat)
        
    font = ImageFont.truetype('arialbd.ttf', 26)
    # calculate the x,y coordinates of the text
    margin = 10
    x = margin + 350
    y =  margin + 130
    
    # draw watermark in the bottom right corner
    draw.text((x, y), ('\n'.join([str(elem) for elem in h])), font=font, fill=(73,186,0))
    
    #Save watermarked image
    if(indicator == 1):
        im.save('India_Covid_Graph.jpeg')
        return 'India_Covid_Graph.jpeg'
    else:
        im.save('India_Pneum_Graph.jpeg')
        return 'India_Pneum_Graph.jpeg'
    

if __name__ == "__main__":
    print("Running...")
    app.run(host = '0.0.0.0',port=5006)
