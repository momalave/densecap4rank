# preprocess.py
# Extract frames from video
# author: Mario Malave
# date: 1-27-2020

import cv2
import math
import os

# extract before specfied delim
def substring_before(s, delim):
    return s.partition(delim)[0]

# return all .mp4 files
arr_mp4 = [x for x in os.listdir("./vids") if x.endswith(".mp4")]
arr_mp4.sort();
print(arr_mp4)
# output: ['work.txt', '3ebooks.txt']


#videoFile = "microsoft.mp4"
#videoFile = "vids/samsung2.mp4"
temp_res = 5; # frame extraction rate in seconds

curFolder = os.path.dirname(os.path.realpath(__file__)) #current path

for ii, vidName in enumerate(arr_mp4):
    print("Processing video " + str(vidName) + "...")
    videoFile = os.path.join(curFolder, "vids/", vidName)
    cap = cv2.VideoCapture(videoFile)
    frameRate = cap.get(5) #frame rate
    while(cap.isOpened()):
        frameId = cap.get(1) #current frame number
        ret, frame = cap.read()
        if (ret != True):
            break
        if (frameId % math.floor(temp_res*frameRate) == 0):
            filename = curFolder + "/imgs/" + substring_before(vidName,'.') + "_tp" + str(round(frameId/frameRate)) + ".jpg"
            cv2.imwrite(filename, frame)
    cap.release()
print("Done!")
