from fastapi import APIRouter, HTTPException, Depends
from typing import List
from model.item import Item
from service.item_service import ItemService as item_service

class ItemController:

    router = APIRouter()

    @router.post("/items/", response_model=Item)
    def create_item(item: Item):
        return item_service.create_item(item)

    @router.get("/items/", response_model=List[Item])
    def read_items():
        return item_service.get_items()

    @router.get("/items/{item_id}", response_model=Item)
    def read_item(item_id: int):
        item = item_service.get_item(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @router.put("/items/{item_id}", response_model=Item)
    def update_item(item_id: int, item: Item):
        updated_item = item_service.update_item(item_id, item)
        if updated_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return updated_item

    @router.delete("/items/{item_id}")
    def delete_item(item_id: int):
        result = item_service.delete_item(item_id)
        if not result:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"message": "Item deleted"}