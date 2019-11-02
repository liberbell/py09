import os
import nltk

base_file = open('Course-Descriptions.txt', 'rt')
raw_text = base_file.read()
base_file.close()
print('Text read from file: ', raw_text[:200])
