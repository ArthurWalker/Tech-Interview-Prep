from typing import List

def penatly_shop(customers: str) -> int:
    # Condition to calculate penalty:
    # if customer[i] == 'Y' while i is closed => Penalty
    # if customer[i] == 'N' while i is open => Penalty

    close_dict = {}
    for close_time in range(0,len(customers)+1):
        penalty = 0
        for ind, cust_come in enumerate(customers):
            if (ind >= close_time and cust_come =='Y') or (ind < close_time and cust_come =='N'):
                penalty +=1
        close_dict[close_time] = penalty

    min_time = min(close_dict.values())
    for k,v in close_dict.items():
        if v == min_time:
            return k
    return 0

res = penatly_shop('NNNYYYY')
print(res)
