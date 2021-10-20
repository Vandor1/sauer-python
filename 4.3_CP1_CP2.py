# Write a program that implements classical Gram-Schmidt to find the reduced QR factorization.
import numpy as np


def numpygramschmidt(X):
    Q, R = np.linalg.qr(X)
    return Q, R


def gramschmidt(A):
    n, m = np.shape(A)
    r = np.zeros((m, m))
    q = np.zeros((n, n))

    for j in range(n):
        y = A[:, j]
        for i in range(j):
            r[i, j] = np.dot(np.transpose(q[i, :]), A[:, j])
            y = y - np.dot(r[i, j], q[i])
        r[j, j] = np.sqrt(np.sum(y ** 2))
        q[j] = y / r[j, j]
    return r, q


def modifiedgramschmidt(A):
    n, m = np.shape(A)
    r = np.zeros((m, m))
    q = np.zeros((n, n))

    for j in range(n):
        y = A[:, j]
        for i in range(j):
            r[i, j] = np.dot(np.transpose(q[i, :]), y)  # <- change A[:,j] to y.
            y = y - np.dot(r[i, j], q[i])
        r[j, j] = np.sqrt(np.sum(y ** 2))
        q[j] = y / r[j, j]
    return r, q


def main():
    A = np.array([[4, 0], [3, 1]])
    Q, R = numpygramschmidt(A)
    r, q = gramschmidt(A)
    mr, mq = modifiedgramschmidt(A)
    print("Solution:")
    print("Q:\n", Q)
    print("R:\n", R)
    print("\nMy algorithm:")
    print("Q:\n", q)
    print("R:\n", r)
    print("\nMy Modified:")
    print("Q:\n", mq)
    print("R:\n", mr)


if __name__ == "__main__":
    main()
