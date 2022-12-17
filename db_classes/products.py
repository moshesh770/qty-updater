from db_classes.abs_index import IndObject, NotFoundError
from db_classes.stores import Store
from db_classes.db_client import es


class Product(IndObject):

    @classmethod
    def fetch_store_products(cls, store_id: str):
        query_body = {
            "query": {
                "match": {
                    "store_id": store_id
                }
            }
        }
        try:
            res = es.search(index="products", body=query_body, size=100)
            return 200, res
        except NotFoundError:
            return 404, f"No products for store {store_id} were found"

    @classmethod
    def update_inventory(cls, prod_id: str, new_qty: int):
        if not cls.is_object_exists("products", prod_id):
            return 404, f"No product with {prod_id} was found"
        try:
            res = cls.update_obj("products", obj_id=prod_id, query={"inventory": new_qty})
            return 200, res
        except Exception as e:
            return 500, str(e)

    @classmethod
    def put_single(cls, index: str, obj):
        store_id = obj.store_id
        if store_id is None:
            return 400, "Store ID was not provided"
        if not Store.is_object_exists('stores', obj_id=store_id):
            return 404, f"Store with ID: {store_id} does not exist"
        try:
            res = super().put_single(index=index, obj=obj)
            return 200, res
        except Exception as e:
            return 500, str(e)

