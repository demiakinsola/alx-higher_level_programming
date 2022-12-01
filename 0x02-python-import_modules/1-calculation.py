#!/usr/bin/python3
# this guard prevents the code from executing when imported.
if __name__ == "__main__":

    import calculator_1

    a = 10
    b = 5
    print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))
    print("{0:d} - {1:d} = {2:d}".format(a, b, sub(a, b)))
    print("{0:d} * {1:d} = {2:d}".format(a, b, mul(a, b)))
    print("{0:d} / {1:d} = {2:d}".format(a, b, div(a, b)))
