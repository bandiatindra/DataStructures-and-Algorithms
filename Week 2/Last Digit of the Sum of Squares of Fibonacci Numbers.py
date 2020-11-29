def last_digit_SS_fibonnaci (n):

    if n<= 1:
        return n
    
    else:

        arr = [0 for i in range(n+1)] 
        arr[0] = 0
        arr[1] = 1

        for i in range(2,n+1):
            arr[i] = (arr[i-1]%10 + arr[i-2]%10)%10 #Storing only the last digit. 
            # next_lasdigit = (arr[i]%10 + arr[i-1]%10)%10
            # arr[i] = (curr_lastdigit * next_lasdigit)%10
            


        return ((arr[n] * (arr[n]%10 + arr[n-1]%10)%10 )%10)

if __name__ == '__main__':
    a = int (input())
    print (last_digit_SS_fibonnaci(a%60)) #Using the Fibonnaci Period Logic
 
   