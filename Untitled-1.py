import random

def main():
    number = RandomNumber()
    guess = input("Enter a number")
    CheckUserChoice(number, guess)
    return None

def RandomNumber():
    random_number = random.randint(0, 100)
    return random_number
def CheckUserChoice(number, guess):
    return None

main()
