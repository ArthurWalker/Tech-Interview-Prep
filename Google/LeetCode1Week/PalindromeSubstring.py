class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        def countPalindrome(start,end):
            count = 0
            while  start >=0 and end < len(s) and s[start] == s[end]:
                count+=1
                start-=1
                end+=1
            return count
             
        total = 0
        for i in range(len(s)):
            total += countPalindrome(i,i) + countPalindrome(i,i+1)    
        return total
