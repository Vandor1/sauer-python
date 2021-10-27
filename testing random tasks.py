import numpy as np
from scipy.linalg import lu
import math


# conditional values etc.
def main():
    #4.1 2a)
    A = np.array([[1,1,0],[0,1,1],[1,2,1],[1,0,1]])
    b = np.array([2,2,3,4]).reshape(4,1)
    x = np.array([2,-1/3,2]).reshape(3,1)
    z = b- np.dot(A,x)
    print(np.sqrt((z[0]**2 + z[1]**2 + z[2]**2 + z[3]**2)/2))

    #4.1 3)
    c = [[1,0],[1,0],[1,0]]
    d = [[1],[5],[6]]
    ct = np.transpose(c)
    print(np.dot(ct,c))

    #4.1 8a)
    e = [[1,1,1,1],[0,1,2,5]]
    g = [[1,0],[1,1],[1,2],[1,5]]
    b2 = [[0],[3],[3],[6]]
    print(np.dot(e,g))
    print(np.linalg.lstsq(g,b2,rcond=None))
    x2 = [[0.857142],[15/14]]
    z2 = b2-np.dot(g,x2)
    print(np.sqrt((z2[0]**2 + z2[1]**2 + z2[2]**2 + z2[3]**2)/2))

    # A = np.matrix([[1, 2.01], [3, 6]])
    # B = np.matrix([[1, 2], [3, 4]])
    # eigB = np.linalg.eig(B)
    # Ainf = np.linalg.norm(A, np.inf)
    # Acond = np.linalg.cond(A)
    # inverse = np.linalg.inv(A)
    # print(eigB)


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
    main()
    # print(g(1.1))
    #
    # x = sy.Symbol("x")
    # print(sy.integrate(f(x), (x, -3.0, 3.0)))

