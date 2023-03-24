class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:

        max_dist = 0
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            
            if nums2[j] < nums1[i]:
                i = i+1

            elif nums2[j] >= nums1[i]:
                max_dist = max(max_dist, (j-i))
                j = j+1
        return max_dist
