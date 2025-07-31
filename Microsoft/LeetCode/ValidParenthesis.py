class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            elif s[i] == ')' and len(stack) > 0 and stack[-1] =='(':
                stack.pop()
            elif s[i] == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            elif s[i] == '}' and len(stack)>0 and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(s[i])
        
        if len(stack) == 0:
            return True
        return False