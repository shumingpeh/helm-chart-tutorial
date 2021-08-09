# from memoization import cached
from math import floor

from app.addition_math.models import AdditionModelOutput

# @cached(ttl=180)
def _get_addition_output(
    number_1: int, number_2: int, number_3: int, flooring: int
):
    number_1_computation = number_1 - 10
    number_2_computation = number_2 - 5
    number_3_computation = number_3 - 1
    total_sum = number_1_computation + number_2_computation + number_3_computation

    if flooring == 1:
        total_sum = floor(total_sum)

    response_model = AdditionModelOutput(
        output_sum=total_sum,
        curation_name="addition",
    )

    response = response_model.dict()

    return response