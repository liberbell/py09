from sklearn import preprocessing

with open('Course-Classification.txt', 'r') as fh:
    classifications = fh.read().splitlines()

le = preprocessing.LabelEncoder()
le.fit(classifications)
print('Classes found: ', le.classes_)
