# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [1,3,4]
    min_num_coins = [0]*(m+1)

    min_num_coins[0] = 0

    for i in range (1, m+1) :

        min_num_coins[i] = 10000000000
        
        for j in range(len(coins)):
            if i >= coins[j]:
                num_coins = min_num_coins[i - coins[j]] + 1
                if num_coins < min_num_coins[i]:
                    min_num_coins[i] = num_coins
    return min_num_coins[m]  
         

if __name__ == '__main__':
    m = int(sys.stdin.read())
    #m = int(input().split()[0])
   
    
    print(get_change(m))
