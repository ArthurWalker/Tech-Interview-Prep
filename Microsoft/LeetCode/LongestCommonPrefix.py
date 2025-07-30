class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <=1:
            return strs[0]
        strs.sort(key = lambda x: len(x))
        print(strs)
        max_len = ""
        for i in range(len(strs[0])):  
            temp = [s[:i+1] for s in strs]
            print(temp,strs[:i+1])
            if len(set(temp))==1 and len(temp[0])> len(max_len):
                max_len = temp[0]
        return max_len
        