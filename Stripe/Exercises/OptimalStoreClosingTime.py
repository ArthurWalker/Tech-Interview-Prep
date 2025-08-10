def computePenalty(log, closingTime):
    log = log.split()
    if len(log) == 0 :
        return 0
    penalty = 0
    for hour,customer_arrive in enumerate(log):
        if (hour < closingTime and customer_arrive == 'N') or (hour >= closingTime and customer_arrive=='Y'):
            penalty+=1
    return penalty

def getClosingWithMinPenalty(log):
    # log = log.split()
    if len(log) == 0:
        return 0
    hour_penalty = {}
    for close_hour in range(len(log)+1):
        penalty = computePenalty(log,close_hour)
        hour_penalty[close_hour] = penalty
    min_penalty = min(hour_penalty.values())
    for hour,penalty in hour_penalty.items():
        if penalty == min_penalty:
            return hour

def getAllClosingTimes(log):
    if len(log) == 0:
        return []
    log_split = log.split()
    stack_begin_end = []
    store = []
    store_lst = []
    i = 0
    while i < len(log_split):
        if log_split[i] == 'BEGIN':
            stack_begin_end.append(log_split[i])
        elif log_split[i] != 'END':
            store.append(log_split[i])
        else:
            store_lst.append(' '.join(store))
            store = []
        i+=1

    penalty_store = [getClosingWithMinPenalty(store) for store in store_lst]
    return penalty_store


log = "BEGIN BEGIN BEGIN Y Y N Y END Y Y N N END Y N Y N END"
closingTime = 0
# result1 = computePenalty(log,closingTime)
# result2 = getClosingWithMinPenalty(log)
result3 = getAllClosingTimes(log)
print(result3)
print('Finished')