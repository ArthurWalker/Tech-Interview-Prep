class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            are they sorted? not sorted
            empty? no
            can it be duplicated? no
            can it be negative? no

            if one item ? return itself
            [[1,5],[1,3],[6,7]]
            [[1,3],[2,5],[6,7]]

            i will sort by first element
            merged_list created
            iterate through the list
                if merged_lst is empty or last ele of merged_lst is smaller than item[0]:
                    append
                else:
                    if item[0] <= merged_lst[-1][-1]:
                        merged_lst[-1][-1] = max(item[-1],merged[-1][-1])
        """
        intervals.sort()
        merged_lst = []
        for item in intervals:
            if len(merged_lst) == 0 or merged_lst[-1][-1] < item[0]:
                merged_lst.append(item)
            elif item[0] <= merged_lst[-1][-1]:
                merged_lst[-1][-1] = max(item[-1],merged_lst[-1][-1])
        return merged_lst