import numpy as np


# conditional values etc.
def main():
    A = np.matrix([[1, 2.01], [3, 6]])
    B = np.matrix([[1, 2], [3, 4]])
    eigB = np.linalg.eig(B)
    Ainf = np.linalg.norm(A, np.inf)
    Acond = np.linalg.cond(A)
    inverse = np.linalg.inv(A)
    print(eigB)


if __name__ == '__main__':
    main()


# finding norms.
def main2():
    matrix = np.matrix([[1, 5, 1], [-1, 2, -3], [1, -7, 0]])
    norm = np.linalg.norm(matrix, 1)
    print(norm)
