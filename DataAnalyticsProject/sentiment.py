from textblob import TextBlob
import pandas as pd

# Sample reviews
reviews = [
    "This product is amazing",
    "Worst experience ever",
    "Very good quality",
    "I love this product",
    "Not worth the money",
    "Average item"
]

# Create dataframe
df = pd.DataFrame(reviews, columns=["Review"])

# Sentiment function
def get_sentiment(text):

    analysis = TextBlob(text)

    if analysis.sentiment.polarity > 0:
        return "Positive"

    elif analysis.sentiment.polarity < 0:
        return "Negative"

    else:
        return "Neutral"

# Apply function
df["Sentiment"] = df["Review"].apply(get_sentiment)

# Print result
print(df)