from ComputerGuess import ComputerGuess


class Main:
    low = input("Pick the minimum. ")
    high = input("Pick the maximum. ")
    print("That's the range!")
    userNumber = input("Now guess what number I'm thinking of: ")
    obj = ComputerGuess(low, high, userNumber)
    obj.generate_number()
