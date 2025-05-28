# scripts/example_script.py

import argparse
from src.example_module import greet # Example of importing from src

def main():
    parser = argparse.ArgumentParser(description="A simple example script.")
    parser.add_argument("-n", "--name", default="User", help="Name to greet")
    args = parser.parse_args()

    greeting = greet(args.name)
    print(greeting)
    print("This is an example script.")

if __name__ == "__main__":
    main()
