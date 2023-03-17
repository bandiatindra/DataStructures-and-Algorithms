class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range (len(tokens)):
            if tokens[i]=='+' or tokens[i] == '-' or tokens[i]=='*' or tokens[i] =='/':
                num_2 = int(stack.pop())
                num_1 = int(stack.pop())
                new_num = 0
                if tokens[i] == '+':
                    new_num = num_1 + num_2
                if tokens[i]== '-':
                    new_num = num_1 - num_2
                if tokens[i] == '*':
                    new_num = num_1 * num_2
                if tokens[i] == '/':
                    new_num = int(num_1 / num_2)
                stack.append(new_num)


            else:
                stack.append(tokens[i])
        return int(stack[0])
