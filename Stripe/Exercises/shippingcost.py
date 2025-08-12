# For some items, shipping the first item is more expensive than shipping additional items. Update the shipping matrix to reflect quantity based discounts.

# The order remains unchanged and the shipping cost matrix has been updated like the following:

# Order:
# {
#     "country": "US", // or "CA" for the CA order
#     "items": [
#         {"product": "mouse", "quantity": 20},
#         {"product": "laptop", "quantity": 5}
#     ]
# }

# Shipping Cost:

# Each country/product has its own shipping cost tiers:

# {
#     "US": [
#         {
#             "product": "mouse",
#             "costs": [
#                 {
#                     "minQuantity": 0,
#                     "maxQuantity": null,
#                     "cost": 550
#                 }
#             ]
#         },
#         {
#             "product": "laptop",
#             "costs": [
#                 {
#                     "minQuantity": 0,
#                     "maxQuantity": 2,
#                     "cost": 1000
#                 },
#                 {
#                     "minQuantity": 3,
#                     "maxQuantity": 4,
#                     "cost": 950
#                 },
#                 {
#                     "minQuantity": 5,
#                     "maxQuantity": null,
#                     "cost": 900
#                 }
#             ]
#         }
#     ],
#     "CA": [
#         {
#             "product": "mouse",
#             "costs": [
#                 {
#                     "minQuantity": 0,
#                     "maxQuantity": null,
#                     "cost": 750
#                 }
#             ]
#         },
#         {
#             "product": "laptop",
#             "costs": [
#                 {
#                     "minQuantity": 0,
#                     "maxQuantity": 2,
#                     "cost": 1100
#                 },
#                 {
#                     "minQuantity": 3,
#                     "maxQuantity": null,
#                     "cost": 1000
#                 }
#             ]
#         }
#     ]
# }

# Update the function calculate_shipping_cost to now calculate shipping based upon the tiered discount.

# Examples:

# calculate_shipping_cost(order_us, shipping_cost) == 15800 // 20 * 550 + 2 * 1000 + 2 * 950 + 1 * 900 = 15800
# calculate_shipping_cost(order_ca, shipping_cost) == 20200 // 20 * 750 + 2 * 1100 + 3 * 1000 = 20200
# Enter your code here. Read input from STDIN. Print output to STDOUT

def calculate_shipping_cost(order_us,shipping_cost):
    shipping_country = order_us['country']
    order_items = order_us['items']
    if shipping_country in shipping_cost:
        price  = 0
        for item in order_items:
            price_lst = []
            product = item['product']
            quantity = item['quantity']
            for prodcut_cost in shipping_cost[shipping_country]:
                if prodcut_cost['product'] == product:
                    price_lst.append(prodcut_cost['costs'])

            remain_quanty = quantity
            price_tier = 0
            while remain_quanty > 0 :
                ship_detail = price_lst[0][price_tier]
                max_quantity = ship_detail['maxQuantity']
                cost = ship_detail['cost']
                if max_quantity is not None:
                    price+= max_quantity*cost
                    remain_quanty = remain_quanty-max_quantity
                    price_tier+=1
                else:
                    price+= remain_quanty*cost
                    remain_quanty = remain_quanty-remain_quanty
        return price
    return 0

order_us = {
    "country": "CA",
    "items": [
        {"product": "mouse", "quantity": 20},
        {"product": "laptop", "quantity": 7}
    ]
}
shipping_cost = {
    "US": [
        {
            "product": "mouse",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": None,
                    "cost": 550
                }
            ]
        },
        {
            "product": "laptop",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": 2,
                    "cost": 1000
                },
                {
                    "minQuantity": 3,
                    "maxQuantity": 4,
                    "cost": 950
                },
                {
                    "minQuantity": 5,
                    "maxQuantity": None,
                    "cost": 900
                }
            ]
        }
    ],
    "CA": [
        {
            "product": "mouse",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": None,
                    "cost": 750
                }
            ]
        },
        {
            "product": "laptop",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": 2,
                    "cost": 1100
                },
                {
                    "minQuantity": 3,
                    "maxQuantity": None,
                    "cost": 1000
                }
            ]
        }
    ]
}


res = calculate_shipping_cost(order_us,shipping_cost)
print(res)