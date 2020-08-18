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
    speed = int(input("Enter driver's speed: "))
    if speed <= 60:
        print("OK")
    if speed > 120:
        print("license suspended")
        d = 0
    while speed % 5 == 0:
        d = d + 1
        print("point" %d)


def guess_number(answer: int):
    """
    - Ask the user to guess the number on your mind. This number on your mind is the 'answer' parameter.
    - If the number the user guessed is greater than 'answer', it should tell the user "Your guess is greater"
    - If the number the user guessed is less than 'answer', it should tell the user "Your guess is smaller"
    - If the number the user guessed is equal to 'answer', it should tell the user "Your guess is correct!" and end the game.
    """
    import random
    answer = random.randint(0, 1000001)
    num = int(input("guess:"))
    if num > answer:
        print("your guess is greater") 
    elif num < answer:    
        print("your guess is smaller") 
    else:
        print("your guess is correct!")


def guess_number_advanced(answer: int):
    """
    Implement this function to do the same thing that `guess_number` function does; with the following modifications

    - Keep track of the number of guesses the user is making.
    - If the user has guessed 20 times and have not guessed the correct answer, tell the user "Maximum attempts reached", show the user the correct answer and end the game.
    """
    import random
    answer = random.randint(0, 1000001)
    guesses = 0
    while guesses < 20:
        num = int(input("guess:"))
        guesses = guesses + 1
        print("this is your %d num" %guesses)
        if num > answer:
            print("your guess is greater") 
        elif num < answer:
            print("your guess is smaller") 
        elif num == answer:
            print("your guess is correct!")
    else:
        if guesses == 20:
            print("maximum attempts reached")


def ex_2_qn_1():
    speed = input("Enter driver's speed:\t")
    check_speed(speed)


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
