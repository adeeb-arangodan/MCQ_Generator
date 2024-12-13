from dotenv import load_dotenv
import os
from src.mcqgenerator.logger import logging

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_community.callbacks import get_openai_callback


KEY = os.getenv('OPENAI_API_KEY')
print(f'Key: {KEY}')
logging.info('Initializing openai')
llm = ChatOpenAI(openai_api_key=KEY, model_name='gpt-3.5-turbo', temperature=.7)


quiz_generation_template = '''You are a quiz master bot. You are provided with a Input Text. 
You need to generate {number} question quiz based on the provided text for {subject} students. You need to 
set the difficulty level to {tone} level. The output should be in JSON Format as specified at the end of the prompt 

INPUT TEXT: {text}

Use the above input text to generate quiz and produce the output in JSON Format as shown below.

### OUTPUT JSON Format: 
{json_format}
'''

prompt_template = PromptTemplate(
    input_variables=['number','subject', 'tone', 'text', 'json_format'],
    template=quiz_generation_template
)

logging.info('Generating quiz chain')
quiz_chain = LLMChain(llm=llm, prompt=prompt_template, output_key='quiz_content', verbose=True)

review_template = '''You are a English grammerian and writer. Read the quizzes input in {quiz_content} and analyze the complexity of the question for {subject} student.
If you think, the question doesn't meet the expectations, update the question, options and correct answer accordingly. Make sure the content is from the actual input text.
Please write a short review of the mcq in one paragraph.
'''

prompt_template_review = PromptTemplate(
    input_variables=['quiz_content', 'subject'],
    template=review_template
)

logging.info('Generating review chain')
review_chain = LLMChain(llm=llm, prompt=prompt_template_review, output_key='review', verbose=True)

logging.info('Initializing sequencial chain')
sequential_chain = SequentialChain(chains=[quiz_chain, review_chain], input_variables=['number','subject', 'tone', 'text', 'json_format'],
                                    output_variables=['quiz_content','review'])

