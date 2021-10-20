import numpy as np
from scipy.linalg import lu


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
    # 2.4, 3b)
    # A = np.array([[3, 1, 2], [6, 3, 4], [3, 1, 5]])
    # A = np.array([[-1, 0, 1], [2, 1, 1], [-1, 2, 0]])
    # p, l, u = lu(realA)

    Q = np.array([[2 / 3, 1 / 3, 0], [1 / 3, -2 / 3, -2 / 3], [0, 2 / 3, -2 / 3], [2 / 3, 0, 1 / 3]])
    Qt = np.transpose(Q)
    A = np.array([[2, -1, 4], [1, -3, -9], [0, 2, -2], [2, -2, 5]])
    R = np.dot(Qt, A)
    print(R)


def main4():
    A = np.array([[1000, 999], [1001, 1000]])


if __name__ == '__main__':
    # A = np.array([[2, -2, -1, -1], [4, -4, -2, -2], [0, 2, 3, -1], [6, -4, 0, -4], [5, -6, -2, -2]])
    main3()
