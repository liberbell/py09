from textblob import TextBlob

with open('Movie-Reviews.txt', 'r') as fh:
    reviews = fh.readlines()
print(reviews[:2])

for review in reviews:
    sentiment = TextBlob(review)
    print('{:40} : {: 01.2f} : {:01.2f}'.format(review[:40]), sentiment.polarity, sentiment.subjectivity)
