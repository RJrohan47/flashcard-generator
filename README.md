
# 🧠 LLM-Powered Flashcard Generator

An AI-driven flashcard generator that converts raw educational text or PDFs into concise question-answer pairs using **Google Gemini LLM**. Built with **Streamlit** for the UI and **PostgreSQL** for persistent storage, this tool helps students, educators, and content creators automate learning resource generation.

---

## 📌 Key Features

- 📝 **Input Support:** Paste raw text or upload PDF files.
- 🤖 **LLM Integration:** Generate 10–15 flashcards using Google Gemini API.
- 🧠 **Flashcard Format:** Flashcards in Q&A format ideal for revision and learning.
- 💾 **Persistent Storage:** Save generated flashcards in a PostgreSQL database.
- 🔁 **Management Actions:** Refresh, view, delete, and export flashcards.
- 📦 **Export Options:** Download flashcards as CSV or JSON files.
- ⚡ **Minimal UI:** Clean, responsive interface using Streamlit.

---

## 🧱 Tech Stack

| Layer        | Technology             |
|--------------|------------------------|
| 🖥 Frontend   | Streamlit              |
| 🧠 NLP Model  | Google Gemini (via API)|
| 🗃 Backend    | Python + Flask (utils) |
| 🛢 Database   | PostgreSQL             |
| ☁️ Hosting    | Local / Deploy-ready   |

---

## 🗂️ Project Structure 

```
llm_flashcard_generator/
├── app.py
├── utils.py
├── static/
│   └── style.css (optional)
├── requirements.txt
└── README.md
```


## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Update your credentials in `app.py`:

```python
GEMINI_API_URL = "{url_key}"
DATABASE_URL = "postgresql://postgres:password@localhost:5432/flask_chatbot"
```
Make sure PostgreSQl is updated in your system
```
CREATE TABLE flashcards (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
);
```


## 💡 Use Cases
👨‍🎓 Students revising class notes

📚 Educators preparing quizzes

🧑‍💻 EdTech product prototypes

🤖 AI-powered study tools

## 🔒 Security Notes
Avoid exposing your Gemini API key in public repos.

Sanitize all file inputs before production.

Use HTTPS and secure token storage in deployment.


## 🙌 Acknowledgements
Google Gemini for powerful LLM APIs

Streamlit for rapid UI prototyping

PostgreSQL for robust data storage

## 🙋‍♂️ Author
Rohan Jain <br>
B.Tech CSE | Galgotias University <br>
📧 rohanrajzz4711@gmail.com 

