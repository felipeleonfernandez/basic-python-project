"""
Greeting module for the basic python project.
"""


def greet(name: str) -> str:
    """
    Generate a greeting message.

    Args:
        name: The name of the person to greet.

    Returns:
        A greeting message.
    """
    if not name:
        return "Hello!"
    return f"Hello, {name}!"
