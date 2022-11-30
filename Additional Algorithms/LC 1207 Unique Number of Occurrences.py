class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        new_dict = {}
        
        for i in range(len(arr)):
            if arr[i] in new_dict:
                new_dict[arr[i]] += 1
            else:
                new_dict[arr[i]] = 1
        # occurence = {}
        # for val in new_dict.values():
        #     if val in occurence:
        #         return False
        #     else: 
        #         occurence[val] = 1
        # return True
        return len(set(new_dict.values())) == len(set(arr))