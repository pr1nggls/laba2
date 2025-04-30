from math import factorial


def ff(x):
    if x == 0:
        return 1
    return factorial(x)


print(ff(0))