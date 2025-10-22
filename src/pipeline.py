# src/pipeline.py
from src.transcription.transcriber import transcribe_audio
from src.summarization.summarizer import summarize_text
from src.config import AUDIO_PATH
import os

def audio_to_summary(audio_filename: str):
    audio_path = os.path.join(AUDIO_PATH, audio_filename)
    transcript = transcribe_audio(audio_path)
    summary = summarize_text(transcript)

    print("🗣️ Transcription (extrait):", transcript[:300], "...\n")
    print("📝 Résumé:\n", summary)
    return transcript, summary

if __name__ == "__main__":
    audio_to_summary("example.wav")
