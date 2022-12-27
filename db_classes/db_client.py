from elasticsearch import Elasticsearch, NotFoundError
import os

DEBUG = os.environ.get('local_debug', None)
if DEBUG is not None:
    DB_HOST = "http://localhost:9200"
else:
    DB_HOST = "http://es01.me:9200"
es = Elasticsearch(DB_HOST, verify_certs=False)

