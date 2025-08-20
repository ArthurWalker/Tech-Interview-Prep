class Solution:
    def quicksort(self, lst):
        if len(lst) <= 1:
            return lst

        pivot = lst.pop()
        lower = []
        higher = []
        for item in lst:
            if item[0] > pivot[0]:
                higher.append(item)
            else:
                lower.append(item)
        return self.quicksort(lower) + [pivot] + self.quicksort(higher)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        new_intervals = self.quicksort(intervals)
        res = []
        for item in new_intervals:
            if len(res) == 0 or res[-1][1] < item[0]:
                res.append(item)
            else:
                res[-1][-1] = max(res[-1][-1], item[1])
        return res