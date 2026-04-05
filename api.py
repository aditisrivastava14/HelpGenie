from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI(title="HelpGenie API")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data
def load_data():
    return pd.read_csv("support_chatbot.csv")

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

class ChatRequest(BaseModel):
    message: str

@app.post("/api/chat")
def chat(request: ChatRequest):
    user_input = request.message.lower().strip()
    
    if not user_input:
        return {"response": "Type something so I can help you 😊"}
    
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X).flatten()
    
    best_idx = similarity.argmax()
    threshold = 0.25
    
    if similarity[best_idx] < threshold:
        return {"response": "Hmm 🤔 I didn't quite get that. Try asking differently?"}
    
    return {"response": responses[best_idx]}
