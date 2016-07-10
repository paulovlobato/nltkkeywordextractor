## This script extracts metadata from text files
### Written by Victor

from sys import argv
import nltk
from nltk.corpus import stopwords

# nltk.download('punkt')

# load text file
script, filename = argv
txt = open(filename)

#nltk.download('all')

with open(filename) as textfile:
        textContent=textfile.read()

tokens = nltk.word_tokenize(textContent)

stopwords = stopwords.words('english')
filteredWords = [token for token in tokens if token not in stopwords]

print tokens
print filteredWords
