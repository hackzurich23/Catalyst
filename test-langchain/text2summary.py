"""
This script has an extractor object that extracts the bulletpoints from the 
chat messages.
"""
import os
import openai
import re 
import copy
import json


class Text2Summary():
    def __init__(self) -> None:
        pass

    def _clean_transcript(self, text):
        """
        This function cleans the transcript by removing the date, time, and
        participants from the transcript
        """
        relevant_text = copy.deepcopy(text)
        def remove_starting_substring(input_string, substring):
            regex_pattern = re.escape(substring) + r'.*?$'
            result = re.sub(regex_pattern, '', input_string)
            return result
    
        def remove_ending_substring(input_string, substring):
            # regex_pattern = r'.*?' + re.escape(substring) + r'$'
            # result = re.sub(regex_pattern, '', input_string)
            pattern = re.escape(substring) + r".*"
            result = re.sub(pattern, "", input_string)
            return result
        
        # Ignore the first auto-generated lines.
        autogen_text = "This editable transcript was computer generated and might contain errors. People can also change the text after it was created."
        relevant_text = remove_starting_substring(relevant_text, autogen_text)
        # Ignore the last auto-generated line.
        relevant_text = remove_ending_substring(relevant_text, "Meeting ended after")
    
        return relevant_text
    
    def _get_short_summary(self, prompt, model="gpt-3.5-turbo"):
        """
        This function outputs a list containing a very brief summary of
        the given text
        """

        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0, # this is the degree of randomness of the model's output
        )

        response = response.choices[0].message["content"]

        return response
    
    
    def get_meeting_summary(self, text_to_summarize) -> dict[str, str]:
        prompt = f"""You are given a transcript of a meeting. 
        You need to summarize the main ideas and facts from the following text delimited by
        three backticks. Rephrase each fact into a question and an answer. Save each question and answer
        as a Python dictionary where the key is the question and the value is the answer. 
        ```
        {self._clean_transcript(text_to_summarize)}
        ```
        """
        response = self._get_short_summary(prompt)
        try:
            response = json.loads(response)
        except Exception:
            print("ERROR MEETING SUMMARY FAILED IN JSON")
            response = {"error": "Could not summarize the meeting."}
        return response    
    
    
    def get_document_summary(self, text_to_summarize):
        prompt = f"""You are given a document of a cement manufacturing company. 
        You need to summarize the main ideas and facts from the following text delimited by
        three backticks. Rephrase each fact into a question and an answer. Save each question and answer
        as a Python dictionary where the key is the question and the value is the answer. 
        ```
        {text_to_summarize}
        ```
        """
        response = self._get_short_summary(prompt)
        try:
            response = json.loads(response)
        except Exception:
            print("ERROR DOCUMENT SUMMARY FAILED IN JSON")
            response = {"error": "Could not summarize the document."}
        return response



if __name__ == "__main__":
    from dotenv import load_dotenv
    dir_path = os.path.dirname(os.path.realpath(__file__))
    assert load_dotenv(dotenv_path=dir_path + "/../.env", override=True), "Could not load .env file"

    text2summary = Text2Summary()
    
    summary = text2summary.get_meeting_summary("""
        kmk-wovu-mzz (2023-09-16 08:30 GMT) - Transcript
        Attendees
        Martin Tefra
        Transcript
        This editable transcript was computer generated and might contain errors. People can also change the text after it was created.
        Martin Tefra: Okay, so I'm trying to speak and see how Google will react to that, maybe we need some more voices. Yeah. Okay, hi This is the first time meeting you nice spot.
        Martin Tefra: What else do I have to say? Maybe they both will think Still that. It's you because we're speaking from the same account. I wonder if Google is that smart too, the thing with voice. So it just doesn't Assigning the voice to accounts. Could be, but we're doing that without Google anyways. Right, we're using a third party model, but if it is of a better quality than worse, we tested it just like this is the meeting feature, maybe it's better than the one that we saw with GCP, but our house works. Also, if we just have an MP3 file, then we can use that. So, we just know more. Do you think I should Just close it and see if the meeting will get saved. Because theoretically, we can press the button after two minutes.
        Martin Tefra: He? Better know, whatever you want, okay?
        Martin Tefra: first of all,
        Martin Tefra: my God.
        Meeting ended after 00:02:55 👋
    """)
    
    print(summary)
    
    pass