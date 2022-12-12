from pydantic import BaseModel
from uuid import UUID



class Book(BaseModel):
    id: int | None = None
    title: str
    author: str
