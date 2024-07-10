import streamlit as st
import os
import dotenv
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from pydantic import BaseModel
import json
import re
import pandas as pd

# Define the Pydantic model
class ServiceIssue(BaseModel):
    service_name: str
    exceptions: str
    root_cause: str
    remedial_actions: str

def load_text(file):
    return file.read().decode('utf-8')

def parse_response(text):
    data = {
        'service_name': '',
        'exceptions': '',
        'root_cause': '',
        'remedial_actions': ''
    }
    patterns = [
        (r"1\. Main application or service name: (.+?)(?=\n\d|\Z)", 'service_name'),
        (r"2\. Exceptions occurred: (.+?)(?=\n\d|\Z)", 'exceptions'),
        (r"3\. Root cause for the failure: (.+?)(?=\n\d|\Z)", 'root_cause'),
        (r"4\. Remedial Actions:\s*(.+?)(?=\n\d|\Z)", 'remedial_actions')
    ]
    for pattern, key in patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            data[key] = match.group(1).strip()
    return data

def main():
    # Custom CSS to inject into Streamlit's HTML to change the sidebar color
    st.markdown(
        """
        <style>
        /* More general selector for sidebar using data-testid attribute */
        div[data-testid="stSidebar"] {
            background-color: #007BFF;  /* Set to a blue color */
            color: #ffffff;
        }
        /* Optional: Adjust sidebar link/text color */
        div[data-testid="stSidebar"] .stButton > button {
            color: #ffffff;
            background-color: #0056b3;
        }
        div[data-testid="stSidebar"] a {
            color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Log File Analysis Tool")
    uploaded_file = st.file_uploader("Choose a log file (.txt)", type=['txt'])
    if uploaded_file is not None:
        text_content = load_text(uploaded_file)
        prompt_template = PromptTemplate.from_template("""
            Analyze the following logs to determine the main application or service experiencing the issue:
            {text_content}
            Please provide:
            1. Main application or service name
            2. Exceptions occurred
            3. Root cause for the failure
            4. Remedial Actions
        """)
        prompt_text = prompt_template.format(text_content=text_content)
        llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
        response = llm.invoke(prompt_text)
        response_text = response.content if hasattr(response, 'content') else ""
        response_data = parse_response(response_text)
        issue = ServiceIssue(**response_data)
        data = {
            "Service Name": [issue.service_name],
            "Exceptions": [issue.exceptions],
            "Root Cause": [issue.root_cause],
            "Remedial Actions": [issue.remedial_actions]
        }
        df = pd.DataFrame(data)
        st.table(df)

if __name__ == '__main__':
    load_dotenv()
    main()
