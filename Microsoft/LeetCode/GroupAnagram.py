class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            sorted_word = list(word)
            sorted_word.sort()
            temp = ''.join(sorted_word)
            if temp not in res:
                res[temp] = [word]
            else:
                res[temp].append(word)

        return list(res.values())
            
        