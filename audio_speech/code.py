import nltk
from nltk.tokenize import word_tokenize
import underthesea
from langdetect import detect
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import librosa  # Install this with pip install librosa
import librosa.display
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

text = input("Enter any text: ")

# Detect the language of the text to apply suitable word tokenization
if detect(text) == 'vi':
    tokens = underthesea.word_tokenize(text)
else:
    tokens = word_tokenize(text)
print(tokens)


# Generate speech
export_path = "output.mp3"
tts = gTTS(text=text, lang=detect(text))
tts.save(export_path)
sound = AudioSegment.from_mp3(export_path)


y, sr = librosa.load(export_path, sr=None)

print(f"Sample Rate: {sr} \nAudio Data Shape: {len(y)}")
print(f"Bits per sample: 16")
print(f"Duration: {len(y)/sr} seconds")
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

mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)

plt.figure(figsize=(10, 4))
librosa.display.specshow(mel_spectrogram_db, sr=sr, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel-frequency spectrogram')
plt.tight_layout()
plt.show()

f0, voiced_flag, voiced_prob = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
print("F0:", f0)
print("Voiced Flag:", f0)
print("Voiced Prob:", f0)

plt.figure(figsize=(12, 4))
times = librosa.times_like(f0)
plt.plot(times, f0, label='Pitch (Hz)')
plt.title('Pitch Contour')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.ylim(0, np.nanmax(f0)+50)
plt.show()