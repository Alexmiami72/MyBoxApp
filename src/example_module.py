# src/example_module.py

def greet(name):
    """A simple function to greet someone."""
    return f"Hello, {name}!"

class SimpleClass:
    """A basic example class."""
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

if __name__ == "__main__":
    print(greet("World"))
    simple_obj = SimpleClass(10)
    print(f"SimpleClass value: {simple_obj.get_value()}")
