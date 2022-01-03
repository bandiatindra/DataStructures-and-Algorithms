# Uses python3
import sys

def optimal_sequence(n):
    min_operations = [0]*(n+1) # So that min_operations [n] is there. 
    min_operations [1] = 1 #Assign the first length of operations.
    numOps = 0
    seq = [0]*(n+1)

    for i in range (1,n+1):
        k = i-1
        min_operations[i] = min_operations[i-1]  + 1
        
        if i % 3 == 0:
            numOps = min_operations[i//3] + 1
            if numOps < min_operations [i]:
                min_operations [i] = numOps
                k = i//3

        if i % 2 == 0:
            numOps = min_operations[i//2] + 1
            if numOps < min_operations [i]:
                min_operations [i] = numOps
                k = i//2

        seq [i] = k      
    
    sequence = []
    while n >= 1:
        sequence.append(n)
        n = seq [n]
        
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
