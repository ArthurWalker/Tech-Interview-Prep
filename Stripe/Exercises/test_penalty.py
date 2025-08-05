
from penaltyshop import penatly_shop

def test_shop_closing():
    test_cases = [

        # Test Case 1: Basic example with mixed pattern
        {
            "input": "YYNY",
            "expected": 2,
            "description": "Mixed pattern - optimal to close at hour 2"
        },

        # Test Case 2: All customers come
        {
            "input": "YYYY",
            "expected": 4,
            "description": "All hours have customers - keep open all day"
        },

        # Test Case 3: No customers at all
        {
            "input": "NNNN",
            "expected": 0,
            "description": "No customers ever - close immediately"
        },

        # Test Case 4: Single character - customer comes
        {
            "input": "Y",
            "expected": 1,
            "description": "Single hour with customer - stay open"
        },

        # Test Case 5: Single character - no customer
        {
            "input": "N",
            "expected": 0,
            "description": "Single hour with no customer - close immediately"
        },

        # Test Case 6: Customers only at the beginning
        {
            "input": "YYNNNN",
            "expected": 2,
            "description": "Customers early, then none - close after customers leave"
        },

        # Test Case 7: Customers only at the end
        {
            "input": "NNNYYYY",
            "expected": 7,
            "description": "No customers early, then many - close before they arrive"
        },

        # Test Case 8: Alternating pattern
        {
            "input": "YNYNYN",
            "expected": 1,
            "description": "Alternating pattern - best to stay open (tie-breaking chooses later)"
        },

        # Test Case 9: Longer sequence with clear optimal point
        {
            "input": "YYYNNNNYYY",
            "expected": 3,
            "description": "Clear gap in middle - optimal to close during gap"
        },

        # Test Case 10: Edge case - empty string
        {
            "input": "",
            "expected": 0,
            "description": "Empty string - close at hour 0 (no hours to consider)"
        }
    ]

    for i, case in enumerate(test_cases):
        result = penatly_shop(case['input'])
        assert result == case["expected"], f"Test case {i+1} failed: got '{result}', expected '{case['expected']}'"

    print("All test cases passed!")


test_shop_closing()