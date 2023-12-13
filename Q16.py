from nltk import bigrams, word_tokenize
# Sample sentence
sentence = "Natural language proceimport nltkssing is fascinating."
# Tokenize the sentence
words = word_tokenize(sentence)
# Generate bigrams
bigrams_list = list(bigrams(words))
# Display the result
print(bigrams_list)
