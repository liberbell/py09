from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.native_bayes import MultinomialNB

with open('Course-Classification.txt', 'r') as fh:
    classifications = fh.read().splitlines()

le = preprocessing.LabelEncoder()
le.fit(classifications)
print('Classes found: ', le.classes_)

int_classes = le.transform(classifications)
print('\nClasses converted to integers: ', int_classes)
