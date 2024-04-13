from textblob import TextBlob

def analyze_sentiment(text):
    """Analyze sentiment of news articles."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return polarity

def categorize_sentiment(polarity):
    """Categorize sentiment polarity into positive, neutral, or negative."""
    if polarity > 0:
        return "Positive"
    elif polarity == 0:
        return "Neutral"
    else:
        return "Negative"
