#Uses python3

import sys

def Isgreater(x,max_digit):
    if x + max_digit >= max_digit + x:
        return x
    else:
        return max_digit

def largest_number(a):
    res = ""
    while len(a)!=0 :
        max_digit = 0
    
        for x in a:
            max_digit = Isgreater(str(x),str(max_digit))

        a.remove(max_digit)
        res = res + max_digit        
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
