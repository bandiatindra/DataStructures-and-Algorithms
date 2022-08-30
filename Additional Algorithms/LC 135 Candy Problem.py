class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        #Brute force Approach - Too slow! 
#         n = len(ratings)
#         candies = [1]*n
#         hasChanged = True
#         while hasChanged is True:
#             hasChanged = False
#             for i in range(n):
#                 if i!=0 and ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
#                     candies[i] = candies[i-1] + 1
#                     hasChanged = True
#                 if i!=n-1 and ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
#                     candies[i] = candies[i+1] + 1
#                     hasChanged = True
        
#         return sum(candies)
    
    # Approach 2 - 2 arays. start from left and right simultaneously
        n = len(ratings)
        left_arr = [1]*n
        right_arr = [1]*n
        sum = 0

        for i in range(1,n):
            if i!=0 and ratings[i] > ratings[i-1]:
                left_arr[i] = left_arr[i-1] + 1
        for i in range(n-2,-1, -1):
            if i!=n-1 and ratings[i] > ratings [i+1]:
                right_arr[i] = right_arr[i+1] + 1
        for i in range(n):
            sum = sum + max(left_arr[i],right_arr[i])
        return sum

    
                    
        
        