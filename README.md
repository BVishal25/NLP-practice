(I may not be able to talk about everything in NLP. As the below words are my understanding through the journey, don't expect much)

# NLP-practice
I am practicing my NLP skills by learning NLP and techniques. I am writing my understanding through this.

## What is NLP?
NLP is a sub-field of AI where making the machines to understand human speech and the emotions within it and have an amazing interaction with humans.

## Why need NLP for Tamil language?
As Tamil language has a 5000 years of history and my mother tongue too. It is already a challenge to train a NLP for english language which only has 26 letters, but in Tamil there are whooping 247 letters present. It is a biggest challenge to train Tamil with NLP and work it finely. But it needs to be done.

# Process
(cooking anology)
1. Text Preprocessing techniques (chopping and cleaning)
2. Document representation methods (Spices and Flavors)

## Text Preprocessing (chopping and cleaning)
(cooking anology)
This is a fantastic step. It is not only important to select the ingredient (raw text), it is also important to cut it into bitable size (tokenization) according to the dish (problem), peel the skins (punctuation and stop words removal), remove unnecessary parts (stemming), make the ingredient into simple from its complex form ie. Banana flower (lemmatization)

1. raw text
2. tokenization
3. punctuation and stop words removal
4. stemming
5. lemmatization

### Raw Text (raw ingredients)
Each ingredient give the different taste, like that each text (file) has different content which is used to cook variety of models. So choosing a data set is verty important for making a NLP model.

### Tokenization // Punctuation and stop words removal (chopping the ingredients)
We all have small mouth. We can only chew the ingredient if it fits the mouth and it is easy to digest. like that tokening (small part) the text is necessary to train a NLP model. There are types of tokenization

1. Word tokenization (word by word cutting)
2. sentence tokenization (sentence by sentence cutting)

punctuation and stop words removal also comes under tokenization but it is a some specific process. You see, a peeled ingredients is good. Because the skin doesn't have the taste, all tastes are inside. So you know what to do.

### Stemming (roughly chopping the vegetables)
We cut each end of the ingredients for the better preparation. Like that we remove pre/suffices of words in the text. 

### Lemmatization (chopping the vegetables into precise and recognizable pieces)
Clean the ingredients while preserving the essence of taste. Removing the unwanted words while preserving the grammar.

## Document representation methods (Spices and Flavors)
Adding flavors to the ingredients and making specific spices. Like converting the preprocessed words to numerical values for the machine learning works (or the NLP problems)

### Bag of Words - BoW (creating the spices for the dish)
collection of unique words and their frequencies in the document. This ignores word order and grammatical structure.

### TF-IDF -- Term Frequency-Inverse Document Frequency (adding spices in specific proportions based on their availability and importance in the dish)
Weighting words based on their importance in the document and their rarity across all documents. Helps identify words that are most informative for the document.
