import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

hashtags_df = pd.read_csv('Course-Hashtags.csv')
print('Sample Hashtag Data: ')
print(hashtags_df[:2])

hash_list = hashtags_df['HashTags'].tolist()
title_list = hashtags_df['Course'].tolist()

vectorizer = TfidfVectorizer(stop_words='english')
hash_matrix = vectorizer.fit_transform(hash_list)

print('n\ Feature names Identified: \n')
print(vectorizer.get_feature_names())
