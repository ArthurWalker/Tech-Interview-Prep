def calucalteion(quer,variable_hash):
    second_var = quer[1]
    first_var = quer[0]
    stack_cal = []
    while second_var not in first_var and second_var not in stack_cal:
        if len(stack_cal) ==0:
            stack_cal = (variable_hash[first_var])
        else:
            replaced_value = stack_cal.pop()
            stack_cal+=(variable_hash[replaced_value])

    res = stack_cal[0]
    operator= ''
    for element in stack_cal[1:-2]:
        if element in ["*","/"]:
            operator = element
        else:
            if operator  == '*':
                res = res*element
            else:
                res = res/element
    return res

def evaluation_division(equations,values, queries):
    variable_hash = {}

    for index, equation in enumerate(equations):
        if equation[0] not in variable_hash:
            variable_hash[equation[0]] = [values[index],'*',equation[1]]

    for index, equation in enumerate(equations):
        if equation[1] not in variable_hash:
            variable_hash[equation[1]] = [equation[0],'/',str(values[index])]

    saved_res = []
    for quer in queries:
        new_cal = calucalteion(quer,variable_hash)
        saved_res.append(new_cal)

    return saved_res

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
result = evaluation_division(equations,values, queries)