from typing import Any


class ShoppingCart:
    def __init__(self, owner: str) -> None:
        """
        Initializes a shopping cart.

        Args:
            owner (str): The owner of the shopping cart.
        """
        self.owner = owner
        self.items: list[dict[str, Any]] = []

    def add_item(self, item_name: str, quantity: int, price: float) -> None:
        """
        Adds an item to the shopping cart.

        Args:
            item_name (str): The name of the item.
            quantity (int): The quantity of the item.
            price (float): The price per unit of the item.
        """
        item = {
            'name': item_name,
            'quantity': quantity,
            'price': price
        }
        self.items.append(item)

    def calculate_total(self) -> float:
        """
        Calculates the total cost of items in the shopping cart.

        Returns:
            float: The total cost.
        """
        total_cost = sum(item['quantity'] * item['price'] for item in self.items)
        return total_cost

# Exercise usage
# Creating an instance of ShoppingCart, adding items, and calculating the total cost

# Create a shopping cart for "Alice"
alice_cart = ShoppingCart("Alice")

# Add items to the shopping cart
alice_cart.add_item("Apple", 3, 1.50)
alice_cart.add_item("Banana", 2, 0.75)
alice_cart.add_item("Book", 1, 15.99)

# Calculate the total cost
total_cost_alice = alice_cart.calculate_total()
print(total_cost_alice)