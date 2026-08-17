

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


def restaurant_data_structure_prompt_generation(restaurant_paragraph , example_restaurant_paragraph):

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
    {example_restaurant_paragraph}

    Output:
    {EXAMPLE_OUTPUT}

    Return only the JSON object without additional explanation.
    """

    return base_system_msg, base_user_prompt


def JSON_auto_repair_prompts(candidate_json_output, error_message):

    auto_repair_system_msg = """
    You are an expert JSON repair assistant.
    Your task is to correct invalid JSON output based on
    the validation error provided.
    Return only valid JSON.
    Do not add explanations or additional text.
    """

    auto_repair_prompt = f"""
    The following JSON output is invalid:

    {candidate_json_output}

    The validation error is:

    {error_message}

    Correct the JSON output according to the validation error.
    Preserve the original information whenever possible.
    Return only the corrected JSON object.
    """

    return auto_repair_system_msg, auto_repair_prompt