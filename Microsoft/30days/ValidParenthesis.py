class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            '[':']',
            '{':'}',
            '(':')'
        }
        stack = []
        for char in s:
            if char in parenthesis:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if parenthesis[stack[-1]] == char:
                        stack.pop()
                    else:
                        return False
        if len(stack)==0:
            return True
        return False