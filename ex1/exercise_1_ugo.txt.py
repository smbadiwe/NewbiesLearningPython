def ex_1_qn_0():
    """Write a program that prints ‘Hello World’ to the screen."""
    print("Hello World")

def ex_1_qn_1():
    """Write a program that asks the user for their name and greets them with their name."""
    form = input("Enter Your Name: ")

def ex_1_qn_2():
    """Modify the pre\vious program (ex_1_qn_1) such that only the users Alice and Bob are greeted with their names."""
    f = input("Enter Your Name:")
    a = ("Alice")
    b = ("Bob")
    if a == f:
        print("Welcome", a)
    if b == f:
        print("Welcome", b)
    else:
        print("Welcome")

def ex_1_qn_3():
    """Write a program that asks the user for a number n and prints the sum of the numbers 1 to n"""
    n = int(input("Enter a Number:"))
    sum = (n * (n + 1)) / 2
    print(sum)

def ex_1_qn_4():
    """Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17"""
    n = int(input("Enter a number:"))
    m = 0
    for i in range(n):
        if (i % 3 == 0 or i % 5 == 0):
            m  = m + i
    print(m)

def ex_1_qn_5():
    """Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n."""
    n = input("Please Enter sum or product:")
    p = ("product")
    s = ("sum")
    if n == p:
       n = int(input("Enter a Number:"))
       factorial = 1
       for i in range(1, n+1):
           factorial = factorial*i
           print(factorial)
    if n == s:
       n = int(input("Enter a Number:"))
       sum = (n * (n + 1)) / 2
       print(sum)

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
