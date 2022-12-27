import json
from retry import retry
from db_classes.db_client import es, NotFoundError


class IndObject:
    @classmethod
    @retry(tries=3)
    def load_by_id(cls, index: str, obj_id: str):
        try:
            res = es.get(index=index, id=obj_id)
            return 200, res
        except NotFoundError:
            return 404, f"The item with ID:{obj_id} does not exist"

    @classmethod
    @retry(tries=3)
    def remove_by_id(cls, index: str, obj_id: str):
        try:
            res = es.delete(index=index, id=obj_id)
            return 200, res
        except NotFoundError:
            return 404, f"The item with ID:{obj_id} does not exist"

    @classmethod
    @retry(tries=3)
    def find_by_name(cls, index: str, name: str):
        query_body = {
            "query": {
                "match": {
                    "name": name
                }
            }
        }
        return es.search(index=index, body=query_body)

    @classmethod
    @retry(tries=3)
    def put_single(cls, index: str, obj):
        jobj = json.dumps(obj.__dict__)
        return es.index(index=index, body=jobj)

    @classmethod
    @retry(tries=3)
    def is_object_exists(cls, index: str, obj_id: str):
        return es.exists(index=index, id=obj_id)

    @classmethod
    @retry(tries=3)
    def update_obj(cls, index: str, obj_id: str, query: dict):
        return es.update(index=index, id=obj_id, body={"doc": query})

    @classmethod
    @retry(tries=3)
    def get_all(cls, index, size=100):
        try:
            results = es.search(index=index, body={'size': size, 'query': {'match_all': {}}})
            return 200, results['hits']['hits']
        except NotFoundError as e:
            return 404, str(e)
