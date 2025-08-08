from MinimumPenalty import earlier_minimum_penalty

def test_bestClosingTime():
    test_cases = [
        # Example cases
        {
            "customers": "YYNY",
            "expected": 2
        },
        {
            "customers": "NNNNN",
            "expected": 0
        },
        {
            "customers": "YYYY",
            "expected": 4
        },

        # Single-character cases
        {
            "customers": "N",
            "expected": 0  # Closing immediately avoids penalties
        },
        {
            "customers": "Y",
            "expected": 1  # Must stay open until hour 1
        },

        # Mixed cases
        {
            "customers": "NYNY",
            "expected": 1
        },
        {
            "customers": "YNNYNN",
            "expected": 1
        },
        {
            "customers": "NNYNNY",
            "expected": 2
        },

        # Long sequences of Y then N
        {
            "customers": "YYYYNNNN",
            "expected": 4
        },
        {
            "customers": "NNNNYYYY",
            "expected": 4
        },

        # All N except one Y in middle
        {
            "customers": "NNNYNN",
            "expected": 3
        },

        # Tie-breaking earliest case
        {
            "customers": "YNYN",
            "expected": 1  # Same penalty at 1 and 3, choose earliest
        }
    ]

    for i, case in enumerate(test_cases, 1):
        result = earlier_minimum_penalty(case["customers"])
        assert result == case["expected"], f"Test case {i} failed: got {result}, expected {case['expected']}"

    print("All test cases passed!")

test_bestClosingTime()