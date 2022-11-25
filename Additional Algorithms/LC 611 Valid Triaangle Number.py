class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        n = len(nums)
        count = 0
        for i in range (n-1,1,-1):
            leftIndex = 0
            rightIndex = i-1
            while leftIndex < rightIndex:
                if (nums[leftIndex] + nums[rightIndex]) > nums[i]:
                    count = count + rightIndex - leftIndex
                    rightIndex = rightIndex - 1
                else:
                    leftIndex = leftIndex + 1
        return count