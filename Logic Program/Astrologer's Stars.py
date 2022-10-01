# Python Program to print Astrologer's Stars

def pattern(num, bol):
    """Function to print pattern according to requirements of question."""

    bob = bool(bol)                     # Converting the integer b to bool.

    v = list(range(1, num + 1))         # Creating a list containing numbers from 1 to n.

    if not bob:                         # If the bool value turns False, the list is reversed.
        v.reverse()

    for i in v:                         # A loop to print the required pattern.
        print("*" * i)


if __name__ == '__main__':
    # Taking the inputs.
    n = int(input("Enter the value of n:"))
    b = int(input("Enter the value of bool(0 or 1):"))

    # Calling the function.
    pattern(n, b)
