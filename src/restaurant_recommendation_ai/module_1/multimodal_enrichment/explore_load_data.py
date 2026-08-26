from .load_data import (
    load_recipes,
    load_user_reviews,
    load_recipe_images,
)


recipes = load_recipes()
user_reviews = load_user_reviews()
recipe_images = load_recipe_images()

print(f"Recipes: {len(recipes)}")
print(f"User reviews: {len(user_reviews)}")
print(f"Images: {len(recipe_images)}")