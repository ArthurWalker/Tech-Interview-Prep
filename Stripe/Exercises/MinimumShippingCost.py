def minimum_shipping(shipping_data_string,source,destination):
    if len(shipping_data_string) == 0:
        return 0

    flights_lst = shipping_data_string.split(":")
    flights_cost = {}
    for travel in flights_lst:
        travel_split = travel.split(",")
        if (travel_split[0],travel_split[1]) in flights_cost:
            flights_cost[(travel_split[0], travel_split[1])].append([travel_split[2],travel_split[3]])
        else:
            flights_cost[(travel_split[0],travel_split[1])]=[[travel_split[2],travel_split[3]]]

    # direct cost
    cost_lst = []
    def direct_route():
        if (source,destination) in flights_cost:
            travels = flights_cost.get((source,destination))
            travel_cost = [int(carrier_cost[1]) for carrier_cost in travels]
            return min(travel_cost)
        return float('inf')
    direct_route_cst = direct_route()
    cost_lst.append(direct_route_cst)

    # one-hop travel
    def one_hop_route():
        res = []
        for (from_src, to_dest),carrier_cost in flights_cost.items():
            if from_src == source:
                from_hop = flights_cost.get((from_src,to_dest))
                to_hop = flights_cost.get((to_dest,destination))
                if to_hop:
                    from_one_cost = [int(carrier_cost[1]) for carrier_cost in from_hop]
                    to_one_cost = [int(carrier_cost[1]) for carrier_cost in to_hop]
                    res.append(min(from_one_cost)+min(to_one_cost))
        if len(res)>0:
            return min(res)
        return float('inf')
    one_hop_cst = one_hop_route()
    cost_lst.append(one_hop_cst)
    print(cost_lst)
    res =  min(cost_lst)
    if res == float('inf'):
        return -1
    return res

shipping_data_string = "US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7:US,UK,RoyalMail,12"
source = "US"
destination = "UK"
res = minimum_shipping(shipping_data_string,source,destination)
print(res)