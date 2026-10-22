
from app import greet


def test_greet_returns_name():
    assert greet("Barella") == "Hello, Barella!"


def test_greet_handles_empty_name():
    assert greet("") == "Hello, !"
