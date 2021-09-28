# Apply the Midpoint Method on a grid of step size h = 0.1 in [0,1] for the initial value problems in Exercise 1.
# Print a table of the t values, approximations, and global truncation error at each step.
import numpy as np
from pandas import DataFrame as DF


def midPointMethod(y0, h, f, t):
    w = np.zeros(len(t))
    w[0] = y0
    for i in range(len(t) - 1):
        w[i + 1] = w[i] + h * f(t[i] + (h / 2), w[i] + (h / 2) * f(t[i], w[i]))
    return w


# Task A
def mainA():
    f = lambda t, y: t  # From exercise 6.4.1
    exact = lambda t: (t ** 2) / 2 + 1  # From exercise 6.1.3
    h = 0.1
    t = np.arange(0, 1 + h, h)
    w = midPointMethod(1, h, f, t)
    exact_value = exact(t)
    error = abs(exact_value - w)
    print(
        DF({"t": t, "w": w, "Error": error, 'Exact value': exact_value}).set_index('t')[['Exact value', 'w', 'Error']])

# Task B
def mainB():
    f = lambda t, y: (t ** 2) * y  # From exercise 6.4.1
    exact = lambda t: np.exp((t ** 3) / 3)  # From exercise 6.1.3
    h = 0.1
    t = np.arange(0, 1 + h, h)
    w = midPointMethod(1, h, f, t)
    exact_value = exact(t)
    error = abs(exact_value - w)
    print(
        DF({"t": t, "w": w, "Error": error, 'Exact value': exact_value}).set_index('t')[['Exact value', 'w', 'Error']])


if __name__ == '__main__':
    mainA()
    mainB()
