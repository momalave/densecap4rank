# preprocess.py
# Extract frames from video
# author: Mario Malave
# date: 1-27-2020

import cv2
import math
import os


#videoFile = "microsoft.mp4"
videoFile = "vids/samsung2.mp4"
temp_res = 5; # frame extraction rate in seconds

imagesFolder = os.path.dirname(os.path.realpath(__file__)) #current path
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate

while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(temp_res*frameRate) == 0):
        filename = imagesFolder + "/imgs/imageMS_" +  str(int(frameId)) + ".jpg"
        cv2.imwrite(filename, frame)
cap.release()
print("Done!")
