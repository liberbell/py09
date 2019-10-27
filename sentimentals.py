

with open('Movie-Reviews.txt', 'r') as fh:
    reviews = fh.readlines()
print(reviews[:2])
