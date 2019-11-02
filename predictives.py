import os
import nltk

base_file = open('Course-Descriptions.txt', 'rt')
raw_text = base_file.read()
base_file.close()
print('Text read from file: ', raw_text[:200])

token_list = nltk.word_tokenize(raw_text)
token_list2 = [word_replace('`', '') for word in token_list]
