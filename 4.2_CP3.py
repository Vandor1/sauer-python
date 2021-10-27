# Consider the world population problem of Computer Problem 3.1.1. Find the best exponential fit of the data points
# by using linearization. Estimate the 1980 population, and find the estimation error.
import numpy as np
import matplotlib.pyplot as plt


def main():
    A = np.array([[1, 1960], [1, 1970], [1, 1990], [1, 2000]])
    b = np.array([[3039585530], [3707475887], [5281653820], [6079603571]])
    lstsq = np.linalg.lstsq(A, b, rcond=None)
    leastSquares = lstsq[0]
    print(leastSquares)
    function = lambda t: leastSquares[0] * np.exp(leastSquares[1] * t)

    year = np.array([1960, 1970, 1990, 2000], dtype=np.int64)
    population = np.array([3039585530, 3707475887, 5281653820, 6079603571])
    x_range = np.linspace(1960, 2000, 1000)

    plt.figure(figsize=(10, 6))
    plt.scatter(year, population)
    plt.plot(x_range, function(x_range), c='g')
    plt.show()

    error1 = np.sqrt(sum((population - function(year)) ** 2) / len(year))
    print("ESTIMATE 1980:", function(1980))
    print("RMSE: ", error1)


if __name__ == "__main__":
    main()
