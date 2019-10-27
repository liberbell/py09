from wordcloud import WordCloud, STOPWORDS

with open('Course-Descriptions.txt', 'r') as fh:
    filedata = fh.read()

print('File data sample: ', filedata[:200])

stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, max_words=25, backgroudcolor='white').generate(filedata)
