import pandas as pd

hashtags_df = pd.read_csv('Course-Hashtags.csv')
print('Sample Hashtag Data: ')
print(hashtags_df[:2])

hash_list = hashtags_df['HashTags'].tolist()
title_list = hashtags_df['Course'].tolist()
