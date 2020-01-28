# read_json.py
# Process the output of the densecap model for elastic search
# author: Mario Malave
# date: 1-28-2020

import json

with open("results_new.json", "r") as read_file:
    data = json.load(read_file)


# extract before specfied delim
def substring_after(s, delim):
    return s.partition(delim)[2]
# extract after specfied delim
def substring_before(s, delim):
    return s.partition(delim)[0]
# extract frame number
def extract_frame_num(s):
    return substring_before(substring_after(s,'_'),'.')

# extract metadata when file name follows id_frFrameRate_fnFrameNumber.jpg
def extract_meta(s):
    id = substring_before(s,'_')
    fr = substring_before(substring_after(s,'fr'),'_')
    fn = substring_before(substring_after(s,'fn'),'.')
    print('ID: ' + id)
    print('Frame rate: ' + fr)
    print('Frame number: ' + fn)
    print('Seconds: ' + str(float(fn)/float(fr)))
    return id,fr,fn

#test1 = 'test_fr50_fn30.jpg'
#id, fr, fn = extract_meta(test1)
#print(test1)

#test1 = data['results']
#tmp1 = test1[0]
#print tmp1.keys()

for frame in data['results']:
    frame_num = extract_frame_num(frame['img_name'])

    # if filename is not in name_frame_num.jpg format
    if (frame_num == ''):
        frame_num = -1

    print(frame['img_name'])
    print(frame_num)
