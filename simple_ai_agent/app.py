
import json
import streamlit as st
from fuzzywuzzy import fuzz

st.set_page_config(page_title="My AI Agent", page_icon="🤖", layout="centered")

# Custom CSS for background and input styling
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #6c63ff;
        padding: 8px;
    }
    .stSuccess {
        background-color: #d1ffd6 !important;
        border-radius: 10px;
    }
    .stWarning {
        background-color: #fff3cd !important;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for branding and instructions
st.sidebar.image("https://img.icons8.com/emoji/96/robot-emoji.png", width=80)
st.sidebar.title("Welcome to My AI Agent")
st.sidebar.markdown("""
**Instructions:**
- Type your question in the box below.
- The agent will try to find the best answer from its dataset.
- If it can't answer, it will let you know!
""")

st.title("🤖 My Simple AI Agent")
st.write("<span style='font-size:18px;'>Ask me anything!</span>", unsafe_allow_html=True)

with open("dataset.json", "r") as file:
    dataset = json.load(file)


# Chat history using session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def submit():
    user_input = st.session_state.user_input
    if user_input:
        best_match = None
        highest_score = 0
        for data in dataset:
            score = fuzz.ratio(user_input.lower(), data["question"])
            if score > highest_score:
                highest_score = score
                best_match = data["answer"]
        if highest_score > 60:
            response = f"<span style='font-size:18px;'>🤖 <b>Agent:</b> {best_match}</span>"
            st.session_state.chat_history.append((user_input, response))
        else:
            response = "<span style='font-size:18px;'>🤖 <b>Agent:</b> I am still learning 🤔</span>"
            st.session_state.chat_history.append((user_input, response))
        # Instead of directly assigning, use st.experimental_rerun to clear input
        st.session_state.user_input = ""
        st.rerun()

st.text_input("You:", key="user_input", on_change=submit, value=st.session_state.user_input)

# Display chat history
if st.session_state.chat_history:
    st.markdown("<hr>", unsafe_allow_html=True)
    for q, a in st.session_state.chat_history:
        st.markdown(f"<span style='color:#6c63ff;font-weight:bold;'>You:</span> {q}", unsafe_allow_html=True)
        st.markdown(a, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
