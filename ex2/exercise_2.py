import random


def check_speed(speed: int):
    """
    This function is for checking how fast a driver is driving.
    It takes one parameter: speed. Units is km/h.

    You are to implement it such that it does the following:
    - If speed is less than 60km, it should print "OK".
    - Otherwise, for every 5km above the speed limit (60), it should give the driver one warning point and print the total number of warning points. For example, if the speed is 80, it should print "Points: 4".
    - If the driver gets more than 12 points, it should print "License suspended".
    """
    pass


def guess_number(answer: int):
    """
    - Ask the user to guess the number on your mind. This number on your mind is the 'answer' parameter.
    - If the number the user guessed is greater than 'answer', it should tell the user "Your guess is greater"
    - If the number the user guessed is less than 'answer', it should tell the user "Your guess is smaller"
    - If the number the user guessed is equal to 'answer', it should tell the user "Your guess is correct!" and end the game.
    """
    pass


def guess_number_advanced(answer: int):
    """
    Implement this function to do the same thing that `guess_number` function does; with the following modifications

    - Keep track of the number of guesses the user is making.
    - If the user has guessed 20 times and have not guessed the correct answer, tell the user "Maximum attempts reached", show the user the correct answer and end the game.
    """
    pass


def ex_2_qn_1():
    speed = input("Enter driver's speed:\t")
    check_speed(int(speed))


def ex_2_qn_2():
    answer = random.randint(0, 1000001)
    print("Guessing Game\nGuess the number on my mind.\nIt's a number between 0 and 1,000,000 (1 million)\nYou'll get multiple attempts and I'll be giving you hints to nidge you towards the correct answer.")
    guess_number(answer)


def ex_2_qn_3():
    answer = random.randint(0, 1000001)
    print("Guessing Game [Advanced]\nGuess the number on my mind.\nIt's a number between 0 and 1,000,000 (1 million)\nYou'll get multiple attempts and I'll be giving you hints to nidge you towards the correct answer.")
    guess_number_advanced(answer)


if __name__ == "__main__":
    while True:
        qn = input("Which question do you want to run? (Type q to exit)\nAns: ")
        if qn == 'q':
            break
        if qn not in ['1', '2', '3']:
            print(f"Invalid: There's no question {qn}")
            continue
        print(f"Running Ex. 2 Qn. {qn}...\n")
        locals()[f"ex_2_qn_{qn}"]()
        print(f"\nDone running Ex. 2 Qn. {qn}\n========================\n")

    print("\nBye!")
