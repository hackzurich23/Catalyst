import requests
import os

X_GLADIA_KEY = "1291550f-6f62-4f66-a10e-337fbac31028"

def query(file_path):
    
    file_name, file_extension = os.path.splitext(file_path) 
    with open(file_path, 'rb') as f:  
        files = {
            # 'audio_url': (None, 'sample1.mp3'),
            # 'audio_url': (None, 'http://files.gladia.io/example/audio-transcription/split_infinity.wav'),
            'audio': (file_name, f, 'audio/'+file_extension[1:]),
            'language_behaviour': (None, 'automatic single language'),
            'toggle_diarization': (None, 'true'),
        }
        response = requests.post(
            'https://api.gladia.io/audio/text/audio-transcription/', 
            headers={
            'x-gladia-key': X_GLADIA_KEY,
            }, 
            files=files
        )

    # Unpack the response.
    convo_prediction = response.json()["prediction"]
    convo_prediction_raw = response.json()["prediction_raw"]
    transcriptions = [_["transcription"] for _ in convo_prediction]
    speaker_order = [_["speaker"] for _ in convo_prediction_raw["speaker_mapping"]]

    convo_list = []

    crt_speaker = None
    crt_speaker_text = ""
    for i, (text, speaker) in enumerate(zip(transcriptions, speaker_order)):
        # New speaker or still the same speaker.
        if crt_speaker is None or crt_speaker == speaker:
            crt_speaker_text += text + " "
            crt_speaker = speaker
        # Speaker changed.
        else:
            convo_list.append((crt_speaker, crt_speaker_text))
            crt_speaker = None
            crt_speaker_text = ""
        # If the convo is over.
        if i == len(speaker_order) - 1:
            crt_speaker_text += text + " "
            convo_list.append((speaker, crt_speaker_text))
        
    return convo_list
    
    
if __name__ == '__main__':
    output = query("sample2.mp3")

    print(output)
    
{
    "question": "answer",
}