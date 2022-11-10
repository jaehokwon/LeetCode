class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        calc = 0
        
        for c in s:
            if c == '(':
                calc += 1
            else:
                calc -= 1
            
            if calc > 1 - (c == ')'):
                stack.append(c)
        
        return ''.join(stack)