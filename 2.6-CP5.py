# Use CGM to solve 2.45 for n = 100, 1000, 10000. Report the size of the final residual, and the number of steps
# required.
import numpy as np
import scipy.sparse as sp


def conjugate_gradient_method(initial_guess, matrix_a, matrix_b, tol):
    (n, n) = matrix_a.shape
    x, r, d, alpha, beta = [], [], [], [], []
    x.append(initial_guess)
    r.append(matrix_b - matrix_a @ x[0])  # Residual fra første gjetning
    d.append(r[0])  # Start verdi starter med residualet
    for k in range(n):
        print(np.linalg.norm(r[-1]))
        if np.linalg.norm(r[-1]) < tol:
            print(f"Ferdig etter {k} iterasjoner.")
            break
        alpha.append((r[k].dot(r[k])) / d[k].dot(matrix_a.dot(r[k])))
        x.append(x[k] + alpha[k] * d[k])
        r.append(r[k] - (alpha[k] * matrix_a.dot(d[k])))
        beta.append((r[k + 1].dot(r[k + 1])) / (r[k].dot(r[k])))
        d.append(r[k + 1] + beta[k] * d[k])
    return x[-1], k, r[-1]


def sparse_matrix_setup(n):
    A = np.zeros((n, n))
    for i in range(n):
        A[i, n - i - 1] = 1 / 2  # Needs to be first since '3' has priority.
        A[i, i] = 3

    for i in range(n):
        if i < n - 1:
            A[i, i + 1] = -1
            A[i + 1, i] = -1
    return A


def b_setup(a):
    (n, m) = np.shape(a)
    b = np.ones((n, 1))
    for i in range(n - 1):
        b[i] = 1.5
    b[-1], b[0] = 2.5, 2.5
    b[int(n / 2) - 1], b[int(n / 2)] = 1, 1
    return b


def main():
    a = sparse_matrix_setup(10)
    print(a)
    b = b_setup(a)
    # print(b)
    n, n = a.shape
    # print(n)
    initial_guess = np.zeros(n)
    # print(initial_guess)
    machine_epsilon = 2.0 ** (-52)
    x = conjugate_gradient_method(initial_guess, a, b, machine_epsilon)
    print(x)


if __name__ == '__main__':
    main()
