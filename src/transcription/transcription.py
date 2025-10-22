# src/transcription/transcriber.py
from transformers import pipeline
from src.config import STT_MODEL_NAME
import os

def transcribe_audio(audio_file: str) -> str:
    asr = pipeline("automatic-speech-recognition", model=STT_MODEL_NAME)
    result = asr(audio_file)
    return result["text"]

if __name__ == "__main__":
    audio_path = "data/raw_audio/example.wav"
    transcript = transcribe_audio(audio_path)
    print("🗣️ Transcription:\n", transcript)
