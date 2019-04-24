# from textblob import TextBlob

# payload = TextBlob('It is great to have seen such a goof siltun')
# spell_correction_text = payload.correct()

# print(spell_correction_text)

# sentimental_analysis_text = spell_correction_text.sentiment

# print(sentimental_analysis_text)

import spacy
from spacy import displacy
from collections import Counter
# import en_core_web_sm
nlp = spacy.load('en_core_web_sm')


doc = nlp('I want to buy two tickets from New york to Chicago tomorrow for 3 people.')
print(doc.ents)
print([(X.text, X.label_) for X in doc.ents])


