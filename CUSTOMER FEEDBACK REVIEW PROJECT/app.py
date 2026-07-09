import streamlit as st
import re
import nltk
import pandas as pd
import numpy as np

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# Download stopwords (first time only)
nltk.download('stopwords')

# Title
st.title("🍽️ Restaurant Review Sentiment Analysis")

# Load dataset
@st.cache_data
def load_data():
    dataset = pd.read_csv(
        r'D:\AI NLP -NATURAL LANGUAGE PROCESSING DATA\Restaurant_Reviews.tsv',
        delimiter='\t',
        quoting=3
    )
    return dataset

dataset = load_data()

# Text preprocessing
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_text(text):
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower().split()
    review = [ps.stem(word) for word in review if word not in stop_words]
    return ' '.join(review)

# Prepare corpus
@st.cache_data
def prepare_data(dataset):
    corpus = [clean_text(review) for review in dataset['Review']]
    return corpus

corpus = prepare_data(dataset)

# TF-IDF
@st.cache_resource
def train_model(corpus, dataset):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus).toarray()
    y = dataset.iloc[:, 1].values

    model = RandomForestClassifier(
        max_depth=4,
        n_estimators=60,
        random_state=0,
        criterion='entropy'
    )
    model.fit(X, y)

    return vectorizer, model

vectorizer, model = train_model(corpus, dataset)

# User input
user_input = st.text_area("Enter your review:")

# Prediction
if st.button("Predict Sentiment"):
    if user_input.strip() != "":
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned]).toarray()
        prediction = model.predict(vectorized)[0]

        if prediction == 1:
            st.success("✅ Positive Review 😊")
        else:
            st.error("❌ Negative Review 😡")
    else:
        st.warning("Please enter a review!")
