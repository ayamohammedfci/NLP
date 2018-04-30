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

#Assigning a score to every sentence

# Secondly, we will need a dictionary to keep the score of each sentence, this way we can later go through the dictionary to generate the summary.

sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
    print (sentence.lower())
    for wordValue in freqTable:
        if wordValue[0] in sentence.lower():
            #Note: Index 0 of wordValue will return the word itself. Index 1 the number of instances.
            print (wordValue[0])
            if sentence[:12] in sentenceValue:
                sentenceValue[sentence[:12]] += wordValue[1]
            else:
                sentenceValue[sentence[:12]] = wordValue[1]

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

# Average value of a sentence from original text
average = int(sumValues/ len(sentenceValue))
summary = ''

#apply our threshold and store our sentences in order into our summary.
for sentence in sentences:
        if sentence[:12] in sentenceValue and sentenceValue[sentence[:12]] > (1.5 * average):
            summary +=  " " + sentence
