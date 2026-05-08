import joblib

from app.features.preprocess import load_audio
from app.features.preprocess import normalize_audio
from app.features.preprocess import extract_mfcc


model = joblib.load(
    "models/deepfake_detector.pkl"
)


def predict_audio(file_path):

    audio, sr = load_audio(file_path)

    normalized_audio = normalize_audio(audio)

    mfcc_features = extract_mfcc(
        normalized_audio,
        sr
    )

    prediction = model.predict(
        [mfcc_features]
    )[0]

    if prediction == 0:
        return "REAL"

    return "FAKE"