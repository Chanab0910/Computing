from Fahrenheit_to_celsius_converter import fahrenheit_to_celsius
from Fahrenheit_to_celsius_converter import celsius_to_fahrenheit


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(50) == 10
    assert fahrenheit_to_celsius(59) == 15

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(10) == 50
    assert celsius_to_fahrenheit(15) == 59
    