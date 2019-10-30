import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

with open('Course-Descriptions.txt', 'r') as fh:
    descriptions = fh.read().splitlines()
print('Sample course descriptions: ', descriptions[:2])

# nltk.download('stopwords')
# nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def customtokenize(str):
    tokens = nltk.word_tokenize(str)
    nostop = list(filter(lambda token: token not in stopwords.words('english'), tokens))
    lemmatized = [lemmatizer.lemmatize(word) for word in nostop ]
    return lemmatized

vectorizer = TfidfVectorizer(tokenizer = customtokenize)
tfidf = vectorizer.fit_transform(descriptions)

print('\n Sample feature name Identified: ', vectorizer.get_feature_names()[:25])
