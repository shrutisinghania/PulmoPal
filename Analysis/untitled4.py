# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 04:13:27 2020

@author: SS067504
"""


from bokeh.models import GeoJSONDataSource
from urllib.request import urlopen
import json

from bokeh.models import GeoJSONDataSource, HoverTool, LinearColorMapper
from bokeh.palettes import Viridis256
from bokeh.plotting import figure
from bokeh.io import output_file, show
import matplotlib.pyplot as plt
from bokeh.io import show, output_notebook

#output_notebook()

# Geojson of India
with urlopen("https://raw.githubusercontent.com/geohacker/india/master/state/india_state.geojson") as response:
    geojson = json.load(response)

# Round robin over over 3 colors
# You can set the colors here based on the case count you have per state
for i in range(len(geojson['features'])):
  geojson['features'][i]['properties']['Color'] = ['blue', 'red', 'green'][i%3]


# Set the hover to state information and finally plot it
cmap = LinearColorMapper(palette=Viridis256)

TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"

geo_source = GeoJSONDataSource(geojson=json.dumps(geojson))
#print(geo_source)

p = figure(title='India', tools=TOOLS, x_axis_location=None, y_axis_location=None, width=800, height=800)
p.grid.grid_line_color = None

p.patches('xs', 'ys', fill_alpha=0.7, line_color='black', fill_color='Color', line_width=0.1, source=geo_source)

hover = p.select_one(HoverTool)
hover.point_policy = 'follow_mouse'
hover.tooltips = [('State:', '@NAME_1')]

show(p)