import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

hashtags_df = pd.read_csv('Course-Hashtags.csv')
print('Sample Hashtag Data: ')
print(hashtags_df[:2])

hash_list = hashtags_df['HashTags'].tolist()
title_list = hashtags_df['Course'].tolist()

vectorizer = TfidfVectorizer(stop_words='english')
hash_matrix = vectorizer.fit_transform(hash_list)

print('\n Feature names Identified: \n')
print(vectorizer.get_feature_names())

kmeans = KMeans(n_clusters=3).fit(hash_matrix)
clusters = kmeans.labels_

for group in set(clusters):
    print('\nGroup: ', group, '\n--------------')

    for i in hashtags_df.index:
        if (clusters[i] == group)
