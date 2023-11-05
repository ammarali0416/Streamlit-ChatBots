import openai
import streamlit as st
import os
from dotenv import load_dotenv

# Get the path to the directory this file is in
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

# Connect the path with your '.env' file name located one level above
BASEDIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
load_dotenv(os.path.join(BASEDIR, '.env'))
openai.api_key = os.getenv('OPENAI_API_KEY')

st.title("AI Assistant 2: Stream the response like real ChatGPT")

prompt = st.text_input("Enter your message:", key="prompt") # the text input widget

if st.button("Submit", type="primary"):
    st.markdown("----")
    res_box = st.empty()
    report = []
    for resp in openai.Completion.create(model='text-davinci-003',
                                        prompt=prompt,
                                        max_tokens=500, 
                                        temperature = 1,
                                        stream = True):
        # join method to concatenate the elements of the list 
        # into a single string, 
        # then strip out any empty strings
        report.append(resp.choices[0].text)
        result = "".join(report).strip()
        result = result.replace("\n", "")        
        res_box.markdown(f'*{result}*')

st.markdown("----")



