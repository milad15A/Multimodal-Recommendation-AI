EXAMPLE_RESTAURANT_PARAGRAPH = restaurant_list[1]

EXAMPLE_OUTPUT = """
{
    "name": "Mar de Cortez",
    "location": "Santa Monica",
    "type": "casual taqueria",
    "food_style": "Baja-style seafood",
    "rating": 4.2,
    "price_range": 1,
    "signatures": [
        "beer-battered snapper tacos",
        "zesty octopus ceviche"
    ],
    "vibe": "salt-air energy",
    "environment": "a premier sun-drenched spot for open-air dining near the pier.",
    "shortcomings": []
}
"""


def restaurant_data_structure_prompt_generation(restaurant_paragraph):

    base_system_msg = """
    You are an expert restaurant information extraction assistant.
    Your task is to transform unstructured restaurant descriptions
    into structured JSON data.

    Extract only information that is supported by the restaurant
    description. Do not invent or assume information.

    Return valid JSON only.
    """

    base_user_prompt = f"""
    Task:
    Extract the restaurant information from the description and
    convert it into a structured JSON object.

    Restaurant description:
    {restaurant_paragraph}

    Example:
    Input Restaurant Description:
    {EXAMPLE_RESTAURANT_PARAGRAPH}

    Output:
    {EXAMPLE_OUTPUT}

    Return only the JSON object without additional explanation.
    """

    return base_system_msg, base_user_prompt