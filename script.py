# HelpGenie - Customer Support Chatbot

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Dataset

@st.cache_data
def load_data():
    df = pd.read_csv("support_chatbot.csv")
    return df

df = load_data()

# Prepare Data

pattern_response = []

for _, row in df.iterrows():
    raw_patterns = row["Patterns"]
    
    if pd.isna(raw_patterns):
        continue
        
    for pattern in str(raw_patterns).split(";"):   
        pattern = pattern.strip().lower()
        if pattern:
            pattern_response.append((pattern, row["Response"]))

patterns = [p[0] for p in pattern_response]
responses = [p[1] for p in pattern_response]

# TF-IDF Model

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)


# Chatbot Function

def get_response(user_input, threshold=0.25):
    user_input = user_input.lower().strip()
    
    if not user_input:
        return "Type something so I can help you 😊"
    
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X).flatten()
    
    best_idx = similarity.argmax()
    
    if similarity[best_idx] < threshold:
        return "Hmm 🤔 I didn't quite get that. Try asking differently?"
    
    return responses[best_idx]

# Streamlit UI

st.set_page_config(
    page_title="HelpGenie 🧞‍♂️",
    page_icon="🧞‍♂️",
    layout="centered"
)

st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(120deg, #18181c 0%, #232323 40%, #1a1a1a 80%, #000000 100%);
            position: relative;
            min-height: 100vh;
        }
        .stApp::before {
            content: "";
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: radial-gradient(ellipse at 60% 10%, rgba(80,80,120,0.10) 0%, rgba(0,0,0,0.0) 60%),
                        radial-gradient(ellipse at 20% 80%, rgba(60,0,60,0.10) 0%, rgba(0,0,0,0.0) 70%);
            pointer-events: none;
            z-index: 0;
        }
        .stChatMessage {
            border-radius: 16px;
            padding: 14px;
            margin-bottom: 12px;
            box-shadow: 0 4px 24px 0 rgba(30,30,40,0.18);
            position: relative;
            z-index: 1;
        }
        .user-msg {
            background: linear-gradient(90deg, #232323 60%, #18181c 100%);
            color: #f3eaff;
            padding: 10px;
            border-radius: 12px;
            box-shadow: 0 2px 8px 0 rgba(80,80,120,0.10);
        }
        .bot-msg {
            background: linear-gradient(90deg, #18181c 60%, #232323 100%);
            color: #f3eaff;
            padding: 10px;
            border-radius: 12px;
            box-shadow: 0 2px 8px 0 rgba(80,80,120,0.10);
        }
        .stTextInput > div > div > input {
            background-color: #232323;
            color: #f3eaff;
            border-radius: 10px;
        }
        .stChatInputContainer {
            background: #18181c;
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# Title Section

st.title("🧞‍♂️ HelpGenie")
st.caption("Instant answers. Zero waiting. Your personal support genie ✨")

st.write("Track orders • Fix payments • Get refunds • Resolve issues — all in one place!")

# Chat History

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User Input

user_input = st.chat_input("Type your message...")

if user_input:
    if user_input.lower() in ["bye", "exit", "quit"]:
        response = "Goodbye! Hope I made things easier for you! ✨"
    else:
        response = get_response(user_input)
    
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))

# Display Chat

for idx, (sender, message) in enumerate(st.session_state.chat_history):
    is_last = idx == len(st.session_state.chat_history) - 1
    avatar = "🧑‍💻" if sender == "user" else "🧞‍♂️"
    bubble_class = "user-msg" if sender == "user" else "bot-msg"
    extra_style = ""
    with st.chat_message(sender, avatar=avatar):
        st.markdown(f"<div class='{bubble_class}' style='font-size: 1.1rem; font-weight: 500; {extra_style}'>{message}</div>", unsafe_allow_html=True)