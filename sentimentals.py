from textblob import TextBlob
import matplotlib.pyplot as plt

with open('Movie-Reviews.txt', 'r') as fh:
    reviews = fh.readlines()
# print(reviews[:2])

for review in reviews:
    sentiment = TextBlob(review)
    print('{:40} : {: 01.2f} : {:01.2f}'.format(review[:40], sentiment.polarity, sentiment.subjectivity))

labels = ['Negative', 'Neautral', 'Positive']
values = [0, 0, 0]

for review in reviews:
    sentiment = TextBlob(review)
    polarity = round(( sentiment.polarity + 1) * 3) % 3

    values[polarity] = values[polarity] + 1

print('Final summarized count: ', values)

colors = ['Green', 'Blue', 'Red']
print('\n Pie Representation \n ------------')

plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
