from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import shutil
import os

from app.services.predict import predict_audio

router = APIRouter()

UPLOAD_FOLDER = "data/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/predict")
async def predict(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = predict_audio(file_path)

    return {
        "filename": file.filename,
        "prediction": result
    }