from fastapi import FastAPI
from controller.item_controller import ItemController as item_controller

app = FastAPI()

app.include_router(item_controller.router)
