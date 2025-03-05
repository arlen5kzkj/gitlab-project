import random

def get_random_code():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ["A", "B", "C", "D", "E", "F"]
    return f"{random.choice(numbers)}{random.choice(letters)}-{random.choice(numbers)}{random.choice(letters)}-{random.choice(numbers)}{random.choice(letters)}{random.choice(numbers)}{random.choice(letters)}"
