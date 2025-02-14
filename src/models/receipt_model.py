from pydantic import BaseModel, Field
from typing import List

class ItemDTO(BaseModel):
    shortDescription: str = Field()
    price: str = Field()

class ReceiptDTO(BaseModel):
    retailer: str = Field()
    purchaseDate: str = Field()
    purchaseTime: str = Field()
    items: List[ItemDTO]

    total: str  = Field()
