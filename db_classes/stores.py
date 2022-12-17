from typing import Union, Optional
from db_classes.abs_index import IndObject


class Store(IndObject):
    name: str
    description: Optional[str] = None