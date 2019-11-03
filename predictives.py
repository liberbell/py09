import os
import nltk
from nltk.util import ngrams
import sqlite3

base_file = open('Course-Descriptions.txt', 'rt')
raw_text = base_file.read()
base_file.close()
print('Text read from file: ', raw_text[:200])

token_list = nltk.word_tokenize(raw_text)
token_list2 = [word.replace('`', '') for word in token_list]
token_list3 = list(filter(lambda token: nltk.tokenize.punkt.PunktToken(token).is_non_punct, token_list2))
token_list4 = [word.lower() for word in token_list3 ]

print('\nSample token list: ', token_list4[:10])
print('\nTotal tokens: ', len(token_list4))


conn = sqlite3.connect(':memory:')
conn.execute('''DROP TABLE IF EXISTS NGRAMS''')
conn.execute('''CREATE TABLE GRAMS
        (FIRST TEXT NOT NULL,
        SECOND TEXT NOT NULL,
        COUNTS INT NOT NULL,
        CONSTRAINT PK_GRAMS PRIMARY (FIRST, SECOND));''')

bigrams = ngrams(token_list4, 2)
for i in bigrams:
    insert_str = "INSERT INTO NGRAMS (FIRST, SECOND, COUNTS)
    VALUES ('" + i[0] + "','" + i[1] + "', 1 )
    ON CONFLICT(FIRST, SECOND) DO UPDATE SET COUNTS=COUNTS + 1"
    conn.execute(insert_str);
