# This project focus on create various types of sounds
from pydub import AudioSegment
from pydub.generators import Sine, Square, WhiteNoise
from pydub.playback import play
import numpy as np
from scipy.signal import butter, lfilter

sine_wave = Sine(440).to_audio_segment(duration=2000)  # 440Hz, 2s
square_wave = Square(330).to_audio_segment(duration=2000)  # 330Hz, 2s
noise = WhiteNoise().to_audio_segment(duration=2000)  # White noise, 2s
print("Playing Sine Wave...")
play(sine_wave)
print("Playing Square Wave...")
play(square_wave)
print("Playing Noise...")
play(noise)


# Print metadata (duration, frame rate, channels, etc.)
print("Sine Wave:", sine_wave.duration_seconds, "seconds,", sine_wave.frame_rate, "Hz,", sine_wave.channels, "channel(s)")
print("Square Wave:", square_wave.duration_seconds, "seconds,", square_wave.frame_rate, "Hz,", square_wave.channels, "channel(s)")
print("Noise:", noise.duration_seconds, "seconds,", noise.frame_rate, "Hz,", noise.channels, "channel(s)")


# Export to files
sine_wave.export("sine_wave.wav", format="wav")
square_wave.export("square_wave.wav", format="wav")
noise.export("noise.wav", format="wav")
print("Exported sine_wave.wav, square_wave.wav, noise.wav")


# Combine the sounds
combined = sine_wave + square_wave + noise 
# Play it
print("Playing Combined...")
play(combined)

# Metadata of this file
print("Combined:", combined.duration_seconds, "seconds,", combined.frame_rate, "Hz,", combined.channels, "channel(s)")
combined.export("combined.wav", format="wav")

# Increase the sound amplitude
# Increase the combined to 20 dB
louder_combined1 = combined + 20
print("Playing Louder Combined 1...")
play(louder_combined1)
# Increase each component to 20 dB
louder_combined2 = (sine_wave + 20) + (square_wave + 20) + (noise + 20) 
print("Playing Louder Combined 2...")
play(louder_combined2)
# This does not increase the sound amplitude, but loops the audio
loop_combined = (sine_wave * 2) + (square_wave * 2) + (noise * 2) 
print("Playing Loop Combined...")
play(loop_combined)

# Export these files
louder_combined1.export("louder_combined1.wav", format="wav")
louder_combined2.export("louder_combined2.wav", format="wav")
loop_combined.export("loop_combined.wav", format="wav")

# Audio Filtering
low_passed = combined.low_pass_filter(1000)   # Cut above 1kHz
high_passed = combined.high_pass_filter(1000) # Cut below 1kHz
print("Playing low-pass filtered...")
play(low_passed)
print("Playing high-pass filtered...")
play(high_passed)

low_passed.export("low_passed.wav", format="wav")
high_passed.export("high_passed.wav", format="wav")


# Using numpy
samples = np.array(combined.get_array_of_samples())
sample_rate = combined.frame_rate


def butter_lowpass_filter(data, cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return lfilter(b, a, data)

# Apply the function
filtered_samples = butter_lowpass_filter(samples, cutoff=1000, fs=sample_rate)

# Using NumPy to rebuild the audio segment
filtered_audio = AudioSegment(
    filtered_samples.astype(np.int16).tobytes(),
    frame_rate=sample_rate,
    sample_width=2,  # 16-bit audio
    channels=1)

# Play the audio
play(filtered_audio)

# Export the file
filtered_audio.export("filtered_output.wav", format="wav")

