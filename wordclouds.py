from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as mpLib

with open('Course-Descriptions.txt', 'r') as fh:
    filedata = fh.read()

print('File data sample: ', filedata[:200])

stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, max_words=25, background_color='white').generate(filedata)

# mpLib.imshow(wordcloud)
# mpLib.axis('off')
# mpLib.show()

stopwords.update(['many', 'using', 'want', 'value'])
wordcloud = WordCloud(stopwords=stopwords, max_words=10, background_color='azure').generate(filedata)

mpLib.imshow(wordcloud)
mpLib.axis('off')
mpLib.show()
