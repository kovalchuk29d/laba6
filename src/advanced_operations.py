"""
Модуль для розширених математичних операцій.
"""

def power(base, exp):
    """Підносить число до степеня."""
    return base ** exp

def root(number, degree=2):
    """Обчислює корінь заданого степеня з числа."""
    if number < 0 and degree % 2 == 0:
        raise ValueError("Неможливо обчислити парний корінь з від'ємного числа.")
    return number ** (1 / degree)

def percentage(total, percent):
    """Обчислює вказаний відсоток від заданого числа."""
    return (total * percent) / 100