from pydantic import BaseModel
from uuid import UUID
from typing import List

class ReceiptItem(BaseModel):
    name:str
    amount:float


class GeneratedReceipt(BaseModel):
    total_amount:float
    itmes:List[ReceiptItem]
    