# Uses python3
import sys
import random

def fast_count_segments(starts, ends, points):
    cnt_dict = {}
    cnt = [0]* len(points)

    Left_suffx = ['L']*len(starts)
    Right_suffx = ['R']*len(ends)
    Points_suffx = ['P']*len(points)

    combined_arr = starts + ends + points
    combined_arr_suffix = Left_suffx + Right_suffx + Points_suffx
    merged_arr = zip (combined_arr,combined_arr_suffix)
   
    #randomized_quick_sort(combined_arr,combined_arr_suffix, 0, len(merged_arr)-1)

    merged_arr = sorted(merged_arr, key=lambda tup: (tup[0],tup[1]) )
    count = 0
    
    
    for i in range(len(merged_arr)):
        if merged_arr[i][1] == 'L':
            count = count + 1
            
        elif merged_arr[i][1] == 'R':
            count = count -1
        else:
            cnt_dict[merged_arr[i][0]] = count
            
    for i in range(len(points)):
        cnt[i] = cnt_dict[points[i]]
    

    return  cnt


def partition3(a, b, l, r):

    #Ideally we should use this function for sorting,
    #But need to figure out how to sort a tuple using Quick Sort. 
    #Hence using Python's in built sorting functionality.
    
    x = a[l]    
    j = l 
    end = r 
    i=j
    while i <= end:
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
            b[i], b[j] = b[j], b[i]

        elif a[i] > x:
            a[i], a[end] = a[end],a[i]
            b[i], b[end] = b[end],b[i]
            end = end -1
            i=i-1 
        
        i=i+1

    #Get the first element beetween the 2 regions.
    a[l], a[j] = a[j], a[l] 
    b[l], b[j] = b[j], b[l] 

    return j, end


def randomized_quick_sort(a, b, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    b[l], b[k] = b[k], b[l]

    #use partition3
    m,n = partition3(a, b, l, r)  
       
    randomized_quick_sort(a, b, l, m - 1)
    randomized_quick_sort(a, b, n + 1, r)

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    
    for x in cnt:
        print(x, end=' ')
