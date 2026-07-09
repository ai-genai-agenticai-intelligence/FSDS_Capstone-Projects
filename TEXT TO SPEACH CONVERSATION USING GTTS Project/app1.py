import streamlit as st
from deep_translator import GoogleTranslator

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title='Language Converter')

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
    }

    .stButton>button:hover {
        background-color: #1abc9c;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        color: gray;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">🌍 Language Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Translate text easily using AI</div>', unsafe_allow_html=True)

# ---------- INPUT ----------
text_to_translate = st.text_area("✍ Enter text here:")

# ---------- LANGUAGE SELECT ----------
languages = {
    "English": "en",
    "Hindi": "hi",
    "Odia": "or",
    "Spanish": "es",
    "French": "fr"
}

col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox("Source Language", list(languages.keys()))

with col2:
    target_language = st.selectbox("Target Language", list(languages.keys()))

source_code = languages[source_language]
target_code = languages[target_language]

# ---------- TRANSLATE ----------
if st.button("🔄 Translate"):
    if text_to_translate.strip() != "":
        try:
            translated_text = GoogleTranslator(
                source=source_code,
                target=target_code
            ).translate(text_to_translate)

            st.success("✅ Translated Successfully!")
            st.write("### 📝 Translated Text:")
            st.write(translated_text)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("⚠ Please enter some text!")

# ---------- FOOTER ----------
st.markdown('<div class="footer">Developed by <b>Abhishek Sahoo</b></div>', unsafe_allow_html=True)