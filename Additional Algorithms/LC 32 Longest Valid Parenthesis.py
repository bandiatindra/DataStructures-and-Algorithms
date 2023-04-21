class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = []
        stack.append(-1)
        largest = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                
                stack.pop()
                if len(stack) !=0:
                    largest = max(largest, (i - stack[-1]))
            if len(stack) == 0:
                stack.append(i)
        return largest
             
            






