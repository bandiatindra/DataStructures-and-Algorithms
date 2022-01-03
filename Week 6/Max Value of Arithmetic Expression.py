# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    n = int ((len(dataset) + 1)/2)
    ops = dataset[1::2]
    m = [[0] *(n) for i in range(n)]
    M = [[0] *(n) for i in range(n)] 
    
    

    # Assign intiital values to the diagonal
    for i in range (0, n):
        m[i] [i] = int(dataset[2*i])
        M[i] [i] = int(dataset[2*i])

        for s in range (1, n):
            for i in range (0,n-s):
                j = i + s
                m[i][j], M[i][j] = MinAndMax(m, M, i, j, ops)

    return M[0] [n-1]

def MinAndMax(m,M, i, j, ops):

    Maximum = float ('-inf')
    Minimum = float ('inf')

    for k in range (i, j):
        a = evalt(M[i][k], M[k+1][j], ops[k])
        b = evalt(M[i][k], m[k+1][j], ops[k])
        c = evalt(m[i][k], M[k+1][j], ops[k])
        d = evalt(m[i][k], m[k+1][j], ops[k])

        Maximum = max(Maximum, a, b, c, d)
        Minimum = min(Minimum, a, b, c, d)

    return Minimum, Maximum



if __name__ == "__main__":
    print(get_maximum_value(input()))
