# Batch Translation v1.0
# Author: Mahmood Moghimi
# This is a simple code to retrieve related information such as definition, translation, synonyms and, antonyms for given words list.
# I assumed the source language is English and the target is Persian.
# Change source and target languages as you like.

import nltk
from nltk.corpus import wordnet
from deep_translator import GoogleTranslator
import csv 

header = ['word', 'definition', 'translation', 'synonyms', 'antonyms', 'examples']
data = []

print("Processing words...")
count = sum(1 for line in open('words.txt'))
with open('words.csv', 'w', encoding='utf-8', newline='') as w:
    writer = csv.writer(w, delimiter=',')
    writer.writerow(header)
    with open('words.txt') as f:
        line = f.readline().strip()
        c = 0
        while line:
            word = line
            c += 1
            print("%d/%d " % (c, count))
            translate = GoogleTranslator(source='en', target='fa').translate(word)
            synonyms = []
            antonyms = []
            examples = []
            definition = []
            syns = wordnet.synsets(word)
            for syn in syns:
                for lm in syn.lemmas():
                    synonyms.append(lm.name())
                    if lm.antonyms():
                        antonyms.append(lm.antonyms()[0].name())
                examples.append('_'.join(syn.examples()))
                definition.append(syn.definition())
            line = f.readline().strip()
            examples = ('\n'.join(examples)).replace("_", "\n")
            examples = '\n'.join([s for s in examples.splitlines() if s])
            data = [word, '\n'.join(set(definition)), translate, ' / '.join(set(synonyms)), ' / '.join(set(antonyms)), examples]
            writer.writerow(data)

            
            
