import numpy as np


def poly_horner(poly, n, x):
    result = poly[0]
    for i in range(0, n):
        result = result * x + poly[i]
    return result


def main():
    poly = np.ones(50)
    x = 1.00001
    n = len(poly)
    q = (1.00001 ** 51 - 1) / (1.00001 - 1)
    poly = poly_horner(poly, n, x)
    print(poly-q)


if __name__ == '__main__':
    main()
