# 📝 Smart Text Summarizer Web Application

A modern Text Summarization Web App built using Python and Streamlit.

This application generates concise summaries from long text input using Natural Language Processing (NLP) sentence tokenization.


## 🔗 Live Demo

(https://textsummarizerwebapp-ek8hbv4msfwm9pgwagvcj5.streamlit.app/)


## 📌 Project Overview

The Smart Text Summarizer allows users to:

- Paste long paragraphs or articles
- Generate a concise summary instantly
- View original and summarized word counts
- Experience a modern gradient UI design

The app uses NLTK sentence tokenization to extract key sentences and produce a short summary.


## ✨ Features

- Modern Dark Orange + Dark Pink Gradient UI
- Clean centered title design
- Summary displayed in styled card format
- Word count metrics (Original vs Summary)
- Lightweight NLP implementation
- Beginner-friendly deployment


## 🛠 Technologies Used

- Python
- Streamlit
- NLTK (Natural Language Toolkit)


## 📁 Project Structure

text-summarizer-app/
│
├── app.py
├── requirements.txt
└── README.md


## ⚙ Installation & Local Setup

Step 1: Install dependencies

py -m pip install streamlit nltk  
python -m nltk.downloader punkt  

Step 2: Run the application

py -m streamlit run app.py  

The application will open in your browser at:

http://localhost:8501


## 📄 requirements.txt

streamlit  
nltk  


## 🧪 Sample Input

Artificial Intelligence is transforming industries across the world. It enables machines to learn from data, make decisions, and improve over time. AI is widely used in healthcare, finance, education, and automation.


## 📌 Sample Output

Artificial Intelligence is transforming industries across the world. It enables machines to learn from data, make decisions, and improve over time.


## 🌍 Deployment

1. Upload `app.py` and `requirements.txt` to GitHub
2. Login to Streamlit Community Cloud
3. Click **New App**
4. Select your repository
5. Choose `app.py` as the main file
6. Click **Deploy**

Your app will be live with a public URL.


## 👩‍💻 Author

Dasari Renuka  
B.Tech Computer Science Engineering Student  


## 📜 License

This project is open-source and free for educational purposes.
