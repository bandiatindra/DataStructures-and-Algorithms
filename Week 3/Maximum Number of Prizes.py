import sys

def optimal_summands(n):
    summands = []
    #write your code here
    if n ==2:
        summands.append(2)
        return summands
        
    distinct_integer = 1 
    summands.append(distinct_integer)  
    n = n - distinct_integer

    while n!=0:

        distinct_integer = distinct_integer + 1
        n = n - distinct_integer
        if n <=  distinct_integer: #When this happens, there is no possible number other than the previous n itself.
            n= n + distinct_integer
            summands.append(n)
            return  summands     
        else:
            summands.append(distinct_integer)
                        
    return summands

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
