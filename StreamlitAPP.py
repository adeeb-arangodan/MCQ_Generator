import streamlit as st
import json
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.MCQGenerator import sequential_chain
from src.mcqgenerator.utils import read_data_from_file, get_table_data
from src.mcqgenerator.logger import logging
from dotenv import load_dotenv
import traceback

json_format_string=''
JSON_FORMAT_FILE_PATH = './mcq_format.json'
with open(JSON_FORMAT_FILE_PATH) as file:
    json_format_string = json.load(file)

logging.info('loading environment variable')
load_dotenv()

with st.form('Input_Form'):
    data_file = st.file_uploader('Upload the data file: ')
    number = st.number_input('Number of MCQ: ', min_value=3, max_value=10)
    subject = st.text_input('Subject of MCQ: ', max_chars=15)
    tone = st.text_input('Difficulty level of MCQ', placeholder='Simple', max_chars=15)
    submit_button = st.form_submit_button("Generate MCQ")

if submit_button and data_file is not None and number and subject and tone:
    with st.spinner('Loading'):
        try:
            text = read_data_from_file(data_file)
            response = None
            with get_openai_callback() as callback:
                response = sequential_chain.invoke(          
                    {
                        'number': number,
                        'subject': subject, 
                        'tone': tone, 
                        'text': text,
                        'json_format': json_format_string
                    }
                )
            

        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
            st.error("Error")

        else:
            print(f'Prompt Tokens:{callback.prompt_tokens}')
            print(f'Completion Tokens:{callback.completion_tokens}')
            print(f'Total Cost:{callback.total_cost}')

            mcq_json = json.loads(response["quiz_content"])
            questions_df = get_table_data(mcq_json)
            st.table(questions_df)

            review = response["review"]
            st.text_area(label='Review', value=review)
       

       



        

        
