import nltk
from nltk import word_tokenize
from nltk import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
text = "NLTK is a leading platform for building Python programs to work with human language data."
words = word_tokenize(text)
pos_tags = pos_tag(words)
print(pos_tags)
