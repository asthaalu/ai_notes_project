%%writefile app.py

import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
from pypdf import PdfReader
from transformers import pipeline
import time

# CONFIG
st.set_page_config(page_title="AI Doubt Solver", page_icon="🤖", layout="centered")

# 🌙 DARK CHAT UI
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Center content */
.block-container {
    max-width: 700px;
}

/* Title */
.title {
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    color: #fbcfe8;
}

/* Chat bubble user */
.user-bubble {
    background: #c4b5fd;
    color: black;
    padding: 10px 15px;
    border-radius: 15px;
    margin: 10px 0;
    text-align: right;
}

/* Chat bubble bot */
.bot-bubble {
    background: #1e293b;
    padding: 12px;
    border-radius: 15px;
    margin: 10px 0;
    border-left: 4px solid #f9a8d4;
}

/* Input */
.stTextInput input {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 12px;
    border: 1px solid #c4b5fd !important;
}

/* Upload */
section[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.05);
    padding: 10px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("<div class='title'>🤖 AI Chat Doubt Solver</div>", unsafe_allow_html=True)

# Upload
uploaded_file = st.file_uploader("📄 Upload your PDF", type="pdf")

if uploaded_file:

    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    model = SentenceTransformer('all-MiniLM-L6-v2')
    generator = pipeline("text-generation", model="gpt2")

    sentences = text.split("\n")
    embeddings = model.encode(sentences)

    def get_answer(query):
        query_embedding = model.encode([query])
        scores = np.dot(embeddings, query_embedding.T)
        best_index = np.argmax(scores)
        return sentences[best_index]

    def smart_answer(query):
        base = get_answer(query)
        prompt = f"Question: {query}\nAnswer: {base}\nExplain simply:"
        result = generator(prompt, max_new_tokens=120)
        return result[0]['generated_text']

    # SESSION STORAGE (chat history)
    if "history" not in st.session_state:
        st.session_state.history = []

    # INPUT
    query = st.text_input("💬 Ask something...")

    if query:
        st.session_state.history.append(("user", query))

        # typing effect
        with st.spinner("🤖 typing..."):
            answer = smart_answer(query)
            time.sleep(1)

        st.session_state.history.append(("bot", answer))

    # DISPLAY CHAT
    for role, msg in st.session_state.history:
        if role == "user":
            st.markdown(f"<div class='user-bubble'>{msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-bubble'>{msg}</div>", unsafe_allow_html=True)%%writefile app.py

import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
from pypdf import PdfReader
from transformers import pipeline
import time

# CONFIG
st.set_page_config(page_title="AI Doubt Solver", page_icon="🤖", layout="centered")

# 🌙 DARK CHAT UI
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Center content */
.block-container {
    max-width: 700px;
}

/* Title */
.title {
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    color: #fbcfe8;
}

/* Chat bubble user */
.user-bubble {
    background: #c4b5fd;
    color: black;
    padding: 10px 15px;
    border-radius: 15px;
    margin: 10px 0;
    text-align: right;
}

/* Chat bubble bot */
.bot-bubble {
    background: #1e293b;
    padding: 12px;
    border-radius: 15px;
    margin: 10px 0;
    border-left: 4px solid #f9a8d4;
}

/* Input */
.stTextInput input {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 12px;
    border: 1px solid #c4b5fd !important;
}

/* Upload */
section[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.05);
    padding: 10px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("<div class='title'>🤖 AI Chat Doubt Solver</div>", unsafe_allow_html=True)

# Upload
uploaded_file = st.file_uploader("📄 Upload your PDF", type="pdf")

if uploaded_file:

    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    model = SentenceTransformer('all-MiniLM-L6-v2')
    generator = pipeline("text-generation", model="gpt2")

    sentences = text.split("\n")
    embeddings = model.encode(sentences)

    def get_answer(query):
        query_embedding = model.encode([query])
        scores = np.dot(embeddings, query_embedding.T)
        best_index = np.argmax(scores)
        return sentences[best_index]

    def smart_answer(query):
        base = get_answer(query)
        prompt = f"Question: {query}\nAnswer: {base}\nExplain simply:"
        result = generator(prompt, max_new_tokens=120)
        return result[0]['generated_text']

    # SESSION STORAGE (chat history)
    if "history" not in st.session_state:
        st.session_state.history = []

    # INPUT
    query = st.text_input("💬 Ask something...")

    if query:
        st.session_state.history.append(("user", query))

        # typing effect
        with st.spinner("🤖 typing..."):
            answer = smart_answer(query)
            time.sleep(1)

        st.session_state.history.append(("bot", answer))

    # DISPLAY CHAT
    for role, msg in st.session_state.history:
        if role == "user":
            st.markdown(f"<div class='user-bubble'>{msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-bubble'>{msg}</div>", unsafe_allow_html=True)