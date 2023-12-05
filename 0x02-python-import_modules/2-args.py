#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    a = (len(argv) - 1)
    b = a - 1
    c = a - b
    # Conditions for printing the number of arguments
    if a == 0:
        print(a, "arguments.")
    elif a == 1:
        print(a, "argument:")
    elif a > 1:
        print(a, "arguments:")

    # Printing out the arguments with its index
    if a > 0:
        for i in argv[1:]:
            print(c, ':', argv[c])
            c = a - (b - 1)
