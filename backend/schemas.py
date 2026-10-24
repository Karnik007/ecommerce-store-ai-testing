"""
ShopWave — Pydantic Request & Response Data Schemas
Intentional Compile-Time Syntax Error:
  - Bug #1: Missing colon ':' at the end of class ProductBase(BaseModel) header
"""

try:
    from pydantic import BaseModel, Field
except ImportError:
    class BaseModel:
        pass
    def Field(*args, **kwargs):
        return None

from typing import Optional, List

# BUG #1 (Intentional Compile-Time SyntaxError):
# Missing colon ':' at the end of the class definition line!
# Python parser raises: SyntaxError: expected ':'
class ProductBase(BaseModel)
    title: str
    price: float
    category: str
    in_stock: bool = True
    discount: Optional[dict] = None

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: str

class CartItem(BaseModel):
    product_id: str
    quantity: int = 1

class OrderRequest(BaseModel):
    items: List[CartItem]
    coupon_code: Optional[str] = None