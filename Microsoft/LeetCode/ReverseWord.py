class Solution:
    def reverseWords(self, s: str) -> str:
        split_s = [val for val in s.split(' ')[::-1] if val !='']
        return ' '.join(split_s)