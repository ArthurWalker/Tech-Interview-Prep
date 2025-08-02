class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        def binary_search():
            left, right = 0, len(intervals)-1

            while left <= right:
                mid = (right+left)//2
                if intervals[mid] ==  newInterval[0]:
                    return mid
                if newInterval[0] >  intervals[mid][0]:
                    left = mid+1
                else:
                    right = mid-1
            return left
        insert_po = binary_search()
        new_intervals = intervals[:insert_po]+[newInterval]+intervals[insert_po:]
        res = []
        for inter in new_intervals:
            if len(res) == 0 or res[-1][1] < inter[0]:
                res.append(inter)
            elif res[-1][1]>=inter[0]:
                res[-1][1] = max(res[-1][1],inter[1])

        return res
