from pydantic import BaseModel
from datetime import date
from typing import Optional
class SalesQuery(BaseModel):
    start_date: Optional[date]
    end_date: Optional[date]
    product_id: Optional[int]
    category: Optional[str]