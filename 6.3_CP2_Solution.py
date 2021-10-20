import numpy as np
pi = np.pi
exp = np.exp
sqrt = np.sqrt
sin = np.sin
cos = np.cos


def Trapezoid_method(f, a, b, h, y_0):
    n = int((b - a) / h)
    d = len(y_0)

    t = np.linspace(a, b, n + 1)
    w = np.zeros((d, n + 1))
    w[:, 0] = y_0

    for i in range(n):
        w[:, i + 1] = w[:, i] + (f(t[i], w[:, i]) + f(t[i] + h, w[:, i] + h * f(t[i], w[:, i]))) * (h / 2)

    return t, w


def f(t, y):
    y1, y2 = y
    return np.array([y1 + y2, -y1 + y2])


def exact_sol(t):
    return np.array([exp(t)*cos(t), -exp(t)*sin(t)])


def main():
    a, b = 0, 1
    y_0 = (1, 0)

if __name__ == '__main__':
    main()
