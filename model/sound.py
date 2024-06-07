import sounddevice as sd
import numpy as np
import wave

def record_audio(duration, sample_rate=44100):
    print("Recording...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype=np.int16)
    sd.wait()
    print("Recording complete.")
    return recording

def save_audio(filename, recording, sample_rate=44100):
    print(f"Saving audio to {filename}...")
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)  # 2 bytes per sample
        wf.setframerate(sample_rate)
        wf.writeframes(recording.tobytes())
    print("Audio saved.")

if __name__ == "__main__":
    duration = 10  # seconds
    sample_rate = 44100  # Hz
    filename = "recorded_audio.wav"

    recording = record_audio(duration, sample_rate)
    save_audio(filename, recording, sample_rate)
