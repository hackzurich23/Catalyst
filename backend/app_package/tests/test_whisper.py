import os
import requests
from pydub import AudioSegment
import tempfile


API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large"
headers = {"Authorization": "Bearer hf_............."}


def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


def query_long(filename):
    """Query file longer than 30s."""
    
    audio = AudioSegment.from_mp3(filename)
    sec_30 = 30 * 1000  # PyDub handles time in milliseconds
    full_output = ""
    
    for time_start in range(0, len(audio), sec_30):
        end_time = min(time_start+sec_30, len(audio))
        audio_segment = audio[time_start:end_time]
        with tempfile.TemporaryDirectory() as tmpdirname:
            audio_segment.export(os.path.join(tmpdirname, "audio_segment.mp3"), format="mp3")
            output = query(os.path.join(tmpdirname, "audio_segment.mp3"))
            full_output = full_output + " " + output["text"]
            
    return full_output

# output = query("sample1.mp3")
output = query_long("sample1.mp3")

print(output)