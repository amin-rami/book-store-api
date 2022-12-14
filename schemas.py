from pydantic import BaseModel, Field
from uuid import UUID



class Book(BaseModel):
    id: int
    title: str = Field()
    author: str = Field()
