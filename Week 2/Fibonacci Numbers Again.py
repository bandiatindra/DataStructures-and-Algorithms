
def Fibonnaci_period (n,m):

    arr = [0 for i in range (m*m + 1)] 
    arr[0] = 0
    arr[1] = 1

    for i in range(2, m*m + 1):
        arr[i] = (arr[i-1] + arr[i-2])%m 
        if arr[i] == 1 and arr[i-1] == 0 :
            return i-1  

def Fibonnaci_Again (n,m):
    if n<=1:
        return n
    
    else:

        arr = [0 for i in range(n+1)] 
        arr[0] = 0
        arr[1] = 1

        for i in range(2,n+1):
            arr[i] = (arr[i-1]%m + arr[i-2]%m)%m

        return arr[n]

if __name__ == '__main__':
    a, b = map(int, input().split())
    period = Fibonnaci_period(a, b)
    print (Fibonnaci_Again(a%period,b))
