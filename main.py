import products
import store


def display_menu():
    """Displays the main menu."""
    print("\nStore Menu")
    print("----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def display_products(best_buy: store.Store):
    """Displays all active products with a number."""
    product_list = best_buy.get_all_products()

    print("\nProducts")
    print("--------")

    for index, product in enumerate(product_list, start=1):
        print(f"{index}. ", end="")
        product.show()


def create_order(best_buy: store.Store):
    """Collects products from the user and processes an order."""
    shopping_list = []

    while True:
        product_list = best_buy.get_all_products()

        if not product_list:
            print("There are no active products available.")
            return

        display_products(best_buy)

        print(
            "\nEnter the product number and quantity."
        )
        print(
            "Press Enter without entering a product number "
            "to finish the order."
        )

        product_number_input = input(
            "Which product do you want? "
        ).strip()

        if product_number_input == "":
            break

        try:
            product_number = int(product_number_input)

            if (
                product_number < 1
                or product_number > len(product_list)
            ):
                print("Invalid product number.")
                continue

            selected_product = product_list[
                product_number - 1
            ]

            quantity = int(
                input("What amount do you want? ")
            )

            if quantity <= 0:
                print(
                    "The quantity must be greater than zero."
                )
                continue

            if quantity > selected_product.get_quantity():
                print(
                    "The requested quantity is not available."
                )
                continue

            shopping_list.append(
                (selected_product, quantity)
            )

            print("Product added to the order.")

        except ValueError:
            print("Please enter valid whole numbers.")

    if not shopping_list:
        print("No products were selected.")
        return

    try:
        total_price = best_buy.order(shopping_list)

        print("\nOrder made!")
        print(f"Total payment: ${total_price:.2f}")

    except ValueError as error:
        print(f"Order could not be completed: {error}")


def start(best_buy: store.Store):
    """Starts the store user interface."""
    while True:
        display_menu()

        choice = input(
            "\nPlease choose a number: "
        ).strip()

        if choice == "1":
            display_products(best_buy)

        elif choice == "2":
            total_quantity = best_buy.get_total_quantity()

            print(
                "\nTotal of "
                f"{total_quantity} items in store"
            )

        elif choice == "3":
            create_order(best_buy)

        elif choice == "4":
            print("Thank you for visiting Best Buy!")
            break

        else:
            print(
                "Invalid selection. "
                "Please choose a number from 1 to 4."
            )


def main():
    """Creates the inventory and starts the application."""
    product_list = [
        products.Product(
            "MacBook Air M2",
            price=1450,
            quantity=100
        ),
        products.Product(
            "Bose QuietComfort Earbuds",
            price=250,
            quantity=500
        ),
        products.Product(
            "Google Pixel 7",
            price=500,
            quantity=250
        )
    ]

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()