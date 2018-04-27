from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))

file=open('data.txt','rU')
text=file.read()
words = word_tokenize(text)

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

print(freqTable)
