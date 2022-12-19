import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from db_classes.products import Product as ProductInd
from db_classes.stores import Store as StoreInd
from typing import Union, Optional

app = FastAPI()


class Product(BaseModel):
    name: str
    sku: str
    description: Optional[str] = None
    category: Optional[str] = None
    inventory: int
    price: float
    tax: Optional[float] = None
    store_id: Optional[str] = None


class Store(BaseModel):
    name: str
    description: Optional[str] = None
    location: Optional[str] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/stores/{store_id}")
def get_store(store_id: str):
    """
    Get store by ES ID
    """
    st, res = StoreInd.load_by_id("stores", store_id)
    if st != 200:
        raise HTTPException(st, res)
    return res


@app.get("/products/{product_id}")
def get_product(product_id: str):
    """
    Get product by ES ID
    """
    st, res = ProductInd.load_by_id("products", product_id)
    if st != 200:
        raise HTTPException(st, res)
    return res


@app.delete("/stores/{store_id}")
def remove_store(product_id: str):
    st, res = StoreInd.remove_by_id("stores", product_id)
    if st != 200:
        raise HTTPException(st, res)
    return res


@app.get("/products/stores/search/{search_term}")
def get_products_store(search_term: str):
    st, res = ProductInd.fetch_store_by_product(search_term=search_term)
    if st != 200:
        raise HTTPException(st, res)
    else:
        return res


@app.delete("/products/{product_id}")
def remove_product(product_id: str):
    st, res = ProductInd.remove_by_id("products", product_id)
    if st != 200:
        raise HTTPException(st, res)
    return res


@app.put("/products/{product_id}/qty")
def update_qty(product_id: str, qty: int):
    if qty < 0:
        raise HTTPException(status_code=400, detail="Qty must be positive")
    st, res = ProductInd.update_inventory(product_id, qty)
    if st != 200:
        raise HTTPException(st, res)
    return res


@app.get("/stores/{store_id}/products/")
def get_store_items(store_id: str):
    st, res = ProductInd.fetch_store_products(store_id=store_id)
    if st != 200:
        raise HTTPException(st, res)
    else:
        return res


@app.post("/products/")
def create_product(product: Product, store_id: str):
    product.store_id = store_id
    status, err = ProductInd.put_single('products', product)
    if status != 200:
        raise HTTPException(status, err)
    return err


@app.post("/stores/")
def create_store(store: Store):
    return StoreInd.put_single('stores', store)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
