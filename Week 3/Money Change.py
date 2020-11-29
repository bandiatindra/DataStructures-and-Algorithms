def money_change(n):
    
    ten_count = n//10
    five_count = (n%10)//5
    one_count = (n%10)%5

    total_count  = ten_count + five_count + one_count
    return total_count


if __name__ == '__main__':
    n = int (input())
    print (money_change(n))