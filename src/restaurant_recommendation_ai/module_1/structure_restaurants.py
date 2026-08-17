from pydantic import ValidationError

from .llm_client import safe_llm_call
from .load_data import get_restaurant_list
from .prompts import (
    JSON_auto_repair_prompts,
    restaurant_data_structure_prompt_generation,
)
from .validation import Restaurant

restaurant_list = get_restaurant_list()
structured_restaurant_lists = []

for i, restaurant_paragraph in enumerate(restaurant_list):

    # 2.1: Produce initial output
    base_system_msg, base_user_prompt = (
        restaurant_data_structure_prompt_generation(
            restaurant_paragraph=restaurant_paragraph,
            example_restaurant_paragraph=restaurant_list[1]
        )
    )

    candidate_json_output = safe_llm_call(
        system_msg=base_system_msg,
        prompt_txt=base_user_prompt
    )

    # 2.2: Validation and Auto Correction loop
    while True:

        try:
            restaurant_data = Restaurant.model_validate_json(
                candidate_json_output
            )

            # Validation successful
            break

        except ValidationError as e:

            error_message = e.json()

            repair_system_msg, repair_prompt = JSON_auto_repair_prompts(
                candidate_json_output=candidate_json_output,
                error_message=error_message
            )

            candidate_json_output = safe_llm_call(
                system_msg=repair_system_msg,
                prompt_txt=repair_prompt
            )

    # 2.3: Append finalized response
    structured_restaurant_lists.append(restaurant_data.model_dump())

    # Progress
    if (i + 1) % 20 == 0:
        print(f"{i + 1} out of {len(restaurant_list)} is done")


print("ALL DONE!!")