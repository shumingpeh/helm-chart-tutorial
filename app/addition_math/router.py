from fastapi import APIRouter

from app.addition_math.models import AdditionModelOutput
from app.addition_math.models import AdditionModelParam
from app.addition_math.utils import _get_addition_output

router = APIRouter()


@router.post("/addition_model", response_model=AdditionModelOutput)
def addition_model(param: AdditionModelParam):

    response = _get_addition_output(
        number_1=param.number_1,
        number_2=param.number_1,
        number_3=param.number_1,
        flooring=param.flooring,
    )

    return response
