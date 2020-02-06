import streamlit as st

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

st.title('DenseCap Video Rank')

sentence = st.text_input('Search:')
if sentence:
    st.write(my_model.predict(sentence))

st.subheader('Results')


value = st.selectbox("",["one", "two", "three"])
#value = st.sidebar.selectbox("Hello", ["one", "two", "three"])
#st.write(value)


submit = st.button('Play Video')
#if submit:
    #requests.post('http://127.0.0.1:8000/letters', json=new_candidates)

#if st.checkbox('Test'):
#tt = st.slider('Frames',0,50,0)
