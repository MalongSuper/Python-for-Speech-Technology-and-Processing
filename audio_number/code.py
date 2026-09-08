
from pydub import AudioSegment
from pydub.playback import play
import librosa
import librosa.display
import matplotlib.pyplot as plt


speakers = {'1': 's01', '2': 's02', '3': 's03', '4': 's04', '5': 's05', '6': 's06', '7': 's07', '8': 's08', 
            '9': 's09', '10': 's10', '11': 's11', '12': 's12', '13': 's13', '14': 's14', '15': 's15', '16': 's16'}

numbers_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', 
                '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}


# Input are strings 
number_input = list(input("Enter number: "))

if any([i not in numbers_dict.keys() for i in number_input]):
    print("Invalid Input")

else:
    audio_number = []
    # Convert the input to number
    converted = [numbers_dict[i] for i in number_input]
    print("Convered to:", converted)
    # We will allow the user to select which speaker they want to hear
    s = input("Select Speaker (1 to 16): ")
    if s not in speakers.keys():
        print("Invalid Input")
    else:
        print("Speaker:", speakers[s])
        for k in converted:
            sound = AudioSegment.from_file(f"Project_AudioNumber/digits/{speakers[s]}/{k}.wav", 
                                           format="wav")
            audio_number.append(sound) # Append to list
	# The sum() function will concatenate the sound files
	# to create a full audio
    audio = sum(audio_number)
    play(audio)

# Export the audio file
export_path = "audio.wav"
audio.export("audio.wav", format="wav")

