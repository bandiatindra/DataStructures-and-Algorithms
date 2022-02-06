#Uses python3

import sys
# not correct solution needs changes. 
def lcs2(a, b):
    #write your code here
    m = len(a) 
    n = len (b) 
    #Always intitalize 2d Array like this! 
    D = [[0] * (n+1) for i in range(m+1)] 
    
    #Initialize edges
    for i in range(m+1):
       D[i][0] = i
       for j in range(n+1):
           D[0][j] = j
           
    count =0
    for i in range (1, m+1):
        for j in range (1,n+1):
            if a[i-1] == b[j-1]:
                count = count + 1

    return count

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
