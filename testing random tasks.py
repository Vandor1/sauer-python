import numpy as np
from scipy.linalg import lu
import math


def main():
    A = np.array([[1, 1, 0], [0, 1, 1], [1, 2, 1], [1, 0, 1]])
    b = np.array([2, 2, 3, 4]).reshape((4, 1))  # This will return a matrix with array elements.
    AT = np.transpose(A)
    ATA = np.dot(AT, A)
    ATb = np.dot(AT, b)
    #print(ATb)
    newX = np.array([1, (-2 / 3), 2]).reshape(3, 1)
    r = b-A.dot(newX)
    #print(math.sqrt((r[0]**2 + r[1]**2 + r[2]**2 + r[3]**2)/2))
    print(np.linalg.lstsq(A,b,rcond=None))


if __name__ == "__main__":
    main()
