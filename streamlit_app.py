import streamlit as st
import requests

st.title("🎙 VoiceGuard AI")
st.subheader("Deepfake Voice Detection System")

uploaded_file = st.file_uploader(
    "Upload Audio File",
    type=["wav", "mp3"]
)

if uploaded_file is not None:

    files = {
        "file": uploaded_file.getvalue()
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        files={"file": uploaded_file}
    )

    result = response.json()

    st.success(f"Prediction: {result['prediction']}")