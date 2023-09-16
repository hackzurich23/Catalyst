
######## MY BULLSHIT CODE #######
# TODO: extract Q&As from the wiki files
# Function to read the content of a text file
# def read_text_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return file.read()


# Function to append data to an existing CSV file
# def append_to_csv(file_path, data):
#     with open(file_path, 'a', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(data)


# def extract_q_and_a_from_wiki_pages():
#     template_for_database = """
#     You are a developer of a database for machine learning.
#     I will share a company's knowledge data (wiki-pages) with you. You will give me a csv file that consists of
#     two columns: the first one is a question, and the second one is an answer to this question (it must be a Q&A or
#     an FAQ database). You should extract as many questions-answer pairs as possible from the given text and you will
#     follow ALL of the rules below:
#
#     1/ You should extract as many questions as possible from the provided text
#
#     2/ Each answer to the extracted questions should include the name of the source of this information
#     (file name and, if provided, research title and author)
#
#     3/ As the output, you provide the csv file content exclusively, no additional information!
#
#     4/ Do not include the header of the csv file ("Question,Answer" line) into the output
#
#     5/ use a pipeline '|' as a delimiter
#
#     Below is text from which you should extract Q&As:
#     {text}
#
#     Here is a the file name:
#     {file_name}
#
#     Please provide ONLY the content of csv file with the extracted question-answer pairs as your answer
#     """
#
#     prompt_for_database = PromptTemplate(
#         input_variables=["text", "file_name"],
#         template=template_for_database
#     )
#
#     chain_for_database = LLMChain(llm=llm, prompt=prompt_for_database)
#
#     # Define the directory where your text files are located
#     wiki_files_directory = 'wiki_files'
#     output_csv_file = 'generated_q_and_a.csv'
#
#     # Iterate through the files in the directory
#     for filename in os.listdir(wiki_files_directory):
#         if filename.endswith('.txt'):
#             # Construct the full file path
#             file_path = os.path.join(wiki_files_directory, filename)
#
#             # Read the content of the text file
#             text_content = read_text_file(file_path)
#
#             # Call the chain_for_database.run function with the text content and filename
#             response = chain_for_database.run(text=text_content, file_name=filename)
#             print(response)
#             # Extract the CSV data from the response (replace this with the actual way to extract data)
#             data_lines = response.strip().split('\n')
#
#             csv_file = 'generated_q_and_a.csv'
#             with open(csv_file, 'a', newline='', encoding='utf-8') as file:
#                 # Create a CSV writer
#                 csv_writer = csv.writer(file, delimiter='|')
#                 for line in data_lines:
#                     if not 'Question|Answer' in line:
#                         try:
#                             # Split each line into question and answer
#                             data_line = line.split('|')
#
#                             # Write the question and answer to the CSV file
#                             csv_writer.writerow(data_line)
#                         except:
#                             print('we are not adding the line: ' + line)
#


import csv
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

def modify_csv():
    input_file = "generated_q_and_a.csv"
    output_file = "generated_q_and_a_correct.csv"

    with open(input_file, mode="r", newline="") as csv_file, open(output_file, mode="w", newline="") as output_csv_file:
        csv_reader = csv.reader(csv_file)
        csv_writer = csv.writer(output_csv_file, quoting=csv.QUOTE_MINIMAL)

        for row in csv_reader:
            if len(row) >= 2:
                # Combine everything after the first comma and wrap it in double quotes
                row = [row[0], '"' + ','.join(row[1:]) + '"']
            csv_writer.writerow(row)

    print(f'CSV file "{input_file}" has been modified and saved as "{output_file}".')
    
if __name__ == "__main__":
    # modify_csv()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    assert load_dotenv(dotenv_path=dir_path + "/../.env", override=True), "Could not load .env file"

    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    loader = CSVLoader(file_path="test-langchain/generated_q_and_a_correct.csv")
    documents = loader.load()
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    db = FAISS.from_documents(documents, embeddings)
    pass