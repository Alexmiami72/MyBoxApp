# tests/test_example_module.py

import unittest
from src.example_module import greet, SimpleClass

class TestExampleModule(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Test"), "Hello, Test!")
        self.assertEqual(greet(""), "Hello, !")

    def test_simple_class(self):
        obj = SimpleClass(42)
        self.assertEqual(obj.get_value(), 42)
        obj.value = 100
        self.assertEqual(obj.get_value(), 100)

if __name__ == "__main__":
    unittest.main()
