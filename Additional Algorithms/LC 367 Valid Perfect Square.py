class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        def binary_search(l,r,num):
            x = (l+r)//2
            
            if r>=l:

                if x*x == num:
                    return True
                if x*x > num:
                    return binary_search(l,x-1, num)
                if x*x < num:
                    return binary_search(x+1,r,num)
            return False
            


        return binary_search(2, num/2, num)
        
       #The implementation uses a binary search algorithm to find the square root of the input number num. 
       # The binary search is performed between 2 and num/2 since the square root of any number n is at most n/2.
       # The binary search function binary_search takes three parameters l, r, and num. 
       # The parameters l and r represent the left and right endpoints of the search interval, respectively. The parameter num represents the input number.
       # The binary search function first computes the midpoint x of the interval (l, r) using integer division.
       #  If the midpoint x squared is equal to the input number num, the function returns True. 
       # If the midpoint x squared is greater than the input number num, the function recursively searches the left half of the interval (l, x-1). 
       # If the midpoint x squared is less than the input number num, the function recursively searches the right half of the interval (x+1, r).
       # If the binary search does not find a perfect square root in the interval, the function returns False.
       # Note that the special case of num being less than 2 is handled separately, as any integer less than 2 is a perfect square.



