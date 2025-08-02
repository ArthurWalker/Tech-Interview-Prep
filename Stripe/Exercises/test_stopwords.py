from StopwordsStripper import stopword_stripper
def test_remove_stopwords():
    test_cases = [
        # Basic example
        {
            "text": "This is an example sentence with some common words.",
            "stopwords": ["is", "an", "some"],
            "expected": "this example sentence with common words."
        },
        # Case-insensitive stopwords
        {
            "text": "The quick brown fox jumps over the lazy dog.",
            "stopwords": ["the", "over"],
            "expected": "quick brown fox jumps lazy dog."
        },
        # Stopwords with punctuation kept
        {
            "text": "Hello, world! How are you?",
            "stopwords": ["how", "are", "you"],
            "expected": "hello, world!"
        },
        # Empty stopwords list
        {
            "text": "Nothing should be removed here.",
            "stopwords": [],
            "expected": "nothing should be removed here."
        },
        # All words are stopwords
        {
            "text": "Stop me if you can.",
            "stopwords": ["stop", "me", "if", "you", "can"],
            "expected": ""
        },
        # Repeated stopwords
        {
            "text": "Is this the real life? Is this just fantasy?",
            "stopwords": ["is", "this"],
            "expected": "the real life? just fantasy?"
        },
        # Punctuation in stopwords
        {
            "text": "Wait... what?! Seriously?",
            "stopwords": ["what?!"],
            "expected": "wait... seriously?"
        },
        # Leading/trailing/multiple spaces
        {
            "text": "   A  very   spaced    out    sentence   ",
            "stopwords": ["a", "out"],
            "expected": "very spaced sentence"
        },
        # Stopwords with capital letters in text
        {
            "text": "Python Is Awesome And So Are You",
            "stopwords": ["is", "and", "are", "you"],
            "expected": "python awesome so"
        },
        # Edge case: single word
        {
            "text": "Only",
            "stopwords": ["only"],
            "expected": ""
        }
    ]

    for i, case in enumerate(test_cases, 1):
        result = stopword_stripper(case["text"], case["stopwords"])
        assert result == case["expected"], f"Test case {i} failed: got '{result}', expected '{case['expected']}'"

    print("All test cases passed!")

test_remove_stopwords()
# Example call (uncomment to run when function is defined)
# test_remove_stopwords()
