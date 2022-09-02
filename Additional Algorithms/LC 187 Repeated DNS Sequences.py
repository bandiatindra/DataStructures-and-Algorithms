class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        L, n = 10, len(s)
        new_dict = {}
        result = []
        # Loop over each sequence of 10 characters! 
        for i in range (n-L+1):
            temp = s[i:i+L]
            if temp in new_dict:
                new_dict[temp]+=1
            else:
                new_dict[temp] = 1
        
        for key, value in new_dict.items():
            if value > 1:
                result.append(key)
        return result