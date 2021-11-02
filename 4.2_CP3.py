# Consider the world population problem of Computer Problem 3.1.1. Find the best exponential fit of the data points
# by using linearization. Estimate the 1980 population, and find the estimation error.
import numpy as np

def main():
    A = np.array([[1, 0], [1, 10], [1, 30], [1, 40]])
    b = np.array([[np.log(3039585530)], [np.log(3707475887)], [np.log(5281653820)], [np.log(6079603571)]])
    b2 = np.array([[(3039585530)], [(3707475887)], [(5281653820)], [(6079603571)]])
    lstsq = np.linalg.lstsq(A, b, rcond=None)
    lhs = A.T@A
    rhs = A.T@b
    ans = np.linalg.solve(lhs,rhs)
    print(ans)
    r = b - A@ans

    leastSquares = lstsq[0]
    function = lambda t: leastSquares[0] * np.exp(leastSquares[1]*t)
    leastSquares[0] = np.exp(leastSquares[0])

    RMSE = np.sqrt(sum((b2 - r) ** 2) / len(b2))

    print("ESTIMATE 1980:", function(20))
    print("RMSE: ", RMSE)


if __name__ == "__main__":
    main()
