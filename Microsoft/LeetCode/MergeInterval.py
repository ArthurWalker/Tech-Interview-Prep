class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        res = []
        for inter in intervals:
            if len(res) == 0 or res[-1][-1] < inter[0]:
                res.append(inter)
            elif inter[1] >= res[-1][-1] >= inter[0]:
                res[-1][-1] = inter[1]
            else:
                pass
        return res