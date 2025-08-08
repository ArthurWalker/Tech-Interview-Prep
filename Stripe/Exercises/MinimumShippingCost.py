from typing import List

from django.views.static import directory_index


# Notes:
# Wont guarantee to have both cases existing
# The format is exactly like described, no special characters
# Guarentee to have full description for each shippign
# Guarentee there will be no duplication of FROM_LOCATION,TO_LOCATION,CARRIER

# Edge cases:
# more than one item format
# Shipping to itself
# Empty String data
# Very high cost
# Only one route

def min_directRoutes(shippign_dict, source: str, destiation: str) -> int:
    # Return minimum cost of direct routes
    res = []
    if (source, destiation) in shippign_dict:
        carrier_cost = shippign_dict[(source, destiation)]
        res = carrier_cost
    if len(res) == 0:
        return -1
    else:
        res.sort(key=lambda x: x[1])
        return res[0][1]

def min_oneHopeRoutes(shippign_dict, source: str, destiation: str) -> int:
    # Return minimum cost of one hop routes
    # Expected {("US","UK"):["UPS":5], ("US","CA"):["FedEx":3], ("CA","UK"):[["DHL",7]]}
    one_hope_dict = {}
    routes = list(shippign_dict.keys())
    for i in range(len(routes)-1):
        for j in range(len(routes)):
            if routes[i][0]== source and routes[j][1] == destiation and routes[i][1]==routes[j][0]:
                key_hop = (source,routes[i][1],destiation)
                first_route = shippign_dict[routes[i]][0][1]
                second_route = shippign_dict[routes[j]][0][1]
                one_hope_dict[key_hop] = first_route+second_route
    # {(US,CA,UK):10}
    res = (one_hope_dict.values())
    return min(res) if len(res) > 0 else -1


def minimumshipping(shipping_data_string: str, source: str, destiation: str) -> int:
    if source == destiation:
        return 0
    elif len(shipping_data_string) == 0:
        return -1

    # ["US,UK,UPS,5","US,CA,FedEx,3","CA,UK,DHL,7"]
    shipping_lst = shipping_data_string.split(":")
    shipping_dict = {}

    # {("US","UK"):[["UPS":5]], ("US","CA"):[["FedEx":3]]}
    for item in shipping_lst:
        element = item.split(",")
        from_lo, to_lo, carrier, cost = element[0],element[1],element[2],int(element[3])
        if (from_lo,to_lo) not in shipping_dict:
            shipping_dict[(from_lo,to_lo)] = [[carrier,cost]]
        else:
            shipping_dict[(from_lo,to_lo)].append([carrier,cost])


    direct_cost = min_directRoutes(shipping_dict,source,destiation)
    one_hop = min_oneHopeRoutes(shipping_dict,source,destiation)
    if direct_cost  == one_hop == -1:
        return -1
    elif direct_cost > -1 and one_hop > -1:
        return min(direct_cost,one_hop)
    else:
        return direct_cost if direct_cost > -1 else one_hop

shipping_data_string ="A,B,Expensive,999999:A,C,Mid,500000:C,B,Mid2,499999"
source = "A"
destination = "B"
res = minimumshipping(shipping_data_string,source,destination)
print(res)
print("Finished")
