from random import randint


class ComputerGuess:
    userGuess = 0
    low = 0
    high = 0
    value = 0

    def __init__(self, low, high, user_input):
        self.userGuess = user_input
        self.low = low
        self.high = high
        self.value = randint(self.low, self.high)

    def generate_number(self):
        if self.value == self.userGuess:
            print("Correct! The number was: " + str(self.value))
        else:
            print("Incorrect.")

            if self.userGuess > self.value:
                print("Your number was too high.")
            else:
                print("Your number was too low.")

            self.userGuess = input("Try a new number. ")
            self.generate_number()





