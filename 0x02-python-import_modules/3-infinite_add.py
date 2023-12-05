#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    if (len(argv) - 1) == 0:
        print(0)
    elif (len(argv) - 1) == 1:
        print(int(argv[1]))
    elif (len(argv) - 1) == 2:
        print(int(argv[1]) + int(argv[2]))
    elif (len(argv) - 1) > 2:
        a = 1
        b = a + 1
        while b < (len(argv) - 1):
            result = int(argv[a]) + int(argv[b])
            b = b + 1
            result = result + int(argv[b])

        print(result)
