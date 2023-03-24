class Solution:
    import math
    def judgeSquareSum(self, c: int) -> bool:
        #Basic loop using sqrt    
        # for i in range(int(math.sqrt(c)) + 1):
        #     b = math.sqrt(c - i*i)
        #     if b == int(b):
        #         return True
        # return False

        #We can also using 2 pointer left & right and move left one ro right and right to left based on the value of their squared sum.
        l = 0
        r = int(math.sqrt(c))
        while r>=l:
            curr = l*l + r*r
            if c == curr:
                return True
            if curr > c:
                r = r-1
            if curr < c:
                l = l+1
        return False

        
