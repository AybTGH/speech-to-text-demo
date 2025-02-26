import speech_recognition as sr
import numpy as np
from mutagen.flac import FLAC

# AUDIO_FILE = "data/FR/00c2529e-9705-464e-bbc2-acbe19916095.wav"  
# TRANSCRIPT_FILE = "data/FR/00c2529e-9705-464e-bbc2-acbe19916095.txt"  
AUDIO_FILE = "data/FR/0a0bc3af-7e7b-4396-ba6b-8c9e112cb926.flac"  
TRANSCRIPT_FILE = "data/FR/0a0bc3af-7e7b-4396-ba6b-8c9e112cb926.txt" 

def flac_to_pcm(audio_path):
    """Extract PCM data from FLAC using mutagen."""
    audio = FLAC(audio_path)

    # FLAC does not return raw PCM, so we extract the audio data
    sample_rate = audio.info.sample_rate
    channels = audio.info.channels
    bits_per_sample = audio.info.bits_per_sample

    print(f"Sample Rate: {sample_rate} Hz, Channels: {channels}, Bits per Sample: {bits_per_sample}")

    # Convert FLAC to PCM bytes (mutagen does not provide this directly, so we use another method)
    with open(audio_path, "rb") as f:
        pcm_data = f.read()  # Read the raw FLAC data

    return pcm_data, sample_rate

def speech_to_text(audio_path):
    """Convert FLAC speech to text."""
    recognizer = sr.Recognizer()

    # Decode FLAC audio to PCM
    pcm_audio, sample_rate = flac_to_pcm(audio_path)

    # Convert PCM bytes to recognizer's format
    audio = sr.AudioData(pcm_audio, sample_rate=sample_rate, sample_width=2)

    with sr.AudioFile(audio_path) as source:
        print("Processing audio...")
        audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language="fr-FR")  # French
            return text
        except sr.UnknownValueError:
            return "Speech Recognition could not understand the audio"
        except sr.RequestError:
            return "Could not request results, check your internet connection"

def load_transcript(transcript_path):
    """Load actual transcript"""
    with open(transcript_path, "r", encoding="utf-8") as file:
        return file.read().strip()

if __name__ == "__main__":
    # Run Speech-to-Text
    predicted_text = speech_to_text(AUDIO_FILE)

    # Load Actual Transcript
    actual_text = load_transcript(TRANSCRIPT_FILE)

    # Display Results
    print("\n🔹 Predicted Text:\n", predicted_text)
    print("\n✅ Actual Transcript:\n", actual_text)

    # Compare
    if predicted_text.lower() == actual_text.lower():
        print("\n🎉 Perfect match!")
    else:
        print("\n⚠️ Differences found. Check manually.")
