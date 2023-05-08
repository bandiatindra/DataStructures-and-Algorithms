def subset_sum(nums, target):
    n = len(nums)
    dp = [[False for j in range(target+1)] for i in range (n+1)]
    
    # Base case  - When the value or target is zero then its true for all possible sub-sets. 
    for i in range(n+1):
        dp[i][0] = True
    
    for i in range(1, n+1):
        for j in range(1,target+1):
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
    return dp[n][target]



