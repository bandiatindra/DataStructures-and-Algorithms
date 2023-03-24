class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        path = path.split('/')
        for portion in path:
            if portion =='..':
                if stack:
                    stack.pop()
            elif portion == '.' or not portion:
                continue
            else:
                stack.append(portion)
        return '/' + '/'.join(stack)
