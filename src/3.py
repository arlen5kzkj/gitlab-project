import random
def generate_random_python_code():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)
    # Generate a list of words
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grapefruit", "honeydew", "jackfruit", "kiwi"]
    # Generate a random word from the list
    word = random.choice(words)
    # Print the result
    print(num, word)
