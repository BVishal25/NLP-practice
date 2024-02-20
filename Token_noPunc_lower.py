## problem 1: program to take a string, tokenize it without punctuation, convert everything into lowercase.

import string
# taken input
gets = input()
get = gets.lower()
print('Typed words: '+get)
# split into small words
small_token = get.split()
# to remove punctuations and symbols
tables = str.maketrans('','',string.punctuation)
# final tokens
tokens_final = [st.translate(tables) for st in small_token]
print("all lowercase tokens: ",tokens_final)
