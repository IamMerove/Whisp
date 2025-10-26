from pydub import AudioSegment
import os

# NOTE : Utiliser r"" est plus sûr pour les chemins Windows
racine_projet = r"C:\Users\Apprenant\Desktop\Simplon\22_10"
input_path = os.path.join(racine_projet, "data", "raw_audio", "test.mp3")
output_path = os.path.join(racine_projet, "data", "raw_audio", "test.wav")

try:
    print(f"1. Tentative de chargement du MP3 : {input_path}")
    # Pydub cherche FFmpeg.exe et l'utilise pour décoder le MP3.
    audio = AudioSegment.from_mp3(input_path)
    
    # 2. Exporter en WAV avec ré-échantillonnage 16kHz
    print(f"2. Conversion en WAV (16kHz) vers : {output_path}")
    audio.export(output_path, format="wav", parameters=["-ar", "16000"]) 
    
    print("\n✅ Conversion réussie ! Vérifiez la présence de test.wav.")

except FileNotFoundError as e:
    # Ceci est l'erreur la plus probable si ça échoue, même maintenant
    print(f"\n❌ ERREUR GRAVE : FFmpeg n'est pas trouvable ou accessible.")
    print("Vérifiez manuellement si 'ffmpeg.exe' existe dans le dossier 'Scripts' de votre environnement Conda.")
    
except Exception as e:
    print(f"\n❌ ERREUR : {e}")

# Exécutez ce script depuis la racine du projet: python convert.py