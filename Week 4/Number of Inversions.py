# Uses python3
import sys

def merged_sort(b1,c):
    i, j = 0, 0
    sorted_array = []
    number_of_inversions = 0
    
    
    while i < len(b1) and j < len (c):
        if b1[i] <= c[j]:            
            sorted_array.append(b1[i])            
            i = i+1

        else :            
            sorted_array.append(c[j])
            j=j+1            
            number_of_inversions = number_of_inversions + len(b1)  - i
            
    sorted_array = sorted_array + b1[i:]
    sorted_array = sorted_array + c[j:]   

    return sorted_array, number_of_inversions

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0

    if right == left + 1:        
        return a[left:right],0

    ave = (left + right) // 2
    
    b1, i1 = get_number_of_inversions(a, b, left, ave)
    c, i2 = get_number_of_inversions(a, b, ave, right)
    sorted_array, i3 = merged_sort(b1,c)
    number_of_inversions = i1+i2+i3

    return sorted_array, number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    sorted_list, numberofinversions= get_number_of_inversions(a, b, 0, len(a))
    print(numberofinversions)
