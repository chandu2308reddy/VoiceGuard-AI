from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
import shutil
import os

router = APIRouter()

REAL_FOLDER = "data/raw/real"


@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):

    file_path = os.path.join(REAL_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "saved_to": file_path,
        "message": "Audio uploaded successfully"
    }