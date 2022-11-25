class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_sum =  -1000000000000
        leftIndex = 0
        rightIndex = n-1
        while leftIndex < rightIndex:
            if nums[leftIndex] > k/2:# Optimization ot break from the loop if its True. Because, nums[rightIndex] will. be >k/2 if nums[leftIndex] is >k/2. Hence the sum will alaways be > k.
                break
            if nums[leftIndex] + nums[rightIndex] >= k:
                rightIndex = rightIndex - 1
            else:
                
                max_sum = max(max_sum, nums[leftIndex] + nums[rightIndex])
                leftIndex = leftIndex + 1
            
        return max(max_sum, -1)
            
            
        