
from pydantic import BaseModel, Field


class Restaurant(BaseModel):
    name: str
    location: str
    type: str
    food_style: str
    rating: float | None = None
    price_range: int | None = None
    signatures: list[str] = Field(default_factory=list)
    vibe: str | None = None
    shortcomings: list[str] = Field(default_factory=list)


def validate_restaurant(test_response):
    return Restaurant.model_validate_json(test_response)