import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# App title
st.title("🧠 Social Media Sentiment Analyzer")
st.subheader("🔍 Classify tweets/posts as Positive, Negative, or Neutral")

# Input from user
user_input = st.text_area("Enter a tweet or post:", height=150)

# Analyze sentiment
if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        scores = analyzer.polarity_scores(user_input)
        compound = scores['compound']

        # Determine sentiment
        if compound >= 0.05:
            sentiment = "Positive 😊"
        elif compound <= -0.05:
            sentiment = "Negative 😠"
        else:
            sentiment = "Neutral 😐"

        st.markdown(f"### Sentiment: **{sentiment}**")
        st.markdown(f"**Polarity Scores:** `{scores}`")

        # Plot bar chart
        fig, ax = plt.subplots()
        labels = ['Positive', 'Neutral', 'Negative']
        values = [scores['pos'], scores['neu'], scores['neg']]
        colors = ['green', 'gray', 'red']

        ax.bar(labels, values, color=colors)
        ax.set_ylim([0, 1])
        ax.set_ylabel("Score")
        ax.set_title("Sentiment Breakdown")

        st.pyplot(fig)
