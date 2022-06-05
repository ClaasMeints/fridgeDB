from itertools import product
from psycopg2 import Timestamp
from typing import Optional
from pydantic import BaseModel


class user_account(BaseModel):
    account_id: int
    login: str
    passwd: str
    sir_name: Optional[str] = None
    last_name: Optional[str] = None


class account_device_relation(BaseModel):
    account_id: int
    device_id: int


class device(BaseModel):
    device_id: int
    device_name: str


class device_content(BaseModel):
    device_id: int
    product_id: int
    filled_in: Optional[Timestamp] = None
    dropped_out: Optional[Timestamp] = None
    precentage_left: Optional[int] = None


class product(BaseModel):
    product_id: int
    product_name: str
    barcode_id: Optional[int] = None


class product_category_relation(BaseModel):
    product_id: int
    category_id: int


class product_category(BaseModel):
    category_id: int
    category_name: str
    category_image: Optional[str] = None
    unit_id: int


class unit(BaseModel):
    unit_id: int
    unit_symbol: str


class unit_conversion(BaseModel):
    unit_result: int
    unit_factor: int
    conversion_factor: float
