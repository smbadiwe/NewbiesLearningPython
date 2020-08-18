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
    # Strictly speaking, this 'if' statement should be 'if speed < 60'
    # But that'll mean that if 'speed' is 60, our program will print 'Points: 0'
    # which is still the same thing as 'OK'. That's why I'm using 'if speed <= 60'
    if speed <= 60:
        print("OK")
    else:
        # Remove 60 from the original value so what is left is now the excess speed.
        # For instance, if the original speed is 83, after this, it'll now be 23.
        # NB: I could have also created a new variable for the remainder. 
        # e.g. 'rem = speed - 60' and then 'n_points = rem // 5' in line 31;
        # but I wanted to do this to show that SOMETIMES it's OK to reuse a variable
        # for something else.
        speed -= 60 

        # Get the number of points, which is the number of 5's we can count from the remainder
        # For instance, now that speed is 20 (83 - 60), how many 5's are in 23?
        # Ans: 4! The remainder is not up to 5 so we ignore it.
        # So, how do we achieve this? Integer division! Remember our discussion on it?
        n_points = speed // 5

        # Do we suspend license?
        if n_points > 12:
            print("License suspended")
        else:
            print("Points:", n_points)


def guess_number(answer: int):
    """
    - Ask the user to guess the number on your mind. This number on your mind is the 'answer' parameter.
    - If the number the user guessed is greater than 'answer', it should tell the user "Your guess is greater"
    - If the number the user guessed is less than 'answer', it should tell the user "Your guess is smaller"
    - If the number the user guessed is equal to 'answer', it should tell the user "Your guess is correct!" and end the game.
    """
    guess = int(input("Guess the number I have on my mind:\t"))
    while guess != answer:  # keep asking until the correct guess is made.
        if guess < answer:
            print("Your guess is smaller. ", end="")
        else:
            print("Your guess is greater. ", end="")
        guess = int(input("Guess again:\t"))
        # The line of code below (line 59), which I commented out, is equivalent to the 
        # 5 lines of codes above (i.e. lines 50-54). But it's a bit harder to understand. 
        # Lesson: Choose simplicity (easy to understand) even if it means more lines of code.

        # guess = int(input(f"Your guess is {'smaller' if guess < answer else 'greater'}. Guess again:\t"))
    print("Your guess is correct!")


def guess_number_advanced(answer: int):
    """
    Implement this function to do the same thing that `guess_number` function does; with the following modifications

    - Keep track of the number of guesses the user is making.
    - If the user has guessed 20 times and have not guessed the correct answer, tell the user "Maximum attempts reached", show the user the correct answer and end the game.
    """
    guess = int(input("Guess the number I have on my mind:\t"))
    count = 1  # 1 because the user has just guessed the first time.

    # There are several ways to code this 'while' loop that'll achieve the same thing.
    # As in most things in life, there are many paths to achieving the same results.
    # I wrote this version because it looks mostly like the previous solution. The only 
    # difference is the addition of lines 82-85 and of course, line 71.
    while guess != answer:  # keep asking until the correct guess is made.
        if guess < answer:
            print("Your guess is smaller. ", end="")
        else:
            print("Your guess is greater. ", end="")
        count += 1
        if count > 20:
            print("Maximum attempts reached. The correct answer is", answer)
            return
        guess = int(input("Guess again:\t"))

    # if the execution reaches here, it means that the condition for the while loop
    # in line 77 is false; i.e. 'guess == answer'.
    print("Your guess is correct!")


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
