# The idea here is to calculate the max before current index . The idea issimilar to Kadane's Algorithm
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        prevmaxodd = nums[0]
        prevmaxEven = 0
        for i in range(1,len(nums)):
            temp = prevmaxodd
            prevmaxodd = max(prevmaxodd,prevmaxEven + nums[i])
            prevmaxEven = max(prevmaxEven, temp - nums[i])
        return prevmaxodd


            