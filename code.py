import streamlit as st
import nltk
from nltk.tokenize import sent_tokenize

st.set_page_config(page_title="Smart Text Summarizer", layout="wide")

# Custom CSS
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(90deg,#7b2cff,#ff7a18);
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: white;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: white;
}

.summary-box {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# Title Section
st.markdown('<div class="title">📝 Smart Text Summarizer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Generate concise summaries instantly using NLP</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Input
text = st.text_area("📄 Paste your text here:", height=250)

def summarize(text, n=3):
    sentences = sent_tokenize(text)
    return " ".join(sentences[:n])

if st.button("Generate Summary"):
    if text.strip() == "":
        st.warning("⚠ Please enter text.")
    else:
        summary = summarize(text)

        st.markdown("### Summary Output")
        st.markdown(f'<div class="summary-box">{summary}</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        col1.metric("Original Words", len(text.split()))
        col2.metric("Summary Words", len(summary.split()))

st.markdown("---")
st.caption("🚀 Built with Python + Streamlit + NLTK")
