# src/transcription/transcriber.py
import librosa
from transformers import pipeline

class Transcriber:
    def __init__(self, model_name="openai/whisper-small", device="cpu"):
        print(f"Chargement du modèle {model_name}...")
        self.stt = pipeline(
            "automatic-speech-recognition", 
            model=model_name, 
            device=device
        )
        print("Modèle chargé !")
    
    def transcribe(self, audio_file):
        """
        Transcrit un fichier audio en texte
        
        Args:
            audio_file: Chemin vers le fichier audio
            
        Returns:
            str: Texte transcrit
        """
        print(f"Chargement de l'audio: {audio_file}")
        # Charger l'audio avec librosa à 16kHz
        audio_array, sampling_rate = librosa.load(audio_file, sr=16000)
        print(f"Audio chargé : {len(audio_array)/sampling_rate:.2f}s à {sampling_rate}Hz")
        
        print("Transcription en cours...")
        # Transcrire (sans passer sampling_rate)
        result = self.stt(audio_array)
        
        return result['text']