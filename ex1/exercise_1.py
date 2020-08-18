def ex_1_qn_0():
    """Write a program that prints ‘Hello World’ to the screen."""
    print("Hello World")


def ex_1_qn_1():
    """Write a program that asks the user for their name and greets them with their name."""
    pass


def ex_1_qn_2():
    """Modify the previous program (ex_1_qn_1) such that only the users Alice and Bob are greeted with their names."""
    pass


def ex_1_qn_3():
    """Write a program that asks the user for a number n and prints the sum of the numbers 1 to n"""
    pass


def ex_1_qn_4():
    """Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17"""
    pass


def ex_1_qn_5():
    """Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n."""
    pass


if __name__ == "__main__":
    while True:
        qn = input("Which question do you want to run? (Type q to exit)\nAns: ")
        if qn == 'q':
            break
        for i in range(6):
            if qn == str(i):
                print(f"Running Ex. 1 Qn. {qn}...\n")
                locals()[f"ex_1_qn_{qn}"]()
                print(f"\nDone running Ex. 1 Qn. {qn}...\n")
                break
    print("\nBye!")
