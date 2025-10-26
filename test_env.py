# test_env.py
import librosa
import soxr
from transformers import pipeline

print("Librosa OK")
print("SOXR OK")

# Test rapide de transcription (Whisper)
stt = pipeline("automatic-speech-recognition", model="openai/whisper-small", device="cpu")
print("Transformers OK")

# Charger l'audio avec librosa
audio_file = "data/raw_audio/test_clean.wav"
audio_array, sampling_rate = librosa.load(audio_file, sr=16000)
print(f"Audio chargé : {len(audio_array)/sampling_rate:.2f}s à {sampling_rate}Hz")

# Transcrire - passer SEULEMENT l'array, pas le sampling_rate
result = stt(audio_array)
print("Transcription :", result['text'])