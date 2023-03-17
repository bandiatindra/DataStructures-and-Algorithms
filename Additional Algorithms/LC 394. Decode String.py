class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        stack = []
        num = 1
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                new_char = ''
                while stack[-1]!= '[':
                    new_char = new_char + stack.pop()
                
                stack.pop() #Remove '[' from stack
                base = 1
                k=0
                while len(stack)>0 and  stack[-1].isdigit():
                    k = k + int(stack.pop())*base
                    base = base*10
                new_char = new_char * k
                for i in range(len(new_char)-1,-1,-1):
                    stack.append(new_char[i])  
                    
        for i in range(len(stack)):
            res = stack.pop() + res
        

        return res


