# Apply Euler's Method with step size h = 0.1 on [0,1] to the IVP in exercise 3. Print a table of the t values,
# Euler approximations, and error (difference from exact solution) at each step.
import numpy as np
from pandas import DataFrame as DF


def euler(y0, f, h, t):
    w = np.zeros(len(t))
    w[0] = y0
    for i in range(0, len(t) - 1):
        w[i + 1] = w[i] + h * (f(t[i], w[i]))
    return w


def exact_solution(t):
    return np.exp((t**3)/3)


def main():
    f = lambda t, y: (t ** 2) * y
    h = 0.1
    t = np.arange(0, 1 + h, h)
    w = euler(1, f, h, t)
    true_value = exact_solution(t)
    error = abs(true_value - w)
    print(DF({"t": t, "w": w, "Error": error, 'True value': true_value}).set_index('t')[['True value', 'w', 'Error']])


def exact_solution_a(t):
    return (t**2)/2 +1


def main_a():
    f = lambda t, y: t
    h = 0.1
    t = np.arange(0, 1 + h, h)
    w = euler(1, f, h, t)
    true_value = exact_solution_a(t)
    error = abs(true_value - w)
    print(DF({"t": t, "w": w, "Error": error, 'True value': true_value}).set_index('t')[['True value', 'w', 'Error']])



if __name__ == "__main__":
    print("A:")
    main_a()
    print("B:")
    main()
