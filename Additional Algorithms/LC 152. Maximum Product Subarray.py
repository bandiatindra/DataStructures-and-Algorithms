class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_ending_here = nums[0]
        min_ending_here = nums[0]
        max_so_far = nums[0]

        for i in range(1,len(nums)):
            temp = max(nums[i], max_ending_here*nums[i],min_ending_here*nums[i])
            min_ending_here = min(nums[i], max_ending_here*nums[i],min_ending_here*nums[i] )
            max_ending_here = temp
            max_so_far = max(max_so_far,max_ending_here)

        return max_so_far