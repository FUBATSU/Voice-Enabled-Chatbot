import requests
import json
from collections import namedtuple
import urllib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


def filter_sentence(text):
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if w not in stop_words]
    ans = ""
    for x in filtered_sentence:
        ans = ans + x + " "
    return ans

