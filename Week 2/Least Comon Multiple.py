
def LCM (a,b):

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

    GCD = larger_num
    return int(a*b/GCD)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(LCM(a, b))