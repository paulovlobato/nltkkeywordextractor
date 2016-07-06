## This script extracts metadata from text files
### Written by Victor

from sys import argv
import nltk

# nltk.download('punkt')

# load text file
script, filename = argv
txt = open(filename)

#nltk.download('all')

with open(filename) as textfile:
        textContent=textfile.read()

tokens = nltk.word_tokenize(textContent)
print tokens

tagged = nltk.pos_tag(tokens)
print tagged[0:6]

entities = nltk.chunk.ne_chunk(tagged)
print entities

# output
txtOut = open(filename + "Md", "w")
txtOut.write(str(entities))
txtOut.close()

# from nltk.corpus import treebank
# t = treebank.parsed_sents('wsj_0001.mrg')[0]
# t.draw()
