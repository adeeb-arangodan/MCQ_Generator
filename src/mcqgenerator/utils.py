import pandas as pd
import PyPDF2

def get_table_data(mcq_json):
    questions = []
    for index, item in mcq_json.items():
        mcq = item['mcq']
        options = ' | '.join(
            [f"{option}: {option_value}" for option, option_value in item['options'].items()]
        )
        correct_answer = item['correct_answer']
        questions.append({
            'mcq': mcq,
            'options': options,
            'answer': correct_answer
        })
    questions_df = pd.DataFrame(questions)    
    return questions_df


def read_data_from_file(file):
    if file.name.endswith('.pdf'):
        try:
            return read_pdf_file(file)
        except:
            raise Exception("Error reading pdf file")
    elif file.name.endswith('.txt'):
        try:
            return file.read().decode('UTF-8')
        except:
            raise Exception("Error reading text file")
    else:
        raise Exception('Unsupported file format')


def read_pdf_file(file):
    text = ""
    pdf_reader = PyPDF2.PdfFileReader(file)
    for page in pdf_reader.pages:
        text += page.extract_text()
        return text