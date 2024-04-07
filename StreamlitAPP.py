import streamlit as st
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
import json
import pandas as pd
import PyPDF2


st.title('MCQ Generator')

with open("/Users/sanchitsetia/mcqgen/Response.json", "r") as file:
    RESPONSE_JSON = json.load(file)
with st.form("MCQ Generator"):
    file = st.file_uploader("Upload a file for MCQ")

    numberOfQuestions = st.text_input("Enter number of questions")
    Subject = st.text_input("Enter subject for Quiz")
    tone = st.text_input("Enter tone for the quiz")

    submitted = st.form_submit_button("Create MCQ")
    if submitted:
        if(file.name.endswith(".txt")):
            file_contents = file.read()
        if(file.name.endswith(".pdf")):
            pdf_reader = PyPDF2.PdfReader(file)
            file_contents = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                file_contents += page.extract_text()
        response = generate_evaluate_chain({
            "text": file_contents,
            "number": numberOfQuestions,
            "subject":Subject,
            "tone": tone,
            "response_json": json.dumps(RESPONSE_JSON)})
        quiz = response.get('quiz')
        quiz= json.loads(quiz)
        quiz_table_data = []
        for key, value in quiz.items():
            mcq = value["mcq"]
            options = " | ".join(
            [
            f"{option}: {option_value}"
            for option, option_value in value["options"].items()
            ]
            )
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
        quiz=pd.DataFrame(quiz_table_data)
        st.write(quiz)
