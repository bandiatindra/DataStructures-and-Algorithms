class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        n = len(nums)
        if (target + total_sum) % 2==1 or total_sum < abs(target):
            return 0 
        if n == 0 and target == 0:
            return 1
        
        new_target = (target + total_sum)//2
        dp = [[0 for j in range(new_target + 1)] for i in range (n+1)]
        dp[0][0] = 1

        for i in range(1,n+1):
            for j in range(new_target + 1):
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j - nums[i-1]]
        return dp[n][new_target]




        