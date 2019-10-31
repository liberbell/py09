from sklearn import preprocessing

with open('Course-Classification.txt', 'r') as fh:
    classifications = fh.read().splitlines()

le = preprocessing.LabelEncoder()
le.fit(classifications)
print('Classes found: ', le.classes_)

int_classes = le.transform(classifications)
print('\nClasses converted to integers: ', int_classes)
