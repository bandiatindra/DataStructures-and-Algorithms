
def last_digit_fibonnaci (n):

    if n==0:
        return 0

    if n==1:
        return 1
    
    else:

        arr = [0 for i in range(n+1)] 
        arr[0] = 0
        arr[1] = 1

        for i in range(2,n+1):
            arr[i] = (arr[i-1] + arr[i-2])%10 #Storing only the last digit. 

        return (arr[n])

if __name__ == '__main__':
    a = int (input())
    
    print (last_digit_fibonnaci(a))