import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analyzer")

st.title("🧠 Sentiment Analysis App (Simple Version)")

text = st.text_area("Enter your text:")

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            st.success("Sentiment: POSITIVE 😊")
        elif polarity < 0:
            st.error("Sentiment: NEGATIVE 😞")
        else:
            st.info("Sentiment: NEUTRAL 😐")

        st.write("Polarity Score:", round(polarity, 3))