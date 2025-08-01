class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0,len(s)-1
        while left < right:
            
            if s[left] not in 'aeiouAEIOU':
                left+=1
            if s[right] not in 'aeiouAEIOU':
                right-=1

            if left != right and s[left] in 'aeiouAEIOU' and s[right] in 'aeiouAEIOU':
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left+=1
                right-=1
        return ''.join(s)