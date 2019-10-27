from wordcloud import WordCloud, STOPWORD
with open('Course-Descriptions.txt', 'r') as fh:
    filedata = fh.read()

print('File data sample: ', filedata[:200])

stopwords = set(STOPWORDS)
