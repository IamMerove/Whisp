from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import shutil
from pathlib import Path
from transcription.transcriber import Transcriber

# Créer l'application FastAPI
app = FastAPI(
    title="Audio Transcription API",
    description="API pour transcrire des fichiers audio avec Whisper",
    version="1.0.0"
)

# Configuration CORS pour permettre les requêtes depuis votre webapp
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En production, spécifiez votre domaine
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialiser le transcriber
transcriber = Transcriber(model_name="openai/whisper-small", device="cpu")

# Dossier temporaire pour les uploads
UPLOAD_DIR = Path("../data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.get("/")
async def root():
    """Point d'entrée de l'API"""
    return {
        "message": "API de transcription audio",
        "version": "1.0.0",
        "endpoints": {
            "/transcribe": "POST - Envoyer un fichier audio pour transcription",
            "/health": "GET - Vérifier l'état de l'API"
        }
    }

@app.get("/health")
async def health_check():
    """Vérifier que l'API fonctionne"""
    return {"status": "healthy", "model": "whisper-small"}

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Transcrire un fichier audio
    
    Args:
        file: Fichier audio (WAV, MP3, etc.)
        
    Returns:
        JSON avec la transcription
    """
    # Vérifier le type de fichier
    allowed_extensions = {".wav", ".mp3", ".m4a", ".flac", ".ogg"}
    file_extension = os.path.splitext(file.filename)[1].lower()
    
    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Format non supporté. Formats acceptés: {', '.join(allowed_extensions)}"
        )
    
    # Sauvegarder temporairement le fichier
    temp_file_path = UPLOAD_DIR / file.filename
    
    try:
        # Écrire le fichier uploadé
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Transcrire
        transcription = transcriber.transcribe(str(temp_file_path))
        
        # Nettoyer le fichier temporaire
        os.remove(temp_file_path)
        
        return JSONResponse(content={
            "success": True,
            "filename": file.filename,
            "transcription": transcription
        })
    
    except Exception as e:
        # Nettoyer en cas d'erreur
        if temp_file_path.exists():
            os.remove(temp_file_path)
        
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de la transcription: {str(e)}"
        )

@app.delete("/cleanup")
async def cleanup_uploads():
    """Nettoyer tous les fichiers temporaires"""
    try:
        for file in UPLOAD_DIR.glob("*"):
            if file.is_file():
                os.remove(file)
        return {"message": "Fichiers temporaires supprimés"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)