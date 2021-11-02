import numpy as np
import matplotlib.pyplot as plt


# conditional values etc.
def main():
    print("4.1 2a)")
    A = np.array([[1, 1, 0], [0, 1, 1], [1, 2, 1], [1, 0, 1]])
    b = np.array([2, 2, 3, 4]).reshape(4, 1)
    x = np.array([2, -1 / 3, 2]).reshape(3, 1)
    z = b - np.dot(A, x)
    print(np.sqrt((z[0] ** 2 + z[1] ** 2 + z[2] ** 2 + z[3] ** 2) / 4))

    print("\n4.1 3)")
    c = [[1, 0], [1, 0], [1, 0]]
    d = [[1], [5], [6]]
    ct = np.transpose(c)
    print(np.dot(ct, c))

    print("\n4.1 8a)")
    e = [[1, 1, 1, 1], [0, 1, 2, 5]]
    g = [[1, 0], [1, 1], [1, 2], [1, 5]]
    b2 = [[0], [3], [3], [6]]
    print(np.dot(e, g))
    print(np.linalg.lstsq(g, b2, rcond=None)[0])
    x2 = [[0.85714286], [1.07142857]]
    z2 = b2 - np.dot(g, x2)
    print(np.sqrt((z2[0] ** 2 + z2[1] ** 2 + z2[2] ** 2 + z2[3] ** 2) / 4))


# finding norms.
def main2():
    matrix = np.matrix([[1, 5, 1], [-1, 2, -3], [1, -7, 0]])
    norm = np.linalg.norm(matrix, 1)
    print(norm)


# PA = LU Factorization using scipy.
def main3():
    # 2.4, 2c) A = np.array([[1, 2, -3], [2, 4, 2], [-1, 0, 3]])
    # 2.4, 3b)
    # A = np.array([[3, 1, 2], [6, 3, 4], [3, 1, 5]])
    # # A = np.array([[-1, 0, 1], [2, 1, 1], [-1, 2, 0]])
    # B = np.array([[1, 2, -1, 2], [0, 3, 1, 4], [2, -1, 1, 2]])
    # C = np.array([[4, 2, 0], [4, 4, 2], [2, 2, 3]])
    # D = np.array([[1, 2, -3], [2, 4, 2], [-1, 0, 3]])
    # E = np.array([[3, 2, 1], [6, 3, 4], [3, 1, 5]])
    # p, l, u = lu(E)
    # print(p)
    # print(l)
    # print(u)
    Q = np.array([[2 / 3, -1 / 3], [-2 / 3, -2 / 3], [1 / 3, -2 / 3]])
    R = np.array([[3, 6], [0, 3]])
    print(np.dot(Q, R))


def main4():
    # F3(t)
    A = np.array([
        [1.0, np.cos(0.0), np.sin(0.0)],
        [1.0, np.cos(np.pi / 3.0), np.sin(np.pi / 3.0)],
        [1.0, np.cos(np.pi * (2.0 / 3.0)), np.sin(np.pi * (2.0 / 3.0))],
        [1.0, np.cos(np.pi), np.sin(np.pi)],
        [1.0, np.cos(np.pi * (4.0 / 3.0)), np.sin(np.pi * (4.0 / 3.0))],
        [1.0, np.cos(np.pi * (10.0 / 6.0)), np.sin(np.pi * (10.0 / 6.0))]
    ])
    b = np.array([4, 2, 0, -5, -1, 3]).reshape((6, 1))
    b2 = np.array([4, 2, 0, -5, -1, 3])
    leastSquares = np.linalg.lstsq(A, b, rcond=None)[0]
    f3 = lambda t: leastSquares[0] + np.cos(2 * np.pi * t) * leastSquares[1] + np.sin(2 * np.pi * t) * leastSquares[2]
    i = np.array([0, 1 / 6, 1 / 3, 1 / 2, 2 / 3, 5 / 6], dtype=np.int64)
    RMSE1 = np.sqrt(sum((b2 - f3(i)) ** 2) / len(i))
    print(RMSE1)
    # x_range = np.linspace(0, 3, 1000)
    # plt.scatter(i, b2)
    # plt.plot(x_range, f3(x_range), c='g')
    # plt.show()

    # F4(t)
    A2 = np.array([
        [1.0, np.cos(0.0), np.sin(0.0), np.cos(0 * 4.0 * np.pi)],
        [1.0, np.cos(np.pi / 3.0), np.sin(np.pi / 3.0), np.cos(4.0 * np.pi * (1 / 6))],
        [1.0, np.cos(np.pi * (2.0 / 3.0)), np.sin(np.pi * (2.0 / 3.0)), np.cos(4.0 * np.pi * (1 / 3))],
        [1.0, np.cos(np.pi), np.sin(np.pi), np.cos(4.0 * np.pi * (1 / 2))],
        [1.0, np.cos(np.pi * (4.0 / 3.0)), np.sin(np.pi * (4.0 / 3.0)), np.cos(4.0 * np.pi * (2 / 3))],
        [1.0, np.cos(np.pi * (10.0 / 6.0)), np.sin(np.pi * (10.0 / 6.0)), np.cos(4.0 * np.pi * (5 / 6))]
    ])
    b3 = np.array([4, 2, 0, -5, -1, 3]).reshape((6, 1))
    b4 = np.array([4, 2, 0, -5, -1, 3])
    leastSquares2 = np.linalg.lstsq(A2, b3, rcond=None)[0]
    f4 = lambda t: leastSquares2[0] + np.cos(2 * np.pi * t) * leastSquares2[1] + np.sin(2 * np.pi * t) * leastSquares2[
        2] + leastSquares2[3] * np.cos(4 * np.pi * t)
    RMSE2 = np.sqrt(sum((b4 - f4(i)) ** 2) / len(i))
    print(RMSE2)

    print("    ")
    if (RMSE2 < RMSE1):
        print("Second model is best!")
    else:
        print("First model is best!")


def main5():
    Q = np.array([[2 / 3, 1 / 3, 0], [1 / 3, -2 / 3, -2 / 3], [0, 2 / 3, -2 / 3], [2 / 3, 0, 1 / 3]])
    A = np.array([[2, -1, 4], [1, -3, -9], [0, 2, -2], [2, -2, 5]])
    qt = np.transpose(Q)
    R = np.dot(qt, A)
    print(R)


if __name__ == "__main__":
    main()
