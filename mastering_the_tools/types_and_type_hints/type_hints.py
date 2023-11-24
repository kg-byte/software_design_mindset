def add_numbers(x: int, y: int) -> int:
    """
    Adds two numbers and returns the result.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.
    """
    return x + y


def greet(name: str) -> str:
    """
    Generates a greeting message.

    Args:
        name (str): The name of the person.

    Returns:
        str: A personalized greeting message.
    """
    return f"Hello, {name}!"


# Example usage
result = add_numbers(5, 7)
print(f"Result of adding numbers: {result}")

message = greet("Alice")
print(message)
