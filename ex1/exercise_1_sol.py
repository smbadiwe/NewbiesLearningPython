def ex_1_qn_0():
    """Write a program that prints ‘Hello World’ to the screen."""
    print("Hello World")


def ex_1_qn_1():
    """Write a program that asks the user for their name and greets them with their name."""
    name = input("What's your name?\n> ")
    print("Good day, " + name)


def ex_1_qn_2():
    """Modify the previous program (ex_1_qn_1) such that only the users Alice and Bob are greeted with their names."""
    name = input("What's your name?\n> ")
    if name == "Alice" or name == "Bob":
        print("Good day, " + name)
    else:
        print("Good day!")


def sum_to_n(n):
    # short form:
    return n * (n+1) // 2

    # # long form:
    # total, i = 0, 1
    # while i <= n:
    #     total += i
    #     i += 1
    # return total


def ex_1_qn_3():
    """Write a program that asks the user for a number n and prints the sum of the numbers 1 to n"""
    n = input("Enter a number: ")
    return sum_to_n(int(n))


def ex_1_qn_4():
    """Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17"""
    n = input("Enter a number: ")
    n = int(n)
    if n != 17:
        return sum_to_n(n)

    total, i = 0, 3
    while i <= n:
        if i % 3 == 0 or i % 5 == 0:
            total += i
        i += 1
    return total


def ex_1_qn_5():
    """Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n."""
    n = int(input("Enter a number: "))
    do_sum = input(f"Type 0 to compute sum of 1 to {n}; or 1 to compute product of 1 to {n}\n>>> ")
    if do_sum == '0':
        return sum_to_n(n)
    
    total, i = 1, 1
    while i <= n:
        total *= i
        i += 1
    return total


if __name__ == "__main__":
    while True:
        qn = input("Which question do you want to run? (Type q to exit)\nAns: ")
        if qn == 'q':
            break
        for i in range(6):
            if qn == str(i):
                print(f"Running Ex. 1 Qn. {qn}...\n")
                ans = locals()[f"ex_1_qn_{qn}"]()
                result = f"\nDone running Ex. 1 Qn. {qn}..."
                if ans:
                    result += f"\tAns: {ans}\n"
                print(result)
                break
    print("\nBye!")
