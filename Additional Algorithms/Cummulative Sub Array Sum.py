def findSum(numbers, queries):
    # Write your code here
    res = []
    zero_cnt = 0
    zero_arr = []
    sub_arr_sum = []
    
    for i in range(len(numbers)):
        if numbers[i]==0:
            zero_cnt+=1
            zero_arr.append(zero_cnt)
        else:
            zero_arr.append(zero_cnt)
        if i == 0:
            sub_arr_sum.append(numbers[i])
        else:
            sub_arr_sum.append(numbers[i]+sub_arr_sum[i-1])
     
    
    for query in queries:
        curr_sum = 0
        l = query[0]-1
        r = query[1]-1
        x = query[2]
        if l == 0:
            curr_sum = sub_arr_sum[r] - 0
            num_zero = zero_arr[r] - 0
        else:
            curr_sum = sub_arr_sum[r] - sub_arr_sum[l-1]
            num_zero = zero_arr[r] - zero_arr[l-1]
            
        
        curr_sum = curr_sum + num_zero*x
        res.append(curr_sum)
    return res
    