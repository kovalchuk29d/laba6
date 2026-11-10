"""
Головна програма, яка використовує модулі з пакета src.
"""
import math
import requests

# Імпорт з локальних модулів у тій самій папці
from basic_operations import add, divide 
from advanced_operations import root, percentage

if __name__ == "__main__":
    print("--- Використання власного пакета (src) ---")
    print(f"Додавання 15 + 27 = {add(15, 27)}")
    print(f"Ділення 100 / 4 = {divide(100, 4)}")
    print(f"Кубічний корінь з 27 = {root(27, 3)}")
    print(f"20% від 150 = {percentage(150, 20)}")

    print("\n--- Використання стандартного модуля math ---")
    print(f"Число Пі: {math.pi}")
    print(f"Квадратний корінь з 16: {math.sqrt(16)}")

    print("\n--- Використання стороннього пакета requests ---")
    try:
        response = requests.get("https://api.github.com")
        print(f"Статус код запиту до GitHub API: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Помилка при виконанні запиту: {e}")