class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        # Generic Function for K Sum
        def ksum (nums, target, k):
            result = []
            if not nums:
                return result
            if k!=2:
                for i in range(len(nums)):
                    if i ==0 or nums[i]!= nums[i-1]:
                        #quad.append(nums[i])
                        for subset in ksum(nums[i+1:], target - nums[i], k-1):
                            result.append([nums[i]] + subset)
                        
            if k ==2:
                return twoSums(nums, target)
            
            return result
            
        # Base case scenario
        def twoSums (nums, target):
            res = []
            low = 0
            high = len(nums) - 1
            
            while low < high:
                curr_sum = nums[low] + nums [high]
                if curr_sum < target:
                    low = low +1
                elif curr_sum > target:
                    high = high - 1
                else:
                    res.append([nums[low], nums[high]])
                    low = low + 1
                    high = high - 1
                    # This ensures that duplicate records are not included
                    while low < high and nums [low] == nums[low-1]:
                        low = low + 1
            return res
        
        return ksum(nums, target, k=4)
        
        