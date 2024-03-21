import streamlit as st
from transformers import pipeline
import librosa
import soundfile as sf

# Load sentiment analysis model
classifier = pipeline('sentiment-analysis')

def text_analysis():
    st.title("Text Analysis")
    st.write("Enter text below to analyze its sentiment.")

    # Text input from user
    user_input = st.text_input("Enter text here:")

    # Button to trigger sentiment analysis
    if st.button("Analyze Text"):
        if user_input:
            # Perform sentiment analysis
            result = classifier(user_input)[0]

            # Display the sentiment
            st.write("Sentiment:", result['label'])
            st.write("Confidence:", result['score'])
        else:
            st.warning("Please enter some text to analyze.")

def audio_analysis():
    st.title("Audio Analysis")
    st.write("Upload an audio file below to analyze its emotion.")

    # Audio upload from user
    uploaded_file = st.file_uploader("Upload audio file", type=["mp3", "wav"])

    # Button to trigger audio analysis
    if st.button("Analyze Audio"):
        if uploaded_file is not None:
            # Save the uploaded file locally
            with open("temp_audio_file.wav", "wb") as f:
                f.write(uploaded_file.getvalue())

            # Load the audio file and extract features
            audio_data, _ = librosa.load("temp_audio_file.wav", sr=16000)
            sf.write("temp_audio_file.wav", audio_data, 16000)

            # Perform emotion analysis
            audio_results = classifier("temp_audio_file.wav")

            # Display the emotions and their scores
            st.write("Emotions:")
            for result in audio_results:
                for emotion, score in result.items():
                    st.write(f"{emotion}: {score}")
        else:
            st.warning("Please upload an audio file to analyze.")

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Text Analysis", "Audio Analysis"])

    if selection == "Text Analysis":
        text_analysis()
    elif selection == "Audio Analysis":
        audio_analysis()

if __name__ == "__main__":
    main()
