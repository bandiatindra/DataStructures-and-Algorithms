class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        if n==0:
            return False
        new_set = set()
        sum_digits = 0
        while sum_digits != 1:
            sum_digits = 0
            for i in range(len(str(n))):
                digit = int(str(n)[i])
                sum_digits = sum_digits + digit*digit
            n = sum_digits
            if sum_digits not in new_set:
                new_set.add(sum_digits)
            else:
                return False
        return True
     
        