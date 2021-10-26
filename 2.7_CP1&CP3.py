# Implement Newton's Method with appropriate starting points to find all solutions. Check with Exercise 3 to make
# sure your answers are correct.
import numpy as np


def F1(x):
    return np.array([x[0] ** 2 - 4.0 * x[1] ** 2 - 4.0, (x[0] - 1.0) ** 2 + x[1] ** 2 - 4.0]).reshape((2, 1))


def DF1(x):
    return np.array([2.0 * x[0], -8.0 * x[1], 2.0 * x[0] - 2.0, 2.0 * x[1]]).reshape((2, 2))


def F2(x):
    return np.array([x[0] ** 3 - x[1] ** 3 + x[0], x[0]**2 + x[1]**2 - 1]).reshape((2, 1))


def DF2(x):
    return np.array([3*x[0]**2 + 1, - 3*x[1]**2, 2*x[0], 2*x[1]]).reshape((2, 2))


def multivariate_newton(x, tol, F, DF):
    while np.abs(np.linalg.norm(F(x))) > tol:
        s = np.linalg.solve(DF(x), -F(x))
        x = x + s
    return x


def main():
    #CP1
    x0 = np.array([1, 1]).reshape((2, 1))
    x = multivariate_newton(x0, 0.001, F1, DF1)
    print(f"CP1:\n {x}")
    print(f"feil:\n {np.abs(np.linalg.norm(F1(x)))}")
    print(" ")
    #CP3
    x0 = np.array([1, 1]).reshape((2, 1))
    x = multivariate_newton(x0, 0.001, F2, DF2)
    print(f"CP3:\n {x}")
    print(f"feil:\n {np.abs(np.linalg.norm(F2(x)))}")


if __name__ == "__main__":
    main()
