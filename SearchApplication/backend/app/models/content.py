from pydantic import BaseModel
from typing import List

class Content(BaseModel):
    id: str
    title: str
    summary: str
    tags: List[str]
    author: str
    details: str
