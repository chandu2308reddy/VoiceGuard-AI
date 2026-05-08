import librosa
import numpy as np


def load_audio(file_path, sample_rate=16000):

    audio, sr = librosa.load(
        file_path,
        sr=sample_rate
    )

    return audio, sr


def normalize_audio(audio):

    normalized_audio = librosa.util.normalize(audio)

    return normalized_audio


def extract_mfcc(audio, sr, n_mfcc=40):

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=n_mfcc
    )

    mfcc_mean = np.mean(mfcc.T, axis=0)

    return mfcc_mean