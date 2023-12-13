import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
# Download NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# Sample sentence
sentence = "Part-of-speech tagging is important for natural language processing."
# Tokenize the sentence
words = word_tokenize(sentence)
# Perform POS tagging
# Display the result
print(pos_tags)
