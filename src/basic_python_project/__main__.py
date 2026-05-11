"""
Main entry point for the basic python project.
"""

from .greet import greet


def main() -> None:
    """Main function."""
    name = input("Enter your name: ")
    message = greet(name)
    print(message)


if __name__ == "__main__":
    main()
