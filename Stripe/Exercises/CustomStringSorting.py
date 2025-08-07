from typing import List

def customStringSort(arr: List[str]) -> List[str]:
    def split_data(item):
        # a22 -> ['a','22']
        res = []
        word = ''
        numbers =''
        for cha in item:
            if cha.isalpha():
                word+=cha
            else:
                numbers+=cha
        res.append(word)
        res.append(int(numbers)*(-1))
        return res

    arr.sort( key = lambda x: split_data(x))
    return arr

arr = ["a3", "a22", "b1", "b11", "a5"]
res = customStringSort(arr)
print(res)

print('Finished')

