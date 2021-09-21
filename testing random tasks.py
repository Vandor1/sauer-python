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
    # 2.4, 3b) A = np.array([[3, 1, 2], [6, 3, 4], [3, 1, 5]])
    A = np.array([[-1, 0, 1], [2, 1, 1], [-1, 2, 0]])

    p, l, u = lu(A)
    print(p)
    print(l)
    print(u)

if __name__ == '__main__':
    main3()
