import nltk
from nltk.corpus import stopwords

with open('Course-Descriptions.txt', 'r') as fh:
    descriptions = fh.read().splitlines()
print('Sample course descriptions: ', descriptions[:2])

nttk.download('stopwords')
