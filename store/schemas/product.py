from decimal import Decimal
from typing import Annotated, Optional

from bson import Decimal128

from store.schemas.base import BaseSchemaMixin, OutSchema
from pydantic import Field, AfterValidator, BaseModel


class ProductBase(BaseModel):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: Decimal = Field(..., description="Price product")
    status: bool = Field(..., description="Status product")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn, OutSchema):
    ...


def convert_decimal_128(v):
    return Decimal128(str(v))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(ProductBase):
    quantity: Optional[int] = Field(None, description="Product quantity")
    price: Optional[Decimal_] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")


class ProductUpdateOut(ProductUpdate, OutSchema):
    ...
