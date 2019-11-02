import os
import nltk
from nltk.util import ngrams
import sqlite3

base_file = open('Course-Descriptions.txt', 'rt')
raw_text = base_file.read()
base_file.close()
print('Text read from file: ', raw_text[:200])

token_list = nltk.word_tokenize(raw_text)
token_list2 = [word.replace('`', '') for word in token_list]
token_list3 = list(filter(lambda token: nltk.tokenize.punkt.PunktToken(token).is_non_punct, token_list2))
token_list4 = [word.lower() for word in token_list3 ]

print('\nSample token list: ', token_list4[:3])
print('\nTotal tokens: ', len(token_list4))
conn = sqlite3.connect('memory')
