# Write a Python version of hte Conjugate Gradient Method and use it to solve the systems:
import numpy as np


def conjugateGradientMethod(initialGuess, matrix_A, matrix_b, tol):
    (n, n) = matrix_A.shape
    x = []
    r = []
    d = []
    alpha = []
    beta = []
    x.append(initialGuess)
    r.append(matrix_b - matrix_A @ x[0])
    d.append(r[0])
    for k in range(n):
        if np.linalg.norm(r[k])<tol:
            break
        alpha.append ....

    print(matrix_b - matrix_A @ x[0])

    # d = r = matrix_b - matrix_A * initialGuess
    # for k in range(0, n):
    #     if(r[k] = 0):
    #         break
    #     elif:
    #         matrix_b+=1


def main():
    A = np.array([[1, 0], [0, 2]])
    b = np.array([2, 4])
    print(conjugateGradientMethod(1, A, b, 0))



if __name__ == '__main__':
    main()
