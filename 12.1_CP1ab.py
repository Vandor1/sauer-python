# Use provided power iteration algorithm to find dominant eigenvector of A and estimate the dominant eigenvalue by
# calculating a Rayleigh quotient. Compare conclusions with exercise 5.
import numpy as np


def power_iteration(x, A, n=40):
    for _ in range(0, n):
        eigenvector = x / np.linalg.norm(x)  # normalize vector
        x = A.dot(eigenvector)  # power step
        # eigenvalue = np.matmul(np.transpose(eigenvector), x)  # Rayleigh quotient
        eigenvalue = eigenvector.dot(x)  # Rayleigh quotient
    eigenvector = x / np.linalg.norm(x)
    return eigenvalue, eigenvector


def main():
    A = np.array([[10, -12, -6], [5, -5, -4], [-1, 0, 3]])  # Matrix for a)
    B = np.array([[-14, 20, 10], [-19, 27, 12], [23, -32, -13]])  # Matrix for b)
    n, m = np.shape(A)
    x = np.ones(n)
    # print("A:")
    # print(power_iteration(x, A))
    #
    # # n, m = np.shape(B)
    # print("\nB:")
    # print(power_iteration(x, B))
    print(power_iteration(A, x, 10))


if __name__ == "__main__":
    main()
