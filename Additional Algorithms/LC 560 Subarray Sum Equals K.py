class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # The idea is to give
        # Let's define an empty prefix in a dictionary which has a sum of zero. Its basically for the intital base case saying there is a prefix before the start of the array. 
        prefix_sum = {0:1} 
        curr_sum = 0
        res = 0
        # Then we wil iterate through the array and add a prefix if 
        for i in range(len(nums)):
            curr_sum = curr_sum + nums[i]
            psum = curr_sum - k #This is the prefix sum which if we add to our sub-array will give us k. 
        # If we do not have this psum in prefix_sum dictionary:
        # Then let's add the current sum or increase count of curr_sum by 1
        
            if psum not in prefix_sum:
                if curr_sum not in prefix_sum:
                    prefix_sum[curr_sum] = 1
                else:
                    prefix_sum[curr_sum]+=1
            # if we have psum in prefix_sum dictionary: 
            # Then We have found a prefix sum, which if we add to curr_sum will give us k.
            
            # We still need to add the curr_sum or increase its count to prefix_sum dic
            # this is needed to keep the current sum at the current array point. 

            else:
                res+= prefix_sum[psum]
                if curr_sum not in prefix_sum:
                    prefix_sum[curr_sum] = 1
                else:
                    prefix_sum[curr_sum]+=1
        return res



        