from fastapi import APIRouter
from app.services.elastic import search_content

router = APIRouter()

@router.get("/")
async def search(query: str):
    results = await search_content(query)
    return results
