from pydantic import BaseModel
class InventoryUpdate(BaseModel):
    product_id: int
    new_stock: int