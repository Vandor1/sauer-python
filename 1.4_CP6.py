# A 10-cm-high cone contains 60cm^3 of ice cream, including a hemispherical scoop on top. Find the radius of the scoop
# to four correct decimal places.
# Cone = (pi * r^2 * h)/3
# Hemisphere = 2/3 * pi * r^3
# f(r) = pi*r^2*10 + 2*pi*r^3 - 180

import numpy as np


def main(f, Df, x0, epsilon, max_iter):
    xn = x0
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after', n, 'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn / Dfxn
        print(xn)
    print('Exceeded maximum iterations. No solution found.')
    return None


if __name__ == '__main__':
    f = lambda r: (np.pi * r ** 2 * 10) + (2 * np.pi * r ** 3) - 180
    df = lambda r: (20 * r * np.pi) + (6 * np.pi * r**2)
    main(f, df, 1, 1e-10, 10)
