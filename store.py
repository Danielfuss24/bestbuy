from products import Product


class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = 0

        for product in self.product_list:
            total_quantity += product.get_quantity()

        return total_quantity

    def get_all_products(self) -> list[Product]:
        active_products = []

        for product in self.product_list:
            if product.is_active():
                active_products.append(product)

        return active_products

if __name__ == "__main__":
    bose = Product(
        "Bose QuietComfort Earbuds",
        price=250,
        quantity=500
    )

    mac = Product(
        "MacBook Air M2",
        price=1450,
        quantity=100
    )

    pixel = Product(
        "Google Pixel 7",
        price=500,
        quantity=250
    )

    best_buy = Store([bose, mac])

    print("Vor dem Hinzufügen:")
    for product in best_buy.product_list:
        product.show()

    best_buy.add_product(pixel)

    print("\nNach dem Hinzufügen:")
    for product in best_buy.product_list:
        product.show()

    best_buy.remove_product(mac)

    print("\nNach dem Entfernen:")
    for product in best_buy.product_list:
        product.show()

    print("\nGesamtanzahl im Store:")
    print(best_buy.get_total_quantity())

    print("\nAktive Produkte:")
    for product in best_buy.get_all_products():
        product.show()