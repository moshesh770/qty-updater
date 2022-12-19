from elasticsearch import Elasticsearch, NotFoundError
import os

DB_HOST = "http://es01.me:9200"
es = Elasticsearch(DB_HOST, verify_certs=False)

