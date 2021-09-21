# Write a Python version of hte Conjugate Gradient Method and use it to solve the systems:
import numpy as np


def conjugate_gradient_method(initial_guess, matrix_a, matrix_b, tol):
    (n, n) = matrix_a.shape
    x, r, d, alpha, beta = [], [], [], [], []

    x.append(initial_guess)
    r.append(matrix_b - matrix_a @ x[0])  # Residual fra første gjetning
    d.append(r[0])  # Start verdi starter med residualet
    for k in range(n):
        if np.linalg.norm(r[-1]) < tol:
            print(f"Ferdig etter {k} iterasjoner.")
            break
        alpha.append((r[k].dot(r[k])) / d[k].dot(matrix_a.dot(r[k])))
        x.append(x[k] + alpha[k] * d[k])
        r.append(r[k] - alpha[k] * matrix_a.dot(d[k]))
        beta.append((r[k + 1].dot(r[k + 1]) / (r[k].dot(r[k]))))
        d.append(r[k + 1] + beta[k] * d[k])
    return x[-1]


def main():
    machine_epsilon = 2 ** (-52)  # 0 også fungerer.
    # a)
    a = np.array([[1, 0], [0, 2]])
    b = np.array([2, 4])
    initial_guess = [1, 0]
    print(conjugate_gradient_method(initial_guess, a, b, machine_epsilon))

    # b)
    a_2 = np.array([[1, 2], [2, 5]])
    b_2 = np.array([1, 1])
    initial_guess = [1, 0]
    print(conjugate_gradient_method(initial_guess, a_2, b_2, machine_epsilon))


if __name__ == '__main__':
    main()
