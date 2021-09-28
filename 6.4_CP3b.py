# Carry out the steps of CP2, but plot the approximate solutions on [0, 1] for step sizes h = 0.1, 0.05, and 0.025,
# along with the true solution.
import numpy as np
import matplotlib.pyplot as plt


def RK4(y0, h, f, t):
    w = np.zeros(len(t))
    w[0] = y0
    for i in range(len(t) - 1):
        s1 = f(t[i], w[i])
        s2 = f(t[i] + (h / 2), w[i] + (h / 2) * s1)
        s3 = f(t[i] + (h / 2), w[i] + (h / 2) * s2)
        s4 = f(t[i] + h, w[i] + h * s3)
        w[i + 1] = w[i] + (h / 6) * (s1 + (2 * s2) + (2 * s3) + s4)
    return w


# Task A)
def mainA():
    y0 = 1
    f = lambda t, y: t  # From exercise 6.4.1
    exact = lambda t: (t ** 2) / 2 + 1  # From exercise 6.1.3
    # Next time use; for h in (0.1, 0.05, 0.025)

    h = 0.1
    t = np.arange(0, 1 + h, h)
    w = RK4(y0, h, f, t)
    print("h = 0.1: ", w)
    plt.plot(t, w, label="Approximation with h: 0.1")

    h = 0.05
    t = np.arange(0, 1 + h, h)
    w = RK4(y0, h, f, t)
    print("h = 0.05: ", w)
    plt.plot(t, w, label="Approximation with h: 0.05")

    h = 0.025
    t = np.arange(0, 1 + h, h)
    w = RK4(y0, h, f, t)
    print("h = 0.025: ", w)
    plt.plot(t, w, label="Approximation with h: 0.025")

    exact_value = exact(t)
    plt.plot(t, exact_value, label="Exact value")

    plt.legend()
    plt.show()


# Task B)
def mainB():
    y0 = 1
    f = lambda t, y: (t ** 2) * y  # From exercise 6.4.1
    exact = lambda t: np.exp((t ** 3) / 3)  # From exercise 6.1.3
    # Next time use; for h in (0.1, 0.05, 0.025)

    h = 0.1
    t = np.arange(0, 1 + h, h)
    w = RK4(y0, h, f, t)
    print("h = 0.1: ", w)
    plt.plot(t, w, label="Approximation with h: 0.1")

    h = 0.05
    t = np.arange(0, 1 + h, h)
    w = RK4(y0, h, f, t)
    print("h = 0.05: ", w)
    plt.plot(t, w, label="Approximation with h: 0.05")

    h = 0.025
    t = np.arange(0, 1 + h, h)
    w = RK4(y0, h, f, t)
    print("h = 0.025: ", w)
    plt.plot(t, w, label="Approximation with h: 0.025")

    exact_value = exact(t)
    plt.plot(t, exact_value, label="Exact value")

    plt.legend()
    plt.show()


if __name__ == '__main__':
    mainA()
    mainB()
