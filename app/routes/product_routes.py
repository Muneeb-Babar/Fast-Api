from fastapi import APIRouter, HTTPException, status, Depends
from ..models.product_model import product_collection
from ..schemas.product_schema import ProductCreate, ProductUpdate, ProductResponse
from bson import ObjectId
from typing import List
from ..utils.dependencies import get_current_user
from fastapi import Depends


router = APIRouter(prefix="/products", tags=["Products"])

# CREATE
# @router.post("/", response_model=ProductResponse)
# async def create_product(product: ProductCreate):
#     new_product = product.dict()
#     result = await product_collection.insert_one(new_product)
#     new_product["id"] = str(result.inserted_id)
    # return new_product

@router.post("/", response_model=ProductResponse)
async def create_product(
    product: ProductCreate,
    user: dict = Depends(get_current_user)
):
    new_product = product.dict()
    new_product["owner_id"] = user["user_id"]
    result = await product_collection.insert_one(new_product)
    new_product["id"] = str(result.inserted_id)
    return new_product

# READ ALL
@router.get("/", response_model=List[ProductResponse])
async def get_all_products():
    products = []
    async for p in product_collection.find():
        p["id"] = str(p["_id"])
        del p["_id"]
        products.append(p)
    return products

# READ ONE
@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str):
    product = await product_collection.find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product["id"] = str(product["_id"])
    del product["_id"]
    return product

# UPDATE
@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(product_id: str, update_data: ProductUpdate):
    updated = await product_collection.find_one_and_update(
        {"_id": ObjectId(product_id)},
        {"$set": {k: v for k, v in update_data.dict().items() if v is not None}},
        return_document=True
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    updated["id"] = str(updated["_id"])
    del updated["_id"]
    return updated


# DELETE
@router.delete("/{product_id}")
async def delete_product(product_id: str):
    deleted = await product_collection.delete_one({"_id": ObjectId(product_id)})
    if deleted.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
