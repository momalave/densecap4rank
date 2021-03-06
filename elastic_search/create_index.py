#!/usr/bin/env python

from argparse import ArgumentParser, FileType
import json
import logging
import os

from elasticsearch import Elasticsearch
from elasticsearch import helpers

logging.basicConfig(level=logging.WARNING)

# Data cleaning: Consolidate rules to blacklist in a single function.
def blacklist_message(msg):
    if msg.get("type", "").lower() != "question":
        return True


def extract_documents(file_path, index, columns):
    with open(file_path) as f:
        for line in f:
            try:
                l_json = json.loads(line)
            except json.JSONDecodeError as e:
                logging.debug(f"Malformed JSON: {line}")
                continue

            if blacklist_message(l_json):
                continue

            doc = {"_index": index, "_id": l_json["id"]}
            doc.update({k: l_json.get(k) for k in columns})
            yield doc

def addIndex(data, index):
    for i, d1 in enumerate(data):
        data[i].update({"_index": index})
    return data

def main():
    parser = ArgumentParser("Bulk insert stack overflow questions into elastic search")
    parser.add_argument("path", help="Path to raw file.", type=FileType("r"))
    parser.add_argument("mapping", help="Path to mapping.json", type=FileType("r"))
    args = parser.parse_args()
    es_url = os.getenv("ES_URL")
    es = Elasticsearch(es_url)

    #index = "so-questions"
    index = "DC-index"
    mappings = json.loads(args.mapping.read())

    #with open("results_new.json", "r") as read_file:
    #    mappings = json.load(read_file)

    #mappings = data['results']

    # Error 400 indicates that index already exists. In this case,
    # just ignore and do not create the index.
    es.indices.create(index, mappings, ignore=400)
    columns = mappings["mappings"]["properties"].keys()

    #docs = extract_documents(args.path, index, columns)
    docs = json.loads(args.path.read())

    #add index as a keys
    docs = addIndex(docs, index)

    helpers.bulk(es, docs)


if __name__ == "__main__":
    main()
