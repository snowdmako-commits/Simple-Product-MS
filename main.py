from functions import *

while True:

    print("""
        ==============================
        MINI PRODUCT MANAGEMENT SYSTEM
        ==============================

         1. Show all products     
         2. Sort by price ascending
         3. Sort by price descending
         4. Search by name
         5. Search by ID
         6. Get cheapest product
         7. Get most expensive product

         0. Exit
    """)

    try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                show_products()

            elif choice == 2:
                sort_by_price_asc()

            elif choice == 3:
                sort_by_price_desc()

            elif choice == 4:
                search_by_name()

            elif choice == 5:
                search_by_id()

            elif choice == 6:
                get_cheapest_product()

            elif choice == 7:
                get_expensive_product()

            elif choice == 0:
                print("program finished")
                break

            else:
                print("invalid choice")

    except ValueError:
            print("please enter a number")

    except Exception as e:
            print("Error:", e)
