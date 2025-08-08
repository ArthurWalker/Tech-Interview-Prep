from typing import List

# if shop open + no customer => penalty +1
# if shop close + customer comes => penalty +1

def earlier_minimum_penalty(customers: str) -> int:
    close_dict = {}
    # iterate through the customers to calcalute penalty for each hour
    for close_time in range(len(customers)+1):
        penalty = 0
        for ind, cust_come in enumerate(customers):
            if (ind >= close_time and cust_come == 'Y') or (ind < close_time and cust_come == 'N'):
                penalty += 1
        close_dict[close_time] = penalty


    min_penalty = min(close_dict.values())
    for hour,penalty in close_dict.items():
        if penalty == min_penalty:
            return hour


customers = "NYNY"
res = earlier_minimum_penalty(customers)
print(res)
print("Finished")