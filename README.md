# 🧞‍♂️ HelpGenie — Your Personal Support Genie

Tired of waiting for customer support?
Say hello to **HelpGenie** — your instant, no-nonsense, always-available support assistant ✨

---

## 💡 What is HelpGenie?

HelpGenie is a **customer support chatbot** that answers user queries like:

* 📦 Where is my order?
* 💸 How to get a refund?
* 💳 Payment failed?
* 🚚 Delivery issues?

👉 Basically, it’s like a **mini customer care agent**, but faster 

---

## 🧠 How it Works (Simple Version)

1. You ask a question
2. The chatbot converts your text into numbers using **TF-IDF**
3. It compares your question with existing patterns using **cosine similarity**
4. Finds the closest match
5. Returns the best possible answer

👉 In short:

```
Text → Numbers → Compare → Best Match → Answer
```

---

## 📊 Dataset Info

* Shape: **(124, 3)**
* Columns:

  * **Intent** → category of query
  * **Patterns** → different ways of asking
  * **Response** → final answer

👉 Bonus:
Each row can have multiple patterns separated by `;`
So internally, the chatbot actually handles **many more queries**.

---

## ⚙️ Tech Stack

* 🐍 Python
* 📊 Pandas
* 🧠 Scikit-learn (TF-IDF + Cosine Similarity)
* 🎨 Streamlit (for UI)

---

## 🎨 Features

* 💬 Chat-based UI
* 🧞‍♂️ Friendly responses
* ⚡ Instant replies
* 🧠 Smart matching (not exact keyword matching)

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install streamlit pandas scikit-learn
```

### 2. Run the app

```
streamlit run app.py
```

---

## ⚠️ Limitations

Let’s be honest 😄

* Not 100% accurate (around **75%**)
* Doesn’t fully understand meaning (yet 👀)
* Works best with known patterns

---

## 🔥 Future Improvements

* Upgrade to **Embeddings (semantic understanding)**
* Add **LLM (ChatGPT-like responses)**
* Store data in **SQL database**
* Add **context memory (multi-turn chat)**

---

## 🧠 Learning Outcome

This project helped in understanding:

* NLP basics
* Text vectorization
* Similarity matching
* Building UI with Streamlit

---

## ✨ Final Thought

> HelpGenie may not be magic...
> but it’s definitely close 🧞‍♂️

---

## 👩‍💻 Author

Built with curiosity, caffeine ☕, and a little bit of chaos 😄
