"""
Модуль для базових математичних операцій.
"""

def add(a, b):
    """Додає два числа."""
    return a + b

def subtract(a, b):
    """Віднімає друге число від першого."""
    return a - b

def multiply(a, b):
    """Множить два числа."""
    return a * b

def divide(a, b):
    """
    Ділить перше число на друге.
    
    Raises:
        ValueError: Якщо b дорівнює 0.
    """
    if b == 0:
        raise ValueError("Ділення на нуль неможливе.")
    return a / b