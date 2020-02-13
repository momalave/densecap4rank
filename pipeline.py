# main.py
# Full pipeline implementation (TODO integrate into streamlit app)
# author: Mario Malave
# date: 2-5-2020


# 1. Add new videos
# give youtube url
# call dlYoutube.py to download videos

# 2. Prepocess videos by extracting the frames
# call prepocess.py

# 3. Run the frames through the model (on AWS)
# call densecap
# vi ~/.bashrc
# s3fs -o allow_other -o use_cache=/tmp/cache3 -o passwd_file=/root/.passwd-s3fs densecap /s3mnt
# th run_model.lua -input_dir /s3mnt/imgs/
# python2.7 -m SimpleHTTPServer 8181


# 4. Process the output json from densecap model
# call postprecessing.py

# 5. Start elasticsearch or make sure the Elasticsearch server is running
# make sure to use: pip install elasticsearch
# run bin/elasticsearch

# 6. Seach a query based on user input
# curl -XGET 'http://localhost:9200/_cat/indices?v' to show current indices
# curl -XDELETE 'http://localhost:9200/INDEX_NAME_HERE' to delete an index
# call python query_es.py "women in dress"

# 7. Process the output results jsons (query_output.json)
# TODO, extract video id and the timepoint to show in streamlit

# 8. Display video in the streamlit app (with timepoint if possible)
