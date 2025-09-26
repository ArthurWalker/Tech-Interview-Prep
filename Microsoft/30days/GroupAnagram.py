class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        dicta = {}
        for item in strs:
            new_item = ''.join(sorted(item))
            if new_item not in dicta:
                dicta[new_item] = [item]
            else:
                dicta[new_item].append(item)
        
        return list(dicta.values())