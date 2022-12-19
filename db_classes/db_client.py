from elasticsearch import Elasticsearch, NotFoundError
import os

if os.name == 'nt':
    DB_HOST = "http://localhost:9200"
else:
    DB_HOST = "http://es01.me:9200"
es = Elasticsearch(DB_HOST, verify_certs=False)

