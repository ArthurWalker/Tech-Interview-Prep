from typing import List

def customStringCompress(text: str) -> str:
    if len(text) <=2:
        return text

    # split by /
    slash_split = text.split("/")
    minor_list = []
    # [['s4e', 'c1m'], ['p6s'], ['c6t'], ['c6r', 'j2n', 'd1e']]
    for major in slash_split:
        dot_split = major.split(".")
        new_dot_split = []
        for minor in dot_split:
            new_formated = ''
            if len(minor)<=2:
                new_formated+=minor
            else:
                new_formated=minor[0]+str(len(minor)-2)+minor[-1]
            new_dot_split.append(new_formated)
        dot_formatted = '.'.join(new_dot_split)
        minor_list.append(dot_formatted)
    res = '/'.join(minor_list)
    return res

text ="s/tri"
res = customStringCompress(text)
print(res)
print('Finished')