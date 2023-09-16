import openai

# Set up your API key
api_key = "YOUR_API_KEY_HERE"
openai.api_key = api_key

def convert_text_to_qa(text):
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": text},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    return response.choices[0].message['content']

# Process the response into a Python dictionary
def process_response(response):
    qa_pairs = response.split('\n')
    questions = {}
    for i in range(0, len(qa_pairs)-1, 2):
        questions[qa_pairs[i]] = qa_pairs[i+1]
    return questions





def main(audio_transcript):
    text_to_convert = audio_transcript
    response = convert_text_to_qa(
        f"convert the following text into relevant and structured questions and answers in a python dict where the keys are the questions and the values are the answers\n\n{text_to_convert}")
    qa_dict = process_response(response)
    return qa_dict

