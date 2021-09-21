import numpy as np


def bisection(f, a, b, N):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1, N + 1):
        m_n = (a_n + b_n) / 2
        f_m_n = f(m_n)
        if f(a_n) * f_m_n < 0:
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n) / 2


def func1(x): return x ** 3 - 9


def func2(x): return (3 * x ** 3 ) + (x ** 2) - x - 5


def func3(x): return (np.cos(x) ** 2) + 6 - x


def main():
    print(bisection(func1, 2, 3, 10))  # a
    print(bisection(func2, 1, 2, 10))  # b
    print(bisection(func3, 6.6, 6.8, 10))  # c


# Stuff here

if __name__ == '__main__':
    main()
