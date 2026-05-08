from app.features.preprocess import load_audio
from app.features.preprocess import normalize_audio
from app.features.preprocess import extract_mfcc

file_path = "data/raw/real/file_example_WAV_1MG.wav"

audio, sr = load_audio(file_path)

normalized_audio = normalize_audio(audio)

mfcc_features = extract_mfcc(normalized_audio, sr)

print("MFCC Shape:", mfcc_features.shape)

print("MFCC Features:")

print(mfcc_features)