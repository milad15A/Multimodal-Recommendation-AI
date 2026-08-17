from pathlib import Path

file_path = Path(
    "data/raw/California-Culinary-Map.txt"
)

with open(file_path, "r", encoding="utf-8") as file:
    data = file.read()

print(data[:100])


def split_restaurant_paragraphs(data):
    restaurant_list = data.split("\n\n")
    restaurant_list = restaurant_list[1:]
    return restaurant_list


restaurant_list = split_restaurant_paragraphs(data)

