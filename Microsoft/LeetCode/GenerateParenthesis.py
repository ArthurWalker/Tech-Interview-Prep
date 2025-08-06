class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = ''
        def valid_pairs(text):
            stack = []
            for item in text:
                if item ==  ')':
                    if len(stack) ==0 :
                        return False
                    else:
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            return False
                else:
                    stack.append(item)
            if len(stack) == 0:
                return True
            return False
             
        def dfs(temp):
            count_open = temp.count('(')
            count_close = temp.count(')')
            if len(temp) == n*2:
                if valid_pairs(temp):
                    return res.append(temp)
                return
            else:
                dfs(temp+'(')
                dfs(temp+')') 
                return

        dfs(temp)
        return res

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         stack = []
#         res =[]
#         def backtrack(openPara,closePara):
#             if openPara == closePara == n:
#                 res.append("".join(stack))
#                 return
           
#             if openPara < n:
#                 stack.append('(')
#                 backtrack(openPara+1,closePara)
#                 stack.pop()
#             if closePara < openPara:
#                 stack.append(')')
#                 backtrack(openPara,closePara+1)
#                 stack.pop()
#         backtrack(0,0)
#         return res