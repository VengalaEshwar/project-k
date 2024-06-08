from pydub import AudioSegment
from pydub.playback import play
import os

# Path to the OPUS file
file_path = "D:\\coding\\temp\\project-rtrp\\model\\others\\test_case_1.opus"

# Check if the file exists
if os.path.exists(file_path):
    try:
        # Load the OPUS file
        audio = AudioSegment.from_file(file_path, format="opus")
        
        # Play the audio file
        play(audio)
        
    except Exception as e:
        print(f"Error: {e}")
else:
    print(f"File not found: {file_path}")
