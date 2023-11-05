import streamlit as st

st.set_page_config(
    page_title="Streamlit Chatbots",
    page_icon="🤖",
)

st.title("Streamlit Chatbots")

st.markdown(
    """
    This is a multi-page Streamlit app with various examples of OpenAI chat bots.
    **👈 Select a demo from the sidebar** to see progressively more advanced chat bots!
    1. Basic AI Assistant: Input a prompt and recieve a single response.
    2. Streamed Response AI Assistant: Input a prompt and recieve a streamed response  
"""
)