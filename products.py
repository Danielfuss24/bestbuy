class Product:
    """Represents a product in the store."""

    def __init__(
        self,
        name: str,
        price: float,
        quantity: int
    ):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name cannot be empty.")

        if price < 0:
            raise ValueError("Product price cannot be negative.")

        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Returns the current product quantity."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Updates the product quantity."""
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns whether the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Prints the product information."""
        print(
            f"{self.name}, "
            f"Price: {self.price}, "
            f"Quantity: {self.quantity}"
        )

    def buy(self, quantity: int) -> float:
        """Buys a certain quantity and returns the total price."""
        if quantity <= 0:
            raise ValueError(
                "Purchase quantity must be greater than zero."
            )

        if quantity > self.quantity:
            raise ValueError("Not enough items in stock.")

        total_price = self.price * quantity
        new_quantity = self.quantity - quantity

        self.set_quantity(new_quantity)

        return total_price