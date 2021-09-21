import numpy as np
import math
import mpmath as mathsec


def setup(n):
    x = np.ones(n)
    for i in range(0, x.size):
        x[i] = 10 ** (i * (-1) - 1)
    return x


def main():
    n = 10
    array = setup(n)
    for i in range(0, array.size):
        potato = (1 - mathsec.sec(array[i])) / (math.tan(array[i]) ** 2)  # This is the original expression.
        potato2 = (-1) / (1 + mathsec.sec(array[i]))  # Revised expression.
        # print(potato2)
        print(potato2)


if __name__ == '__main__':
    main()
