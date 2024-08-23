import os
import speech_recognition as sr
from pydub import AudioSegment

# Set the path to your Google Cloud service account key file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/User/Downloads/workout-tracker-430104-feac8ecdba64.json"

# Initialize recognizer
recognizer = sr.Recognizer()

# Path to your audio file
audio_file = "20 Aug Spar (online-audio-converter.com).wav"


# Function to split audio into chunks
def split_audio(audio_file, chunk_length_ms=60000):
    audio = AudioSegment.from_wav(audio_file)
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    return chunks


# Function to transcribe audio chunks starting from a specific chunk index
def transcribe_chunks(chunks, start_chunk=0):
    for i in range(start_chunk, len(chunks)):
        chunk = chunks[i]
        chunk_file = f"chunk_{i}.wav"
        chunk.export(chunk_file, format="wav")

        with sr.AudioFile(chunk_file) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google_cloud(audio_data)
                print(f"Chunk {i} transcription:")
                print(text)
            except sr.UnknownValueError:
                print(f"Chunk {i} could not be understood")
            except sr.RequestError as e:
                print(f"Chunk {i} could not request results; {e}")


# Split the audio file into chunks
chunks = split_audio(audio_file)

# Transcribe chunks starting from chunk 21
transcribe_chunks(chunks, start_chunk=0)
