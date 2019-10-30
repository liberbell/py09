import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

with open('Course-Descriptions.txt', 'r') as fh:
    descriptions = fh.read().splitlines()
print('Sample course descriptions: ', descriptions[:2])

# nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
