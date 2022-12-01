#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    index = 1
    total_args = len(sys.argv) - 1
# we are not printing the first argument - module name.

    if len(sys.argv) == 1:
        print(f"{0:d} arguments.")

    elif len(sys.argv) == 2:
        print(f"{total_args:d} argument:")
        print(f"{index:d}: {sys.argv[index]}")

    else:
        print(f"{total_args:d} arguments:")
        while index <= total_args:
            print(f"{index:d}: {sys.argv[index]}")
            index += 1
