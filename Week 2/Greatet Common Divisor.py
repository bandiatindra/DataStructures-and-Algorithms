
def GCD(a,b):
    if a > b:
        larger_num = a
        smaller_num  = b
    else:
        larger_num = b
        smaller_num = a

    rem = -1
    while rem!=0:
        rem = larger_num % smaller_num
        larger_num = smaller_num
        smaller_num = rem

    return  larger_num

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(GCD(a, b))