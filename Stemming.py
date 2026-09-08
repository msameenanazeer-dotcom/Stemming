from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

text = "playing played plays studies studying"

words = word_tokenize(text)

stemmer = PorterStemmer()

for word in words:

    print(
        word,
        "->",
        stemmer.stem(word)
    )
