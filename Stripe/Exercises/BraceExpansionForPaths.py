def brace_expansion(input):
    if len(input) == 0:
        return []
    elif "{" not in input or "}" not in input:
        return input

    open_bracket_ind = input.index("{")
    close_bracket_ind = input.index("}")

    bracket_split  = input[open_bracket_ind+1:close_bracket_ind].split(',')
    if len(bracket_split) < 2 or close_bracket_ind < open_bracket_ind:
        return input
    res = []
    for item in bracket_split:
        combined_txt = input[:open_bracket_ind]+item+input[close_bracket_ind+1:]
        res.append(combined_txt)

    return res

input = 'hello-}-weird-{-world'
result = brace_expansion(input)
print(result)
print("Finished")