
import streamlit as st
import pandas as pd
import numpy as np

st.title('¿Aprueba ChatGPT el examen MIR 2023?')

DATE_COLUMN = 'date/time'
DATA_FILE = 'streamlit/final_results.csv'

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)

@st.cache
def load_data():
    data = pd.read_csv(DATA_FILE)
    return data

def write_correct_question(answers, correct, explanation):
    for i, aux_answer in enumerate(answers):
        if i+1 == correct:
            st.markdown(f'- **:green[{aux_answer}]**')
        else:
            st.markdown(f'- {aux_answer}')
    st.markdown(f'Explicación: *{explanation}*')

def write_wrong_question(answers, correct, answer, explanation):
    for i, aux_answer in enumerate(answers):
        if i+1 == correct:
            st.markdown(f'- **:green[{aux_answer}]**')
        elif i+1 == answer:
            st.markdown(f'- **:red[{aux_answer}]**')
        else:
            st.markdown(f'- {aux_answer}')
    st.markdown(f'Explicación: *{explanation}*')

data = load_data()

st.header('Preguntas: ')

for i, row in data.iterrows():
    correct_answer = row['correct answer']
    answer = row.answer
    evaluation = row.evaluation
    answers = [row[1], row[2], row[3], row[4]]
    justification = row['justificacion']
    justification = justification.strip('\'\"}\.') + '.'
    st.subheader(f'{i+1}) {row.question}')
    if evaluation:
        write_correct_question(answers, correct_answer, justification)
    else:
        write_wrong_question(answers, correct_answer, answer, justification)
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:20px;
    }
    </style>
    ''', unsafe_allow_html=True)