class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_po = t_po =  0

        while s_po < len(s) and t_po < len(t):
            if s[s_po] == t[t_po]:
                s_po+=1
            t_po+=1
        
        return s_po == len(s)