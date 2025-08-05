from typing import List

import re

# def convert_word(s:str) -> List[str]:
#     result = []
#     i = 0
#     while i < len(s):
#         if s[i] == '{':
#             end = s.find('}', i)
#             if end == -1:
#                 raise ValueError("Mismatched braces")
#             group = s[i+1:end].split(',')
#             result.append(group)
#             i = end + 1
#         else:
#             result.append([s[i]])
#             i += 1
#     return result


def convert_word(word_list:str) -> List[str]:
    list_word = []
    i = 0
    sublist = []
    in_bracket = False
    while i < len(word_list):
        if word_list[i] == '{':
            if len(sublist) > 0:
                list_word.append(sublist)
            sublist = []
            in_bracket = True
        elif word_list[i] == '}':
            list_word.append(sublist)
            sublist = []
            in_bracket = False
        else:
            if word_list[i] != ',':
                if not in_bracket:
                    temp = sublist.pop() if len(sublist)> 0 else ""
                    list_word.append(temp+word_list[i])
                else:
                    sublist.append(word_list[i])
        i += 1
    if len(sublist) > 0:
        list_word.append(sublist)
    return list_word



def brace_expansion(word_list: str) -> List[str]:
    # {a,b,c}d{e,f} => [[a,b,c],[d],[e,f]]
    formatted_word = convert_word(word_list)
    res = []
    def dfs(po,created_term):
        if po == len(formatted_word):
            res.append(created_term)
            return

        for letter in formatted_word[po]:
            created_term +=letter
            dfs(po+1,created_term)
            created_term = created_term[:-1]
        return

    dfs(0,'')
    res.sort()
    return res

resuilt =brace_expansion('abcd')

