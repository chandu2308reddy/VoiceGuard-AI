import os
import pandas as pd

from app.features.preprocess import load_audio
from app.features.preprocess import normalize_audio
from app.features.preprocess import extract_mfcc


REAL_PATH = "data/raw/real"
FAKE_PATH = "data/raw/fake"

dataset = []


def process_folder(folder_path, label):

    for file_name in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file_name)

        try:

            audio, sr = load_audio(file_path)

            normalized_audio = normalize_audio(audio)

            mfcc_features = extract_mfcc(
                normalized_audio,
                sr
            )

            row = mfcc_features.tolist()

            row.append(label)

            dataset.append(row)

        except Exception as e:

            print(f"Error processing {file_name}: {e}")


process_folder(REAL_PATH, 0)

process_folder(FAKE_PATH, 1)

columns = [f"mfcc_{i}" for i in range(40)]

columns.append("label")

df = pd.DataFrame(dataset, columns=columns)

df.to_csv("data/dataset.csv", index=False)

print("Dataset Created Successfully")

print(df.head())