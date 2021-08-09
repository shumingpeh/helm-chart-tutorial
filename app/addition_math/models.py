from typing import Optional

from pydantic import BaseModel


# base model
class Endpoint(BaseModel):
    curation_name: str
    route_param: str
    params: Optional[dict] = {}


# params for model addition
class AdditionModelParam(BaseModel):
    number_1: int
    number_2: int
    number_3: int
    flooring: Optional[int] = 0


# model for addition
class AdditionModelOutput(BaseModel):
    output_sum: int
    curation_name: str = "addition"


# logging
class AdditionEndpointLog(BaseModel):
    param: AdditionModelParam
    response: AdditionModelOutput
