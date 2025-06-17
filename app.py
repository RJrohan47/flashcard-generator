
import streamlit as st
import pandas as pd
import json
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, declarative_base

from utils import extract_pdf_text, generate_flashcards, parse_output

# ---------------- CONFIG ----------------


GEMINI_API_KEY = "AIzaSyDsDXgzFvRcpBa-nd0iuK9honNZhGyCtRY"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

DATABASE_URL = "postgresql://postgres:R%40jz4711@localhost:5432/flask_chatbot"


# SQLAlchemy Setup
Base = declarative_base()
class Flashcard(Base):
    __tablename__ = "flashcards"
    id = Column(Integer, primary_key=True)
    question = Column(Text)
    answer = Column(Text)
    subject = Column(String(100))

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="LLM Flashcard Generator", layout="wide")
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🧠 LLM-Powered Flashcard Generator")

st.sidebar.header("Upload Content")
input_method = st.sidebar.radio("Choose Input", ["Paste Text", "Upload PDF/TXT"])
subject = st.sidebar.selectbox("Optional Subject", ["General", "Biology", "History", "Computer Science"])

text = ""
uploaded_file = None

if input_method == "Paste Text":
    text = st.text_area("Paste content here:", height=300)
else:
    uploaded_file = st.file_uploader("Upload PDF or TXT file", type=["pdf", "txt"])
    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            text = extract_pdf_text(uploaded_file)
        else:
            text = uploaded_file.read().decode("utf-8")

# ---------------- FLASHCARD GENERATION ----------------
if text:
    if st.button("🚀 Generate Flashcards"):
        with st.spinner("Calling Gemini LLM..."):
            output = generate_flashcards(text, subject, GEMINI_API_URL)
            flashcards = parse_output(output)

            if flashcards:
                st.success(f"✅ Generated {len(flashcards)} flashcards!")

                session = SessionLocal()
                for fc in flashcards:
                    card = Flashcard(question=fc["Question"], answer=fc["Answer"], subject=subject)
                    session.add(card)
                session.commit()
                session.close()

                for i, fc in enumerate(flashcards):
                    with st.expander(f"Flashcard {i+1}"):
                        st.markdown(f"**Q:** {fc['Question']}")
                        st.markdown(f"**A:** {fc['Answer']}")

                df = pd.DataFrame(flashcards)
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button("📥 Download CSV", df.to_csv(index=False), "flashcards.csv", "text/csv")
                with col2:
                    st.download_button("📥 Download JSON", json.dumps(flashcards, indent=2), "flashcards.json", "application/json")
            else:
                st.warning("⚠️ No flashcards could be generated.")

# ---------------- VIEW & MANAGE DB ----------------
st.markdown("---")
st.subheader("📚 View Saved Flashcards")

if st.button("🔄 Refresh Stored Flashcards"):
    session = SessionLocal()
    cards = session.query(Flashcard).order_by(Flashcard.id.desc()).all()
    session.close()

    if cards:
        for card in cards:
            with st.expander(f"[{card.subject}] {card.question[:50]}..."):
                st.markdown(f"**Q:** {card.question}")
                st.markdown(f"**A:** {card.answer}")
    else:
        st.info("No saved flashcards.")

if st.button("🗑 Clear All Flashcards"):
    session = SessionLocal()
    session.query(Flashcard).delete()
    session.commit()
    session.close()
    st.success("All flashcards deleted.")
