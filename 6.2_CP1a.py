# Apply the Explicit Trapezoid method on a grid of step size h = 0.1 in [0,1] to the initial value problem in
# Exercise 1. Print a table of the t values, approximations, and global truncation error at each step.
import numpy as np
from pandas import DataFrame as DF


def trapezoid(y0, f, h, t):
    w = np.zeros(len(t))
    w[0] = y0
    for i in range(0, len(t) - 1):
        w[i + 1] = w[i] + h / 2 * (f(t[i], w[i]) + f(t[i] + h, w[i] + h * f(t[i], w[i])))
    return w


def exact_solution_a(t):
    return (t ** 2) / 2 + 1


def main():
    f = lambda t, y: t
    h = 0.1
    t = np.arange(0, 1 + h, h)
    w = trapezoid(1, f, h, t)
    true_value = exact_solution_a(t)
    error = abs(true_value - w)
    print(DF({"t": t, "w": w, "Error": error, 'True value': true_value}).set_index('t')[['True value', 'w', 'Error']])


if __name__ == '__main__':
    main()
