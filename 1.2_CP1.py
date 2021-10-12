# Apply Fixed-Point Iteration to find the solution of each equation to eight correct decimal places.
import numpy as np


def fixedpointiteration(f, x0, steps):
    x = np.ones(steps)
    x[1] = x0
    for i in range(0, steps - 1):
        x[i + 1] = f(x[i])
    return x[-1]


def func(x): return (2 * x + 2) ** (1 / 3)


def main():
    print(fixedpointiteration(func, 1, 3))


if __name__ == "__main__":
    main()
