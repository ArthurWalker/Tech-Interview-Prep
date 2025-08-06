class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <=1:
            return len(s)

        max_str = set()
        max_len = 0
        left = 0
        for right in range(len(s)):
            while s[right] in max_str:
                max_str.remove(s[left])
                left+=1
            max_len = max(max_len,right-left+1)
            max_str.add(s[right])
                
        if len(max_str) > max_len:
            max_len = len(max_str)
        return max_len