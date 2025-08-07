from CustomStringSorting import customStringSort
def test_string_sorting():
    """
    Test cases for sorting strings with format <letters><number>
    Rules:
    1. Sort by alphabetical order of letter part
    2. If same letters, sort by numeric part in descending order
    """

    test_cases = [
        # Test Case 1: Basic example from problem description
        {
            "input": ["a3", "a22", "b1", "b11", "a5"],
            "expected": ["a22", "a5", "a3", "b11", "b1"],
            "description": "Basic mixed groups with numeric sorting"
        },

        # Test Case 2: Multi-letter strings from problem description
        {
            "input": ["cat20", "dog5", "cat3", "apple100", "apple11"],
            "expected": ["apple100", "apple11", "cat20", "cat3", "dog5"],
            "description": "Multi-letter strings with numeric sorting"
        },

        # Test Case 3: Single characters with two-digit numbers
        {
            "input": ["z9", "z10", "y1"],
            "expected": ["y1", "z10", "z9"],
            "description": "Single chars, testing 10 > 9 numerically"
        },

        # Test Case 4: All same letters, different numbers
        {
            "input": ["x1", "x100", "x2", "x20", "x3"],
            "expected": ["x100", "x20", "x3", "x2", "x1"],
            "description": "Same letters, pure numeric descending sort"
        },

        # Test Case 5: All different letters, same number
        {
            "input": ["z5", "a5", "m5", "b5"],
            "expected": ["a5", "b5", "m5", "z5"],
            "description": "Different letters, same number - alphabetical sort"
        },

        # Test Case 6: Single element array
        {
            "input": ["hello123"],
            "expected": ["hello123"],
            "description": "Single element array"
        },

        # Test Case 7: Large numbers with leading zeros consideration
        {
            "input": [ "test7", "test70", "test100"],
            "expected": ["test100", "test70", "test7"],
            "description": "Testing numeric parsing (007 = 7, not string comparison)"
        },

        # Test Case 8: Complex multi-letter patterns
        {
            "input": ["abc999", "ab1000", "abc1", "ab500", "abcd50"],
            "expected": ["ab1000", "ab500", "abc999", "abc1", "abcd50"],
            "description": "Complex letter patterns: ab, abc, abcd groups"
        },

        # Test Case 9: Edge case with very large numbers
        {
            "input": ["a9999999999", "a1", "b2", "a123456"],
            "expected": ["a9999999999", "a123456", "a1", "b2"],
            "description": "Very large numbers testing numeric sort"
        },

        # Test Case 10: Mixed single and multi-letter with zero
        {
            "input": ["a0", "aa0", "a10", "aa1", "b0"],
            "expected": ["a10", "a0", "aa1", "aa0", "b0"],
            "description": "Testing with zeros and single vs multi-letter edge cases"
        }
    ]
    for i, case in enumerate(test_cases, 1):
        result = customStringSort(case["input"])
        assert result == case["expected"], f"Test case {i} failed: got {result}, expected {case['expected']}"

    print("All test cases passed!")


# Example call (uncomment to run when function is defined)
test_string_sorting()

