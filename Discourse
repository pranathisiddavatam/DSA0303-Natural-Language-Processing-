import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
sample_text = "NLP is a subfield of artificial intelligence."
sentences = nltk.sent_tokenize(sample_text)
sia = SentimentIntensityAnalyzer()
for i, sentence in enumerate(sentences):
    if i > 0:
        print("\n--- Discourse Relation: Continuation ---")
    else:
        print("--- Discourse Relation: Beginning ---")
    print("Sentence:", sentence)
    sentiment = sia.polarity_scores(sentence)
    print("Sentiment Scores:")
    print(f"Positive: {sentiment['pos']:.2f}")
    print(f"Negative: {sentiment['neg']:.2f}")
    print(f"Neutral: {sentiment['neu']:.2f}")
    words = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)
    print("Part-of-Speech Tags:")
    for word, pos in pos_tags:
        print(f"{word}: {pos}")
