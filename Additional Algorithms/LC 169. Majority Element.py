class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Approach 1  - Hash Map
        # if len(nums) == 1:
        #     return nums[0]
        # hash_map={}
        # for i in range(len(nums)):
        #     if nums[i] in hash_map:
        #         hash_map[nums[i]]+=1
        #         if hash_map[nums[i]] > len(nums)/2:
        #             return nums[i]
        #     else:
        #         hash_map[nums[i]] = 1
        #return max(hash_map, key=hash_map.get)
        
        # Approach 2 - Boyer-Moore Voting Algorithm
        majority_element = None
        
        counter = 0
        for num in nums:
            if counter ==0:
                majority_element = num
            if majority_element == num:
                counter += 1
            else:
                counter -=1
        return majority_element
                
