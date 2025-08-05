from typing import List

def accept_langage(acceptLanguageHeader: str, supportedLanguages: List[str]) -> List[str]:

    # Formet acceptLanguageHeader -> List[str]
    formatedAccept = acceptLanguageHeader.split(',')

    # dictionary supportedLanauges
    dict_supported = set(supportedLanguages)

    res = [word.strip() for word in formatedAccept if word.strip() in dict_supported]
    return res

result = accept_langage("en-US, fr-CA, fr-FR",supportedLanguages = ["fr-FR", "en-US"])
print(result)