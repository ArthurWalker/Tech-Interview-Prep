import string
import re


from typing import List
def stopword_stripper(text, stopwords: List[str]) -> str:
    lst_words = text.split()
    res = []
    for word in lst_words:
        lower_word = word.lower()
        new_word = ''
        for letter in lower_word:
            if (letter.isalpha() == True):
                new_word+=letter
        # new_word =  re.sub(string.punctuation,'',lower_word)

        if new_word not in stopwords:
            res.append(lower_word)

    return ' '.join(res)


text = "Hello, world! How are y?ou"
stopwords =  ["how", "are", "you"]
res = stopword_stripper(text,stopwords)
print(res)


