import os
import nltk

base_file = open('Course-Descriptions.txt', 'rt')
raw_text = base_file.read()
base_file.close()
print('Text read from file: ', raw_text[:200])

token_list = nltk.word_tokenize(raw_text)
token_list2 = [word.replace('`', '') for word in token_list]
token_list3 = list(filter(lambda token: nltk.tokenize.punkt.PunktToken(token).is_non_punct, token_list2))