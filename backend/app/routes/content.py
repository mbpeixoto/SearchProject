from fastapi import APIRouter
from app.services.mongo import get_content_details
from app.services.minio import get_media_url

router = APIRouter()

@router.get("/{content_id}")
async def get_content(content_id: str):
    details =  get_content_details(content_id)
    media_url =  get_media_url(content_id)
    print(f"Media URL: {media_url}")
    return {**details, "media_url": media_url}
