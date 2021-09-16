# Use the Jacobi Method to solve the spare system within six correct decimal places
# (forward error in the infinity norm) for n = 100 and n = 100000. The correct solution is [1,...,1].
# Report the number of steps needed and the backward error. The system;
# Special thanks to riverlike14 on GitHub.
# https://github.com/riverlike14/Numerical_Analysis/blob/master/Ch_02/Ch_2_5.ipynb
import numpy as np


def jacobi(A, b, num_iter, initial_guess=0):
    n = len(A)
    D = np.diag(A)
    R = A - np.diag(D)
    x = initial_guess * np.ones(n)
    for j in range(num_iter):
        x = (b - R.dot(x)) / D
    return x


def sparseMatrixSetup(n):
    A = np.zeros((n, n))
    for i in range(n):
        A[i, i] = 3
        if i < n - 1:
            A[i, i + 1] = -1
            A[i + 1, i] = -1
    return A


def bSetup(A):
    (n, m) = np.shape(A)
    b = np.ones((n, 1))
    b[-1], b[0] = 2, 2
    return b


def main(n):
    A = sparseMatrixSetup(n)
    b = bSetup(A)
    x_true = np.ones(n)  # det står i oppgaven
    j = 0
    guess = np.zeros(n)

    while True:
        guess = jacobi(A, b, 1, guess)
        j += 1
        forward_error = abs(guess - x_true).max()
        if forward_error < 5e-7:
            break
    backward_error = abs(A.dot(guess) - b).max()

    print("Number of iterations:", j)
    print("Backward error:", backward_error)


if __name__ == '__main__':
    main(100)
