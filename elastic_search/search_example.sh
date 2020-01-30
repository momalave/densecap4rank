curl -XGET 'localhost:9200/so-questions/_search?pretty' \
-H 'Content-Type: application/json' -d '{
  "query": {
    "match": {
      "captions": "man in a suit"
    }
  }
}'
