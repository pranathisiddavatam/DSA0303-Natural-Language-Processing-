import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
stemmer = PorterStemmer()
words = ["jumping", "jumps", "jumped", "running", "runner", "easily"]
stemmed_words = [stemmer.stem(word) for word in words]
for word, stemmed_word in zip(words, stemmed_words):
    print(f"{word} => {stemmed_word}")

