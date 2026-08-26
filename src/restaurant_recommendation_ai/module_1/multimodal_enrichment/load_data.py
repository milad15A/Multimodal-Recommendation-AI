from pathlib import Path
import json

DATA_DIR = Path("data/raw")

Recipe_JSON_PATH = DATA_DIR / "recipes.json"
User_Reviews_JSON_PATH = DATA_DIR / "Synthetic-User-Reviews.json"
Recipe_Images_DIR = DATA_DIR / "synthetic-recipe-images"

def load_recipes():
    with open(Recipe_JSON_PATH, "r", encoding="utf-8") as file:
        recipes = json.load(file)
    return recipes

def load_user_reviews():
    with open(User_Reviews_JSON_PATH, "r", encoding="utf-8") as file:
        user_reviews = json.load(file)
    return user_reviews

def load_recipe_images():
    image_paths = list(Recipe_Images_DIR.glob("*.jpg"))
    return image_paths