# read_json.py
# Process the output of the densecap model for elastic search
# author: Mario Malave
# date: 1-28-2020

import json

with open("example_output.json", "r") as read_file:
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
#tmp1 = test1[0]
#print tmp1.keys()

for frame in allResults:
    #frame_num = extract_frame_num(frame['img_name'])

    # if filename is not in name_frame_num.jpg format
    #if (frame_num == ''):
    #    frame_num = -1

    id, tp = extract_frame(frame['img_name'])

    #print(frame['img_name'])
    #print(frame_num)
    with open('data_out.json', 'w') as outfile:
        json.dump(allResults, outfile)
