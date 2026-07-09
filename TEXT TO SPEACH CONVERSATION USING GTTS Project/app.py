import streamlit as st
from deep_translator import GoogleTranslator

#Set psge title and configuration
st.set_page_config(page_title='Language Converter')

#Apply custom CSS using at.markdown()
# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }

    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #2c3e50;
    }

    .subtitle {
        text-align: center;
        color: #7f8c8d;
        margin-bottom: 30px;
    }

    .stTextArea textarea {
        border-radius: 10px;
        border: 1px solid #ccc;
        padding: 10px;
        font-size: 16px;
    }

    .stButton>button {
        background-color: #2c3e50;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
        width: 100%;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #1abc9c;
        color: white;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        color: gray;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------
st.markdown('<h1 class="title">Language Converter</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Convert text into natural voice using AI</p>', unsafe_allow_html=True)



# Initialize the translator
translator = GoogleTranslator()

# Audio (optional)
st.audio("ad.m4a", format="audio/mpeg", loop=False)

# Streamlit app title
#st.title("Language Converter")

# Text input
text_to_translate = st.text_area("Hi, Please enter text here to translate")

# Dropdowns for selecting source and target languages
source_language = st.selectbox(
    "Select your source language",
    list(LANGUAGES.values()),
    index=list(LANGUAGES.keys()).index("en")
)

target_language = st.selectbox(
    "Select the target language you want",
    list(LANGUAGES.values()),
    index=list(LANGUAGES.keys()).index("es")
)

# Language codes
source_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(source_language)]
target_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]

# Translate button
if st.button("Translate"):
    if text_to_translate.strip() != "":
        
        # Translate the text
        translation = translator.translate(
            text_to_translate,
            src=source_language_code,
            dest=target_language_code
        )

        # Success message
        st.write("Translated Successfully!")

        # Display translated text
        st.write(f"**Your Translated Text:** ---- {translation.text}")

    else:
        st.error("Please enter some text to translate.")

# Instructions
st.write(
    "Enter text in the text area above, select source and target languages, "
    "and click 'Translate' to see the translation."
)