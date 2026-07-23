from products import Product


class Store:
    """Represents a store containing multiple products."""

    def __init__(self, product_list: list[Product]):
        self.product_list = product_list

    def add_product(self, product: Product):
        """Adds a product to the store."""
        self.product_list.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the store."""
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products."""
        total_quantity = 0

        for product in self.product_list:
            total_quantity += product.get_quantity()

        return total_quantity

    def get_all_products(self) -> list[Product]:
        """Returns all active products."""
        active_products = []

        for product in self.product_list:
            if product.is_active():
                active_products.append(product)

        return active_products

    def order(
        self,
        shopping_list: list[tuple[Product, int]]
    ) -> float:
        """Processes an order and returns its total price."""
        total_price = 0.0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price