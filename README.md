
# 🧠 LLM-Powered Flashcard Generator (Modular Version)

A Streamlit app that converts educational content into flashcards using Gemini LLM and stores them in a PostgreSQL database.

## 📦 Project Structure

```
llm_flashcard_generator/
├── app.py
├── utils.py
├── static/
│   └── style.css (optional)
├── requirements.txt
└── README.md
```

## 🚀 Features

- Paste text or upload PDFs
- Generate 10–15 flashcards using Gemini API
- Save to PostgreSQL
- Export to CSV or JSON
- Refresh and delete flashcards

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Update your credentials in `app.py`:

```python
GEMINI_API_URL = "https://your-gemini-api-url.com/generate"
DATABASE_URL = "postgresql://postgres:R%40jz4711@localhost:5432/flask_chatbot"
```

---
