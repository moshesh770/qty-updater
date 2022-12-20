import logging
from typing import Union, Optional
from db_classes.abs_index import IndObject
from models.cache_util import stores_cache


class Store(IndObject):
    name: str
    description: Optional[str] = None

    @classmethod
    def load_by_id(cls, index: str, obj_id: str):
        if stores_cache.get(obj_id):
            return stores_cache.get(obj_id)
        store = super().load_by_id(index, obj_id)
        stores_cache[obj_id] = store
        return store

    @classmethod
    def put_single(cls, index: str, obj):
        store = super().put_single(index, obj)
        logging.warning(store)
        stores_cache[store['_id']] = store
        return store

    @classmethod
    def remove_by_id(cls, index: str, obj_id: str):
        stores_cache.pop(obj_id)
        return super().remove_by_id(index, obj_id)
