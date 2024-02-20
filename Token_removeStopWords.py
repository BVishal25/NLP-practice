## problem 2: remove stop words (nltk library)

import nltk
from nltk.corpus import stopwords
nltk.download('Punkt')
nltk.download('stopwords')

text =""" Stop words are words that do not contribute much to the meaning of a sentence. They are often used to make sentences grammatically correct, but they do not add any new information. Stop words can be removed from text data to improve the performance of natural language processing (NLP) tasks.
There are two popular libraries for NLP in Python: NLTK and spaCy. Both of these libraries have functions for removing stop words."""

res = []

for i in text.split():
  if i not in stopwords.words('english'):
    res.append(i)

print('The result without stopwords: ','\n',res)
