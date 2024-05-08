# script.py

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    message = greet(name)
    print(message)
