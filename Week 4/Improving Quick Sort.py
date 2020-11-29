# Uses python3
import sys
import random

def partition3(a, l, r):
    #Whole idea is to compare if the ith element is larger than the last element.
    #If yes, then we swap it. This will automatically make sure that equal elements as the first one will be in the middle.

    x = a[l]
    j = l 
    end = r 
    i=j
    while i <= end:
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]

        elif a[i] > x:
            a[i], a[end] = a[end],a[i]
            end = end -1
            i=i-1 
        i=i+1

    a[l], a[j] = a[j], a[l] #Get the first element beetween the 2 regions.

    return j, end

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l] #Get the first element beetween the 2 regions.
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    print (k)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m,n = partition3(a, l, r)
    print (m,n)
    #m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, n + 1, r)


if __name__ == '__main__':
    #input = sys.stdin.read()
    n, *a = list(map(int, input().split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
