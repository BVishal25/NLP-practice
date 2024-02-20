## problem 2: remove stop words (spaCy library)
import spacy
nlp = spacy.load("en_core_web_sm")
stopWords_spacy = spacy.lang.en.stop_words.STOP_WORDS

text =""" Stop words are words that do not contribute much to the meaning of a sentence. They are often used to make sentences grammatically correct, but they do not add any new information. Stop words can be removed from text data to improve the performance of natural language processing (NLP) tasks.
There are two popular libraries for NLP in Python: NLTK and spaCy. Both of these libraries have functions for removing stop words."""

res_spacy = []
for i in text.split():
  if i not in stopWords_spacy:
    res_spacy.append(i)

print('The result without stopwords (spacy): ','\n',res_spacy)
