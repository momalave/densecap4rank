import streamlit as st
import os
import json
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.patches as patches
#from PIL import Image
import numpy as np


#my_placeholder = st.empty()

#import time
#import math
#import random
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import tensorflow as tf
#import dataset
#import cv2
#from sklearn.metrics import confusion_matrix
#from datetime import timedelta
#import h5py

def fig2data ( fig ):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw ( )

    # Get the RGBA buffer from the figure
    w,h = fig.canvas.get_width_height()
    buf = numpy.fromstring ( fig.canvas.tostring_argb(), dtype=numpy.uint8 )
    buf.shape = ( w, h,4 )

    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = numpy.roll ( buf, 3, axis = 2 )
    return buf

def fig2img ( fig ):
    """
    @brief Convert a Matplotlib figure to a PIL Image in RGBA format and return it
    @param fig a matplotlib figure
    @return a Python Imaging Library ( PIL ) image
    """
    # put the figure pixmap into a numpy array
    buf = fig2data ( fig )
    w, h, d = buf.shape
    return Image.fromstring( "RGBA", ( w ,h ), buf.tostring( ) )

# extract after specfied delim
def substring_after(s, delim):
    return s.partition(delim)[2]
# extract before specfied delim
def substring_before(s, delim):
    return s.partition(delim)[0]
# extract frame number
def extract_frame_num(s):
    return substring_before(substring_after(s,'tp'),'.')

dir_path = os.path.dirname(os.path.realpath(__file__))
st.title('DenseCap Video Rank')

sentence = st.sidebar.text_input('Search:')
if sentence:
	#vids = set()
	options = list()
	options_conv = dict()
	options_bb = dict()
	st.subheader('Results:')
	st.markdown('You searched: ' + "**_"+ str(sentence) + "_**")

	os.system("python elastic_search/query_es.py " + "\"" + sentence + "\"")

	with open("elastic_search/query_output.json", "r") as read_file:
		data = json.load(read_file)
		#print(len(data["hits"]["hits"]))
		for i,hit in enumerate(data["hits"]["hits"]):
			#print([hit["_source"]["img_name"], hit["_source"]["img_name"].split("_")[0], hit["_source"]["img_name"].split("_")[1]])


			#st.text([hit["_source"]["img_name"].split("_")[0], hit["_source"]["img_name"].split("_")[1], hit["_source"]["captions"]])
			#st.markdown('st is **really_cool**.')
			st.markdown(str(i+1) + ". ID: **" + hit["_source"]["img_name"].split("_")[0] + "**, Time: **" + extract_frame_num(hit["_source"]["img_name"].split("_")[1]) + " seconds**, Caption: **" + hit["_source"]["captions"] + "**")


			temp = hit["_source"]["img_name"].split("_")[0] + ", " + extract_frame_num(hit["_source"]["img_name"].split("_")[1]) + " seconds, " + hit["_source"]["captions"]
			options_conv[temp] = hit["_source"]["img_name"]
			options_bb[temp] = hit["_source"]["boxes"]
			options.append(temp)
			#vids.add(hit["_source"]["img_name"].split("_")[0])
			#print(vids)
			#print(hit["_source"]["captions"])
			#image = Image.open('imgs/' + hit["_source"]["img_name"])
			#st.image(image, caption=hit["_source"]["captions"], use_column_width=True)

	options.insert(0,"")
	value = st.selectbox("",options)
	if value != "":
		#image = Image.open('imgs/' + options_conv[value])
		#st.image(image, caption=substring_after(value,"seconds,"), use_column_width=True)

		if 1:
			im = np.array(Image.open('imgs/' + options_conv[value]), dtype=np.uint8)
			# Create figure and axes
			fig,ax = plt.subplots(1)
			plt.axis('off')
			# Display the image
			#mng = plt.get_current_fig_manager()
			#mng.full_screen_toggle()
			ax.imshow(im)
			# Create a Rectangle patch
			rect = patches.Rectangle((options_bb[value][0],options_bb[value][1]),options_bb[value][2],options_bb[value][3],linewidth=1,edgecolor='r',facecolor='none')

			# Add the patch to the Axes
			ax.add_patch(rect)

			#plt.gca().set_axis_off()
			#plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
			#plt.margins(0,0)
			#plt.gca().xaxis.set_major_locator(plt.NullLocator())
			#plt.gca().yaxis.set_major_locator(plt.NullLocator())

			#plt.savefig ( "./my_img.png" )
			plt.savefig("./my_img.png", bbox_inches = 'tight', pad_inches = 0)

			image = Image.open("./my_img.png")
			st.image(image, caption=substring_after(value,"seconds,"), use_column_width=True)
			#plt.show()

	#value = st.sidebar.selectbox("Hello", ["one", "two", "three"])
	#st.write(value)


	#submit = st.button('Play Video')

	#add_slider = st.sidebar.slider(
    #'Select a range of values',
    #0, 100)



#if submit:
    #requests.post('http://127.0.0.1:8000/letters', json=new_candidates)

#if st.checkbox('Test'):
#tt = st.slider('Frames',0,50,0)
