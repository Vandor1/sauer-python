# Consider the world population problem of Computer Problem 3.1.1. Find the best least squares (a) line, (b) parabola
# through the data points, and the RMSE of the fit. In each case, estimate the 1980 population. Which fit gives the
# best line?
import numpy as np
import matplotlib.pyplot as plt


def main():
    # A
    A = np.array([[1, 1960], [1, 1970], [1, 1990], [1, 2000]])
    b = np.array([[3039585530], [3707475887], [5281653820], [6079603571]])
    lstsq = np.linalg.lstsq(A, b, rcond=None)
    leastSquares = lstsq[0]
    function = lambda t: leastSquares[0] + t * leastSquares[1]

    year = np.array([1960, 1970, 1990, 2000], dtype=np.int64)
    population = np.array([3039585530, 3707475887, 5281653820, 6079603571])
    x_range = np.linspace(1960, 2000, 1000)
    plt.scatter(year, population)
    plt.plot(x_range, function(x_range), c='g')
    plt.show()

    error1 = np.sqrt(sum((population - function(year)) ** 2) / len(year))
    print("ESTIMATE 1980:", function(1980))
    print("RMSE: ", error1)
    # B
    A = np.array([[1, 1960, 1960 ** 2], [1, 1970, 1970 ** 2], [1, 1990, 1990 ** 2], [1, 2000, 2000 ** 2]])
    b = np.array([[3039585530], [3707475887], [5281653820], [6079603571]])
    lstsq = np.linalg.lstsq(A, b, rcond=None)
    leastSquares = lstsq[0]
    function = lambda t: leastSquares[0] + t * leastSquares[1] + t ** 2 * leastSquares[2]

    year = np.array([1960, 1970, 1990, 2000], dtype=np.int64)
    population = np.array([3039585530, 3707475887, 5281653820, 6079603571])
    x_range = np.linspace(1960, 2000, 1000)
    plt.scatter(year, population)
    plt.plot(x_range, function(x_range), c='g')
    plt.show()

    error2 = np.sqrt(sum((population - function(year)) ** 2) / len(year))
    print("ESTIMATE 1980:", function(1980))
    print("RMSE: ", error2)
    print("    ")
    if (error2 > error1):
        print("Line is best!")
    else:
        print("Parabola gives the best model!")


if __name__ == "__main__":
    main()
