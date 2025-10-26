from transcription.transcriber import Transcriber

# Initialiser
transcriber = Transcriber()

# Transcrire un fichier
audio_path = "../data/raw_audio/test_clean.wav"
transcription = transcriber.transcribe(audio_path)
print(f"Transcription: {transcription}")
