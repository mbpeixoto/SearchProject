from fastapi import FastAPI
from app.routes.search import router as search_router
from app.routes.content import router as content_router

app = FastAPI()

app.include_router(search_router, prefix="/search")
app.include_router(content_router, prefix="/content")

@app.get("/")
async def root():
    return {"message": "Content Management API"}
