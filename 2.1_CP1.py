# Create a program for "naive" Gaussian elimination.
import numpy as np


def main(A):
    # Shape of the matrix in question (3, 4) in our question.
    (n, m) = np.shape(A)

    # Perform gaussian elimination - algorithm borrowed from Jordan Barry
    for j in range(n - 1):
        for i in range(j + 1, n):
            A[i, :] = -(A[i, j] / A[j, j]) * A[j, :] + A[i, :]
    return A


# Backsubstitution
def backsub(A):
    (n, m) = np.shape(A)
    x = np.zeros(m - 1)

    for i in np.arange(n - 1, -1, -1):
        x[i] = (A[i, -1] - A[i, 0:m - 1] @ x) / A[i, i]
    return x


if __name__ == '__main__':
    A = np.array([[2, -2, -1, -2], [4, 1, -2, 1], [-2, 1, -1, -3]])
    print("Gausselim:")
    print(main(A))
    print("Backsubstitution:")
    print(backsub(A))
