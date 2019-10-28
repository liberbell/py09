from textblob import TextBlob

with open('Movie-Reviews.txt', 'r') as fh:
    reviews = fh.readlines()
# print(reviews[:2])

for review in reviews:
    sentiment = TextBlob(review)
    print('{:40} : {: 01.2f} : {:01.2f}'.format(review[:40], sentiment.polarity, sentiment.subjectivity))

labels = ['Negative', 'Neautral', 'Positive']
vales = [0, 0, 0]

for review in reviews:
    sentiment = TextBlob(review)
    polarity = round(( sentiment.polarity + 1) * 3) % 3

    values[polarity] = values[polarity] + 1

print('Final summarized count: ', values)
