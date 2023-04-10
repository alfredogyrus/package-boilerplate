import os


def module2_function():
    print(f"La password es {os.environ.get('PASSWORD')}")