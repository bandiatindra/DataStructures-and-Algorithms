class SparseVector:
    def __init__(self, nums: List[int]):
        self.new_dic = {}
        for index, value in enumerate(nums):
            if value!=0:
                self.new_dic[index] = value

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for key, val in self.new_dic.items():
            if key in vec.new_dic:
                result += val *  vec.new_dic[key]
        return result

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)