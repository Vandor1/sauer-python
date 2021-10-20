# Write a program that implements classical Gram-Schmidt to find the reduced QR factorization.
import numpy as np


def gramschmidt(A):
    n,m = np.shape(A)
    r = []
    q = []
    for j in range(n+1):
        y = A[:,j]
        for i in range(j):
            r[i, j] = np.dot(np.transpose(q[i]), A[j])
            y  = y - np.dot(r[i,j],q[i])
            print(y)
        normalized_y = y / np.sqrt(np.sum(y ** 2))
        print(normalized_y)
        r[j,j] = normalized_y
        q[j] = y / r[j,j]
    return r[j,j], q[j]

def main():
    A = np.array([[4,0],[3,1]])
    print(gramschmidt(A))


if __name__ == "__main__":
    main()
