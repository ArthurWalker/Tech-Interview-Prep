from AcceptLanguageMatching import accept_langage
def test_get_acceptable_languages():
    test_cases = [
        # Example 1: Typical case with two matches
        {
            "acceptLanguageHeader": "en-US, fr-CA, fr-FR",
            "supportedLanguages": ["fr-FR", "en-US"],
            "expected": ["en-US", "fr-FR"]
        },
        # Example 2: One match at the end
        {
            "acceptLanguageHeader": "fr-CA, fr-FR",
            "supportedLanguages": ["en-US", "fr-FR"],
            "expected": ["fr-FR"]
        },
        # Example 3: Exact match
        {
            "acceptLanguageHeader": "en-US",
            "supportedLanguages": ["en-US", "fr-CA"],
            "expected": ["en-US"]
        },
        # Example 4: No matches
        {
            "acceptLanguageHeader": "es-MX, de-DE",
            "supportedLanguages": ["en-US", "fr-FR"],
            "expected": []
        },
        # Example 5: Empty header
        {
            "acceptLanguageHeader": "",
            "supportedLanguages": ["en-US", "fr-FR"],
            "expected": []
        },
        # Example 6: Empty supported set
        {
            "acceptLanguageHeader": "en-US, fr-CA",
            "supportedLanguages": [],
            "expected": []
        },
        # Extra: Handles extra whitespace
        {
            "acceptLanguageHeader": " en-US ,  fr-CA ,fr-FR ",
            "supportedLanguages": ["fr-CA", "fr-FR"],
            "expected": ["fr-CA", "fr-FR"]
        },
        # # Extra: Case sensitivity
        # {
        #     "acceptLanguageHeader": "en-us, fr-ca",
        #     "supportedLanguages": ["en-US", "fr-ca"],
        #     "expected": ["fr-ca"]
        # },
        # Extra: All match
        {
            "acceptLanguageHeader": "en-US, fr-CA, es-MX",
            "supportedLanguages": ["en-US", "fr-CA", "es-MX"],
            "expected": ["en-US", "fr-CA", "es-MX"]
        },
        # # Extra: Duplicates in header (should preserve order and not deduplicate)
        # {
        #     "acceptLanguageHeader": "en-US, en-US, fr-FR",
        #     "supportedLanguages": ["en-US", "fr-FR"],
        #     "expected": ["en-US", "fr-FR"]
        # },
    ]

    for i, case in enumerate(test_cases, 1):
        result = accept_langage(case["acceptLanguageHeader"], case["supportedLanguages"])
        assert result == case["expected"], f"Test case {i} failed: got {result}, expected {case['expected']}"

    print("All test cases passed!")

# Example call (uncomment to run when function is defined)
test_get_acceptable_languages()
