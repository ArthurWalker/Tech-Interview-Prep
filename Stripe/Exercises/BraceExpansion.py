from typing import List

def convert_word(input):
    stack = []
    txt = ''
    for ele in input:
        if ele == '{':
            if len(txt)>0:
                stack.append([txt])
            txt = ''
        elif ele == '}':
            txt_split =  txt.split(',')
            stack.append(txt_split)
            txt = ''
        else:
            txt+=ele
    if len(txt)>0:
        stack.append([txt])
    return stack

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

