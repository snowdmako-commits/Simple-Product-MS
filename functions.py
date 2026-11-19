import json


def load_products():
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            products = json.load(file)
            return products

    except FileNotFoundError:
        print("products file not found")
        return []

    except json.JSONDecodeError:
        print("json file is empty or incorrect")
        return []

    except Exception as e:
        print("Error:", e)
        return []


def show_products():
    try:
        products = load_products()

        for p in products:
            print(f"ID: {p["id"]} | Name: {p["name"]} | Price: {p["price"]} AZN")

    except Exception as e:
        print("Error:", e)

def sort_by_price_asc():
    try:
        products = load_products()
        products.sort(key=lambda p: p["price"])

        for p in products:
            print(f"{p["name"]} - {p["price"]} AZN")

    except Exception as e:
        print("Error:", e)

def sort_by_price_desc():
    try:
        products = load_products()
        products.sort(key=lambda p: p["price"] , reverse= True)

        for p in products:
            print(f"{p["name"]} - {p["price"]} AZN")

    except Exception as e:
        print("Error:", e)


















