# This program plays an audio file with pydub
# writes an audio file with librosa and pydub
# Using pandas, numpy, librosa, pydub
# Then draw a sine wave plot using matplotlib, seaborn
# Use numpy for numerical operations
import matplotlib.pyplot as plt
import librosa  # Install this with pip install librosa
import librosa.display
from pydub import AudioSegment  # Install this with pip install pydub
from pydub.playback import play
import os

print("Writing and Playing a wave file")

# Load an audio file
# Convert mp3 to wav
# Note: We must download ffmpeg and ffprobe 
# for this to work
# Simply write: brew install ffmpeg and brew install ffprobe

file_path = 'birdsinging.mp3'
audio = AudioSegment.from_mp3(file_path)
export_path = "birdsinging.wav"
audio.export(export_path, format="wav")
print("Converted mp3 to wav!!")
# Play the audio file
print("Playing the audio file...", file_path)
play(audio)

# Write the audio file with librosa
y, sr = librosa.load(export_path, sr=None)

# Total samples is the length of y, and sr is the sample rate
# Bits per sample is 16 for wav files
# Duration in seconds is len(y)/sr
print(f"Sample Rate: {sr} \nAudio Data Shape: {len(y)}")
print(f"Bits per sample: 16")
print(f"Duration: {len(y)/sr} seconds")

# Get the mb size of the audio file, and mb per second
file_size = os.path.getsize("birdsinging.wav") / (1024 * 1024)
print(f"File Size: {file_size:.2f} MB")
print(f"File Size per Second: {file_size / (len(y)/sr):.2f} MB/s")

# Get the Max and Min Amplitude
print(f"Max Amplitude: {max(y)}")
print(f"Min Amplitude: {min(y)}")

# Plot the waveform
plt.figure(figsize=(10,4))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

