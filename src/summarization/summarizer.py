# src/summarization/summarizer.py
from transformers import pipeline
from src.config import SUMMARIZER_MODEL_NAME

def summarize_text(text: str) -> str:
    summarizer = pipeline("summarization", model=SUMMARIZER_MODEL_NAME)
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]["summary_text"]

if __name__ == "__main__":
    text = "Votre texte long ici..."
    print("📝 Résumé:\n", summarize_text(text))
