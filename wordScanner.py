## This script extracts metadata from text files
### Written by Victor

from sys import argv
import nltk

# nltk.download('punkt')

# load text file
script, filename = argv
txt = open(filename)

tokens = nltk.word_tokenize(filename)
tokens=('A', 'eight', 'on', 'Thursday', 'morning', 'Arthur', 'did', 'feel', 'very', 'good')

tagged = nltk.pos_tag(tokens)
tagged[0:6]
[('At', 'IN'), ('eight', 'CD'), ("o'clock", 'JJ'), ('on', 'IN'),
('Thursday', 'NNP'), ('morning', 'NN')]

entities = nltk.chunk.ne_chunk(tagged)
entities
Tree('S', [('At', 'IN'), ('eight', 'CD'), ("o'clock", 'JJ'),
           ('on', 'IN'), ('Thursday', 'NNP'), ('morning', 'NN'),
       Tree('PERSON', [('Arthur', 'NNP')]),
           ('did', 'VBD'), ("n't", 'RB'), ('feel', 'VB'),
           ('very', 'RB'), ('good', 'JJ'), ('.', '.')])

from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
