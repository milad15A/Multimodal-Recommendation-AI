from pathlib import Path

from .llm_client import llm_model
from .load_data import split_restaurant_paragraphs
from .prompts import restaurant_data_structure_prompt_generation
from .validation import validate_restaurant

# Load data
file_path = Path("data/raw/California-Culinary-Map.txt")

with open(file_path, "r", encoding="utf-8") as file:
    data = file.read()

# Split restaurants
restaurant_list = split_restaurant_paragraphs(data)


# Select restaurants
restaurant_paragraph = restaurant_list[0]
example_restaurant_paragraph = restaurant_list[1]


# Generate prompt
base_system_msg, base_user_prompt = restaurant_data_structure_prompt_generation(
    restaurant_paragraph=restaurant_paragraph,
    example_restaurant_paragraph=example_restaurant_paragraph,
)


# Test LLM
test_response = llm_model(system_msg=base_system_msg, prompt_txt=base_user_prompt)

restaurant_data = validate_restaurant(test_response)

print(f"Success! Validated: {restaurant_data.name}")

print(test_response)
