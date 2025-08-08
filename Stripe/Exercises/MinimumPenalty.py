from typing import List

# if shop open + no customer => penalty +1
# if shop close + customer comes => penalty +1

def earlier_minimum_penalty(customers: str) -> int:
    pentaly_dictary = {}
    # iterate through the customers to calcaluta penalty for each hour
    for hour in range(len(customers)+1):
        # if shop open + no customer
        shop_open = customers[:hour]
        shop_close = customers[hour:]
        penalty_hour = 0
        for open_hour in shop_open:
            if open_hour == 'N':
                penalty_hour+=1
        for close_hour in shop_close:
            if close_hour == 'Y':
                penalty_hour+=1
        pentaly_dictary[hour] = penalty_hour


    min_penalty = min(pentaly_dictary.values())
    for hour,penalty in pentaly_dictary.items():
        if penalty == min_penalty:
            return hour


customers = "NYNY"
res = earlier_minimum_penalty(customers)
print(res)
print("Finished")