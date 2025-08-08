from MinimumShippingCost import minimumshipping

def test_minimum():
    test_cases  = [
    # Test Case 1: Basic direct route wins over one-hop
    {
        "shipping_data_string": "US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7:US,UK,RoyalMail,12",
        "source": "US",
        "destination": "UK",
        "expected": 5,
        "description": "Direct route cheaper than one-hop route"
    },

    # Test Case 2: One-hop route wins over direct
    {
        "shipping_data_string": "US,FR,AirCargo,20:US,CA,FedEx,3:CA,FR,DHL,15",
        "source": "US",
        "destination": "FR",
        "expected": 18,
        "description": "One-hop route cheaper than direct route"
    },

    # Test Case 3: No path exists
    {
        "shipping_data_string": "US,CA,FedEx,3:UK,FR,DHL,7",
        "source": "US",
        "destination": "DE",
        "expected": -1,
        "description": "No direct or one-hop path available"
    },

    # Test Case 4: Multiple one-hop routes, choose cheapest
    {
        "shipping_data_string": "A,B,C1,10:B,D,C2,5:A,E,C3,4:E,D,C4,12",
        "source": "A",
        "destination": "D",
        "expected": 15,
        "description": "Multiple one-hop paths, choose minimum cost"
    },

    # Test Case 5: Only direct route available
    {
        "shipping_data_string": "NY,LA,Express,100:SF,CHI,Fast,50",
        "source": "NY",
        "destination": "LA",
        "expected": 100,
        "description": "Only direct route exists, no alternatives"
    },

    # Test Case 6: Only one-hop route available
    {
        "shipping_data_string": "A,B,Carrier1,25:B,C,Carrier2,30",
        "source": "A",
        "destination": "C",
        "expected": 55,
        "description": "No direct route, only one-hop path"
    },

    # Test Case 7: Multiple carriers for same route, choose cheapest direct
    {
        "shipping_data_string": "X,Y,Expensive,100:X,Y,Cheap,10:X,Y,Medium,50:X,Z,Alt,20:Z,Y,Alt2,15",
        "source": "X",
        "destination": "Y",
        "expected": 10,
        "description": "Multiple direct carriers, choose cheapest direct over one-hop"
    },

    # Test Case 8: Complex network with multiple intermediate options
    {
        "shipping_data_string": "A,B,C1,5:A,C,C2,8:A,D,C3,12:B,E,C4,3:C,E,C5,7:D,E,C6,2",
        "source": "A",
        "destination": "E",
        "expected": 8,
        "description": "Multiple one-hop paths through different intermediates"
    },

    # Test Case 9: Same source and destination
    {
        "shipping_data_string": "A,B,Carrier,10:B,C,Carrier2,5",
        "source": "A",
        "destination": "A",
        "expected": 0,
        "description": "Source equals destination, should return 0"
    },

    # Test Case 10: Tie between direct and one-hop costs
    {
        "shipping_data_string": "P,Q,Direct,20:P,R,Hop1,12:R,Q,Hop2,8",
        "source": "P",
        "destination": "Q",
        "expected": 20,
        "description": "Direct and one-hop have same cost, should return either"
    },

    # Edge Case 1: Empty shipping data
    {
        "shipping_data_string": "",
        "source": "A",
        "destination": "B",
        "expected": -1,
        "description": "Empty shipping data string"
    },

    # Edge Case 2: Single route entry
    {
        "shipping_data_string": "A,B,OnlyCarrier,15",
        "source": "A",
        "destination": "B",
        "expected": 15,
        "description": "Only one route in entire data"
    },

    # Edge Case 3: Very high costs (floating point precision)
    {
        "shipping_data_string": "A,B,Expensive,999999:A,C,Mid,500000:C,B,Mid2,499999",
        "source": "A",
        "destination": "B",
        "expected": 999999,
        "description": "Large cost values, one-hop slightly cheaper"
    },

    # Edge Case 4: Zero cost routes
    {
        "shipping_data_string": "A,B,Free,0:A,C,Paid,10:C,B,Free2,0",
        "source": "A",
        "destination": "B",
        "expected": 0,
        "description": "Zero cost direct route available"
    },

    # Edge Case 5: Circular references but no valid path
    {
        "shipping_data_string": "A,B,C1,5:B,A,C2,3:C,D,C3,10",
        "source": "A",
        "destination": "D",
        "expected": -1,
        "description": "Circular routes exist but no path to destination"
    },

    # Edge Case 6: Case sensitivity test
    {
        "shipping_data_string": "us,UK,Carrier1,10:US,uk,Carrier2,15",
        "source": "US",
        "destination": "UK",
        "expected": -1,  # Assuming case-sensitive matching
        "description": "Case sensitivity in location names"
    },

    # Edge Case 7: Very long location names
    {
        "shipping_data_string": "VeryLongSourceLocationName,VeryLongDestinationLocationName,Carrier,25:VeryLongSourceLocationName,IntermediateLocation,Carrier2,10:IntermediateLocation,VeryLongDestinationLocationName,Carrier3,12",
        "source": "VeryLongSourceLocationName",
        "destination": "VeryLongDestinationLocationName",
        "expected": 22,
        "description": "Long location names, one-hop cheaper"
    }
]

    for i,v in enumerate(test_cases):
        result = minimumshipping(v["shipping_data_string"],v["source"],v["destination"])
        assert result == v["expected"], f"Test case {i+1} failed: got {result}, expected {v['expected']}"

    print("Passed all test")

test_minimum()