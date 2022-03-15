class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        arr = [True] * len(s)
        stack = []
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    arr[i] = False
        for idx in stack:
            arr[idx] = False
        
        res = ''
        for i, char in enumerate(s):
            if arr[i]:
                res += char
        
        return res