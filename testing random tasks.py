import numpy as np
from scipy.linalg import lu
import math


# conditional values etc.
def main():
    A = np.matrix([[1, 2.01], [3, 6]])
    B = np.matrix([[1, 2], [3, 4]])
    eigB = np.linalg.eig(B)
    Ainf = np.linalg.norm(A, np.inf)
    Acond = np.linalg.cond(A)
    inverse = np.linalg.inv(A)
    print(eigB)


# finding norms.
def main2():
    matrix = np.matrix([[1, 5, 1], [-1, 2, -3], [1, -7, 0]])
    norm = np.linalg.norm(matrix, 1)
    print(norm)


# PA = LU Factorization using scipy.
def main3():
    # 2.4, 2c) A = np.array([[1, 2, -3], [2, 4, 2], [-1, 0, 3]])
    #2.4, 3b)
    # A = np.array([[3, 1, 2], [6, 3, 4], [3, 1, 5]])
    # # A = np.array([[-1, 0, 1], [2, 1, 1], [-1, 2, 0]])
    # B = np.array([[1, 2, -1, 2], [0, 3, 1, 4], [2, -1, 1, 2]])
    # C = np.array([[4, 2, 0], [4, 4, 2], [2, 2, 3]])
    # D = np.array([[1, 2, -3], [2, 4, 2], [-1, 0, 3]])
    # E = np.array([[3, 2, 1], [6, 3, 4], [3, 1, 5]])
    # p, l, u = lu(E)
    # print(p)
    # print(l)
    # print(u)
    Q = np.array([[2/3,-1/3],[-2/3,-2/3],[1/3,-2/3]])
    R = np.array([[3,6],[0,3]])
    print(np.dot(Q,R))


import sympy as sy

def f(x):
    return x ** 4 * (sy.sin(x) * sy.cos(x) +1)

import math

def g(x):
    return 3*math.exp(1-x**2)

if __name__ == "__main__":
    print(g(1.1))

    x = sy.Symbol("x")
    print(sy.integrate(f(x), (x, -3.0, 3.0)))

