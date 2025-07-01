import whisper
import sounddevice as sd
import numpy as np
import tempfile
import os
import scipy.io.wavfile

model = whisper.load_model("base")  # Downloads on first run

def record_audio(duration=5, fs=16000):
    print("[VOICE] Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    return recording, fs

def save_temp_wav(audio, fs):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        scipy.io.wavfile.write(f.name, fs, audio)
        return f.name

def listen_and_transcribe():
    try:
        audio, fs = record_audio()
        wav_path = save_temp_wav(audio, fs)
        print(f"[VOICE] Transcribing {wav_path}...")
        result = model.transcribe(wav_path)
        os.remove(wav_path)
        return result["text"]
    except Exception as e:
        return f"[Error] {e}"
