#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here

    m = len(a) 
    n = len (b)
    l = len(c)

    
    D = [[[0]*(n+1) for i in range(m+1)] for j in range (l+1)]

    for i in range(l-1,-1,-1):
        for j in range(m-1,-1,-1):
            for k in range(n-1,-1,-1):
                if c[i]==a[j]==b[k]:
                    D[i][j][k] = 1 + D[i+1][j+1][k+1]
                else:
                    D[i][j][k] = max(D[i+1][j][k], D[i][j+1][k],D[i][j][k+1])

    return D[0][0][0]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))