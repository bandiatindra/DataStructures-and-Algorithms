class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        start = 0
        end = 0
        n = len(s)
        while start < n:
            while  end <n and s[end]!= " ":
                end  = end + 1
            s[start:end] = reversed(s[start:end])
            
            
            start = end + 1
            end  = start
        return s