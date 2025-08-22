class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def depth_first_traversal(iter_lst,curr_lst):
            if len(iter_lst)==0:
                res.append(curr_lst[:])
                return
            
            for item in iter_lst:
                curr_lst.append(item)
                depth_first_traversal([num for num in iter_lst if num!= item],curr_lst)
                curr_lst.pop()


        depth_first_traversal(nums,[])
        return res