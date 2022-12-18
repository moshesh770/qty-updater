from elasticsearch import Elasticsearch, NotFoundError
import os

DB_HOST = "http://localhost:9200"
DB_USER = "elastic"
DB_PASS = os.environ.get('ELASTIC_PASS')
print(f'DB_PASS: {DB_PASS}')
es = Elasticsearch(DB_HOST, verify_certs=False)

