import math


def main():
    a = 3344556600
    b = 1.2222222
    ans = b ** 2 / (math.sqrt(a ** 2 + b ** 2) + a)  # utregning for hånd.
    print(ans)


# 2.23322*10^-10

if __name__ == '__main__':
    main()
