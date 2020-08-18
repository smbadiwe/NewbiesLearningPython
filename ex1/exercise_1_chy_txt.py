def ex_1_qn_0():
    """Write a program that prints ‘Hello World’ to the screen."""
    print("Hello World")


def ex_1_qn_1():
    """Write a program that asks the user for their name and greets them with their name."""
    x = input("what is your name?")
    print("hi " + x)   


def ex_1_qn_2():
    """Modify the previous program (ex_1_qn_1) such that only the users Alice and Bob are greeted with their names."""
    x = input("what is your name?")
    y = ("Bob")
    z = ("Alice")
    if x == y:
        print("hi", y)
    if x == z:
        print("hi", z)
    else:
        print("hi")


def ex_1_qn_3():
    """Write a program that asks the user for a number n and prints the sum of the numbers 1 to n"""
    num = int(input("enter any number: "))
    n = num
    sum = n * (n+1) / 2
    print("sum of the first ", n ,"natural numbers using the formula is: ", sum )   


def ex_1_qn_4():
    """Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17"""
    n = int(input("enter any number: "))
    m = 0
    for i in range(n):
        if  (i % 5 == 0 or  i % 3 == 0):
            m = m + i
    print(n)


def ex_1_qn_5():
    """Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n."""
    x = input("enter sum or product:")
    y = ("sum")
    z = ("product")
    if x == y:
        num = int(input("enter any number: "))
        n = num
        sum = n * (n+1) / 2
        print("sum of the first ", n ,"natural numbers using the formula is: ", sum )
    if x == z:
        num = int(input("enter any number: "))
        n = num
        product = 1
        if n < 0:
            print("enter a positive number")
        else:
            for i in range(1,n + 1):
                product = product*i
                print("product of",n,"is", product)


if __name__ == "__main__":
    while True:
        qn = input("Which question do you want to run? (Type q to exit)\nAns: ")
        if qn == 'q':
            break
        for i in range(6):
            if qn == str(i):
                print("Running Ex. 1 Qn. {qn}...\n")
                locals()[f"ex_1_qn_{qn}"]()
                print("\nDone running Ex. 1 Qn. {qn}...\n")
                break
    print("\nBye!")
