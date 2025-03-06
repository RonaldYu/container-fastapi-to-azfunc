from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .routes.hello import router as hello_router
from .routes.items import router as items_router

app = FastAPI(root_path='/task1')
app.include_router(hello_router)
app.include_router(items_router)