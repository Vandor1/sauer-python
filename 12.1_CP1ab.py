# Use provided power iteration algorithm to find dominant eigenvector of A and estimate the dominant eigenvalue by
# calculating a Rayleigh quotient. Compare conclusions with exercise 5.
import numpy as np


def poweriteration(x, u, A, eig, n):

    for j in range(0, n):
        u[j-1] = x[j-1] / np.sqrt(np.sum(x[j-1] ** 2)) #normalize vector
        x[j] = np.dot(A, u[j-1]) #power step
        eig[j] = np.transpose(u[j-1]) * x[j] # Rayleigh quotient
    u[j] = x[j] / np.sqrt(np.sum(x[j] ** 2))
    return u

def main():
    A = np.array([[10, -12, -6], [5, -5, -4], [-1, 0, 3]])  # Matrix for a)
    B = np.array([[-14, 20, 10], [-19, 27, 12], [23, -32, -13]])  # Matrix for b)
    n, m = np.shape(A)

    
    n, m = np.shape(B)





if __name__ == "__main__":
    main()
