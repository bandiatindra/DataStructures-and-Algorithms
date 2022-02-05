class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        D = [[0] * (n) for i in range(n)] 
        
        # Set the diagnoal to 1 
        for i in range(n):
            D[i][i] = 1
            # Assign any diagnol as longest palindrome
            longest_palindrome = s[i]
            
                
        # In reverse order from bottom to up
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                # Check if the last letters of the sub-string to be checked are same
                if s[i]==s[j]:
                    # If the last letters are same, check if the sub string after removing these letters is also a palindrome OR if the current substring is adjacent chracters. Then the substring in question will be a palindrome. 
                    if j-i ==1 or D[i+1][j-1] == 1:
                        D[i][j] = 1
                        # Finaly check if the length is greated that currently assigned length of palindrome
                        if len(longest_palindrome) < len(s[i:j+1]):
                            longest_palindrome = s[i:j+1]
            
           
        return longest_palindrome