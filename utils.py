import fitz
import requests

def extract_pdf_text(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)

def generate_flashcards(text, subject, gemini_api_url):
    prompt = f"""
    You are an AI tutor. Generate 10–15 flashcards in Q&A format from the following {subject} text.
    Each question should be clear and each answer should be factual and self-contained.

    TEXT:
    {text[:3000]}
    """

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(gemini_api_url, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return "❌ Gemini returned an unexpected response format."
    else:
        return f"❌ Error: {response.status_code} - {response.text}"


def parse_output(raw):
    flashcards = []
    for line in raw.split('\n'):
        if ':' in line:
            q, a = line.split(':', 1)
            flashcards.append({"Question": q.strip(), "Answer": a.strip()})
    return flashcards
