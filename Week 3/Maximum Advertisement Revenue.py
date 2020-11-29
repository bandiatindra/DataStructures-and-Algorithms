import sys
import numpy as np

def max_dot_product(a,b):

    a_sort = sorted (a, reverse = True)
    b_sort = sorted(b, reverse = True)

    return np.dot(a_sort, b_sort)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    