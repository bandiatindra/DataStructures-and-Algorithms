import sys

def lcs2(a, b):
    #write your code here
    m = len(a) 
    n = len (b) 
    #Always intitalize 2d Array like this! 
      
        
    D = [[0]*(n+1) for i in range(m+1)]
    # The last row and column should remain zero as edge cases. 
        
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if a[i]==b[j]:
                D[i][j] = 1 + D[i+1][j+1]
            else:
                D[i][j] = max(D[i+1][j], D[i][j+1])
                    
    return D[0][0]

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
