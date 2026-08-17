from pathlib import Path


def load_restaurant_data():

    file_path = Path(
        "data/raw/California-Culinary-Map.txt"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    return data


def split_restaurant_paragraphs(data):

    restaurant_list = data.split("\n\n")
    restaurant_list = restaurant_list[1:]

    return restaurant_list


def get_restaurant_list():

    data = load_restaurant_data()

    restaurant_list = split_restaurant_paragraphs(data)

    return restaurant_list