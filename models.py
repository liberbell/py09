from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

with open('Course-Classification.txt', 'r') as fh:
    classifications = fh.read().splitlines()

lemmatizer = WordNetLemmatizer()

def customtokenize(str):
    tokens = nltk.word_tokenize(str)
    nostop = list(filter(lambda token: token not in stopwords.words('english'), tokens))
    lemmatized = [lemmatizer.lemmatize(word) for word in nostop ]
    return lemmatized

vectorizer = TfidfVectorizer(tokenizer = customtokenize)
tfidf = vectorizer.fit_transform(descriptions)

le = preprocessing.LabelEncoder()
le.fit(classifications)
print('Classes found: ', le.classes_)

int_classes = le.transform(classifications)
print('\nClasses converted to integers: ', int_classes)

xtrain, xtest, ytrain, ytest = train_test_split(tfidf, int_classes, random_state=0)
