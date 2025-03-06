from fastapi import APIRouter
from fastapi.responses import JSONResponse
router = APIRouter()

@router.get("/")
async def read_root():
    return JSONResponse(content={"message": "Welcome to the Microservice Task 2"})
    
