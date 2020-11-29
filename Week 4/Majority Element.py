# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        #Couldnt find any maximum
        return -1
    if left + 1 == right: #When only one element
        return a[left]
    #Code to split the aray t halves and recurrsively call the function
    
    mid = (left + right)//2
    b = get_majority_element(a,mid,right)
    c = get_majority_element(a,left,mid)
    #Code to merge the array. If 2 halves agree on the majority, return it. 
    
    #Otherwise count each element and return the element with a higher count in the sub array.  
    b_count = sum(1 for i in range (left,right) if a[i]==b)
    c_count = sum(1 for i in range (left,right) if a[i]==c)

    if b_count > (right - left)//2:      
        return b

    elif c_count > (right - left)//2:
        return c
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
