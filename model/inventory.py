from pydantic import BaseModel
class Inventory(BaseModel):
    product_id: int
    new_stock: int