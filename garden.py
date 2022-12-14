# -*- coding: utf-8 -*-
"""garden

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kr3npCkgxMLxXI8srgJHcxFRDvdcCB_D
"""

import spacy
nlp = spacy.load('en_core_web_sm')


# === Your task ===
#	Let's have some 'fun'.
#	Go to http://en.wikipedia.org/wiki/Garden_path_sentence and have a brief read at what a 'Garden Path sentence' is (at the top) and look at the 'Examples'

#	Create the file garden.py for this task.
#	Use some Garden Path sentences or think up your own (at least 5).
#   Here, tokenise and perform Entity recognition for each of the sentences after you have stored them in a list called gardenpathSentences.
#	See how spaCy has categorised these sentences and look up the entities you dont understand
#	At the bottom of your file, write a comment about two unusual entities you found that spaCy gave one of the words of your sentences - did you expect this?

#=============================================================================================================================================================

 # I'm not too creative so I stole the Garden Path sentences from: https://www.apartmenttherapy.com/garden-sentences-262915
garden1 = "Oprah convinced her children are noisy."
nlp_garden1 = nlp(garden1)
[token.orth_ for token in nlp_garden1]
print([(token, token.orth_, token.orth) for token in nlp_garden1]) # tokenization
print([(i, i.label_, i.label) for i in nlp_garden1.ents]) # entity recognition

garden2 = "That Jill is never here hurts."
nlp_garden2 = nlp(garden2)
[token.orth_ for token in nlp_garden2]
print([(token, token.orth_, token.orth) for token in nlp_garden2]) # tokenization
print([(i, i.label_, i.label) for i in nlp_garden2.ents]) # entity recognition

garden3 = "The Tom Cruise who whistles tunes pianos."
nlp_garden3 = nlp(garden3)
[token.orth_ for token in nlp_garden3]
print([(token, token.orth_, token.orth) for token in nlp_garden3]) # tokenization
print([(i, i.label_, i.label) for i in nlp_garden3.ents]) # entity recognition

garden4 = "Bill gave the child the dog bit a Band-Aid."
nlp_garden4 = nlp(garden4)
[token.orth_ for token in nlp_garden4]
print([(token, token.orth_, token.orth) for token in nlp_garden4]) # tokenization
print([(i, i.label_, i.label) for i in nlp_garden4.ents]) # entity recognition

garden5 = "Fat Sam eat accumulates."
nlp_garden5 = nlp(garden5)
[token.orth_ for token in nlp_garden5]
print([(token, token.orth_, token.orth) for token in nlp_garden5]) # tokenization
print([(i, i.label_, i.label) for i in nlp_garden5.ents]) # entity recognition

'''
I'm not sure if this is all done correctly, but actually for each sentence I was only given a single recognized entity (ex. [(Oprah, 'PERSON', 380)]).
I thought this was strange because it seems to only pick up on proper nouns, however if i use the name "Mary" the entity is not recognized as an entity at all.
Furthermore, I got the recognized entities of "Oprah", "Jill", & "Bill"; Which are a single word, but I got "Tom Cruise" and "Fat Sam" recognized as two word entities with the same classifications.'''

"""# New Section"""