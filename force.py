from pydub import AudioSegment
from transformers import pipeline

# Initialiser Whisper
stt = pipeline("automatic-speech-recognition", model="openai/whisper-small")

# Chemin du fichier original
input_file = "C:/Users/Apprenant/Desktop/Simplon/22_10/data/raw_audio/test.wav"

# Réécrire le fichier en mono 16 kHz 16-bit PCM
audio = AudioSegment.from_file(input_file)
audio = audio.set_channels(1).set_frame_rate(16000).set_sample_width(2)
clean_file = "C:/Users/Apprenant/Desktop/Simplon/22_10/data/raw_audio/test_clean.wav"
audio.export(clean_file, format="wav")

# Transcription
result = stt(clean_file)
print("Transcription :", result['text'])
