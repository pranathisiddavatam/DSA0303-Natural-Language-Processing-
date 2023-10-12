import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()
text = "I love this product! It's fantastic."
sentiment = analyzer.polarity_scores(text)
compound_score = sentiment['compound']
if compound_score >= 0.05:
    sentiment_label = "Positive"
elif compound_score <= -0.05:
    sentiment_label = "Negative"
else:
    sentiment_label = "Neutral"
print("Text:", text)
print("Sentiment Score:", sentiment_label)
print("Positive: {:.2f}%".format(sentiment['pos'] * 100))
print("Negative: {:.2f}%".format(sentiment['neg'] * 100))
print("Neutral: {:.2f}%".format(sentiment['neu'] * 100))
