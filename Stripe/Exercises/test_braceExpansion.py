from BraceExpansion import brace_expansion

def test_expand():
    test_cases = [
        # Example 1
        {
            "input": "{a,b}c{d,e}f",
            "expected": ["acdf", "acef", "bcdf", "bcef"]
        },
        # Example 2: no braces
        {
            "input": "abcd",
            "expected": ["abcd"]
        },
        # Single group at start
        {
            "input": "{x,y,z}123",
            "expected": ["x123", "y123", "z123"]
        },
        # Single group at end
        {
            "input": "abc{d,e,f}",
            "expected": ["abcd", "abce", "abcf"]
        },
        # Only one brace group
        {
            "input": "{a,b,c}",
            "expected": ["a", "b", "c"]
        },
        # Multiple single-letter options
        {
            "input": "{a,b}{c,d}{e,f}",
            "expected": ["ace", "acf", "ade", "adf", "bce", "bcf", "bde", "bdf"]
        },
        # Repeating characters in output
        {
            "input": "{a}a{b}",
            "expected": ["aab"]
        },
        # Long non-brace prefix/suffix
        {
            "input": "start{a,b}end",
            "expected": ["startaend", "startbend"]
        },
        # Mixed fixed and options
        {
            "input": "a{b,c}d{e,f}g",
            "expected": ["abdeg", "abdfg", "acdeg", "acdfg"]
        },
        # Already sorted order
        {
            "input": "{a,b}x{c,d}",
            "expected": ["axc", "axd", "bxc", "bxd"]
        },
        # Out of order in input, should sort options
        {
            "input": "{c,a,b}x{e,d}",
            "expected": ["axd", "axe", "bxd", "bxe", "cxd", "cxe"]
        },
        # Only braces, unordered options
        {
            "input": "{z,y,x}",
            "expected": ["x", "y", "z"]
        }
    ]

    for i, case in enumerate(test_cases, 1):
        result = brace_expansion(case["input"])
        assert result == case["expected"], f"Test case {i} failed: got {result}, expected {case['expected']}"

    print("All test cases passed!")

# Example call (uncomment to run when function is defined)
test_expand()
