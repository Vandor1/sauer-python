# Create a script to setup LU factorization with no row exchanges allowed. Shut down on zero pivot.
import numpy as np


def gausselim(A, identityM):
    # Shape of the matrix in question (3, 4) in our question.
    (n, m) = np.shape(A)
    # Perform gaussian elimination - algorithm borrowed from Jordan Barry
    for j in range(n - 1):
        for i in range(j + 1, n):
            #Setup L (LU)
            multiple = A[i, j] / A[j, j]
            identityM[i,j] = multiple
            #Gauss elim
            A[i, :] = -(A[i, j] / A[j, j]) * A[j, :] + A[i, :]
    return A, identityM


def main():
    A = np.array([[3, 2, 1], [6, 3, 4], [3, 1, 5]])
    n,m=np.shape(A)
    M = np.identity(n)
    U, L = gausselim(A, M)
    print(U)
    print("________")
    print(L)


if __name__ == "__main__":
    main()
