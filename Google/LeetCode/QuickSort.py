def quicksort(lst):
    if len(lst) <=1 :
        return lst

    pivot = lst.pop()
    lower_lst = []
    higher_lst = []

    for item in lst:
        if item > pivot:
            higher_lst.append(item)
        else:
            lower_lst.append(item)

    return quicksort(lower_lst)+[pivot]+quicksort(higher_lst)

lst = [0,9,3,8,2,7,5]
print(quicksort(lst))



