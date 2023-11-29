def main():
    number = RandomNumber()
    guess = input("Enter a number")
    CheckUserChoice(number, guess)
    return None

def RandomNumber():
    return None

#check
def CheckUserChoice(number, guess):
    if number == guess:
        return 'good guess!'
    else:
        return 'try again'

main()
