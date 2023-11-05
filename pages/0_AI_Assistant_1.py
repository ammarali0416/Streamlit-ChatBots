# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    0_AI_Assistant_1.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ammar syed ali <https://www.linkedin.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/05 02:34:10 by ammar syed        #+#    #+#              #
#    Updated: 2023/11/05 02:34:10 by ammar syed       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


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


def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt, #
        max_tokens=1024,
        n=1, # number of completions to generate in each prompt (MORE THAN ONE CAN GET EXPENSIVE)
        stop = None, # up to 4 sequences where the API will stop generating tokens
        temperature=1
    )

    message = completions.choices[0].text
    return message

st.set_page_config(
    page_title="AI Assistant 1: Input and recieve a basic response"
)

st.title("AI Assistant 1: Input and recieve a basic response")
#st.sidebar.success("Select a demo.")


prompt = st.text_input("Enter your message:", key="prompt") # the text input widget

if st.button("Submit", key="submit"):
    st.markdown("---------")
    res_box = st.empty()
    response = generate_response(prompt)
    res_box.write(response)
