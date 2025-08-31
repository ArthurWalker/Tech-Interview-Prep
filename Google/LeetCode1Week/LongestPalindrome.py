class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        res = []
        def countPalindrome(start,end):
            while  start >=0 and end < len(s) and s[start] == s[end]:
                start-=1
                end+=1
            res.append(s[start+1:end])
            return end-start-1
            
        max_len = 0
        for i in range(len(s)):
            max_len = max(max_len,countPalindrome(i,i),countPalindrome(i,i+1)) 
        res = [item for item in res if len(item) == max_len]   
        return res[0]
