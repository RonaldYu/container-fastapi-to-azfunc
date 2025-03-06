from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return JSONResponse(content={"item_id": item_id})
