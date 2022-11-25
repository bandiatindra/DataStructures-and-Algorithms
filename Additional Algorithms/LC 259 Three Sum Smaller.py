class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        result = 0
        # We need to traverse for n-2 index only, otherwise we will get index overflow
        for i in range(n-2):
            new_target = 0
            new_target += target - nums[i]
            result = result + self.twoSum (nums, i+1, new_target )
            
        return result
            
    def twoSum(self, nums, startIndex, target):
        count = 0
        leftIndex = startIndex
        rightIndex = len(nums) - 1
        
        while leftIndex < rightIndex:                       
            if nums[rightIndex] + nums[leftIndex] >= target:
                rightIndex = rightIndex - 1
            else:
                count = count + rightIndex - leftIndex #If nums[lefIndex] + nums[rightIndex] in a sorted array is < target, then all possible pairs with leftIndex in between leftIndex and rightIndex will also satisfy this property.
                leftIndex = leftIndex + 1
        return count
                    
                
        
        
        