import json


def load_products():
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            products = json.load(file)
            return products

    except FileNotFoundError:
        print("Products file not found!")
        return []

    except json.JSONDecodeError:
        print("JSON file is empty or incorrect!")
        return []

    except Exception as e:
        print("Error:", e)
        return []





















