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

def search_by_name():
    try:
        products = load_products()
        name = input("Enter product name: ").strip().lower()

        found = False

        for p in products:
            if name in p["name"].lower():
                print(f"ID: {p["id"]} | Name: {p["name"]} | Price: {p["price"]} AZN")

                found = True

        if not found:
            print("product not found")

    except Exception as e:
        print("Error:", e)

def search_by_id():
    try :
        products = load_products()
        id = int(input("Enter product ID:" ))

        found = False

        for p in products:
            if p["id"] == id:
                print(f"ID: {p["id"]} | Name: {p["name"]}, | Price: {p["price"]} AZN")

                found = True

        if not found:
            print("product not found")

    except ValueError:
        print("ID must be a number")

    except Exception as e:
        print("Error:", e)

def get_cheapest_product():
    try:
        products = load_products()

        if not products:
            print("no products founded")
            return

        cheapest = min(products, key=lambda p: p["price"])

        print(f"Cheapest: {cheapest["name"]} - {cheapest["price"]} AZN")

    except Exception as e:
        print("Error:", e)

def get_expensive_product():
    try:
        products = load_products()

        if not products:
            print("no products available")
            return

        expensive = max(products, key=lambda p: p["price"])

        print(f"Most Expensive: {expensive["name"]} - {expensive["price"]} AZN")

    except Exception as e:
        print("Error:", e)









