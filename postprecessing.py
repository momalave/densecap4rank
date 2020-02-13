# postprocessing.py
# Process the output of the densecap model for elastic search
# author: Mario Malave
# date: 1-28-2020

import json
import sys

with open("model/results_VIDS.json", "r") as read_file:
    data = json.load(read_file)


# extract after specfied delim
def substring_after(s, delim):
    return s.partition(delim)[2]
# extract before specfied delim
def substring_before(s, delim):
    return s.partition(delim)[0]
# extract frame number
def extract_frame_num(s):
    return substring_before(substring_after(s,'_'),'.')

# extract metadata when file name follows id_frFrameRate_fnFrameNumber.jpg
#test1 = 'test_fr50_fn30.jpg'
#id, fr, fn = extract_meta(test1)
#print(test1)
def extract_meta_full(s):
    id = substring_before(s,'_')
    fr = substring_before(substring_after(s,'fr'),'_')
    fn = substring_before(substring_after(s,'fn'),'.')
    print('ID: ' + id)
    print('Frame rate: ' + fr)
    print('Frame number: ' + fn)
    print('Seconds: ' + str(float(fn)/float(fr)))
    return id,fr,fn

def extract_meta(s):
    id = substring_before(s,'_')
    tp = substring_before(substring_after(s,'tp'),'.')
    print('ID: ' + id)
    print('Seconds: ' + tp)
    return id,tp


allResults = data['results']
allResults_caps = []
#tmp1 = test1[0]
#print tmp1.keys()

#number of captions to use per frame
capNum = 10
print ("Using " + str(capNum) + " captions per frame...")

# Create individual (capNum) occurance for each captions
for ii,frame in enumerate(allResults):
    d, tp = extract_meta(frame['img_name'])
    frame["timepoint"] = tp;
    for xx, caption in enumerate(frame['captions']):
        temp = dict(frame)
        temp['boxes'] = temp['boxes'][:][xx]
        temp['scores'] = temp['scores'][xx]
        temp['captions'] = temp['captions'][xx]
        allResults_caps.append(temp)

        if xx==capNum:
            #print(allResults_caps)
            #sys.exit(0)
            print(str(capNum) + " captions used for " + frame['img_name'] + "...")
            break




    #print(frame['img_name'])
    #print(frame_num)
    with open('data_out2.json', 'w') as outfile:
        json.dump(allResults_caps, outfile)
