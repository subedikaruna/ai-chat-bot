
import os
import streamlit as st
from openai import OpenAI

# Initialize Ollama client
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

# Configure Streamlit page
st.set_page_config(
    page_title="Local AI Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# App title
st.title("Local AI Chatbot")
st.caption("Powered by Ollama and Qwen 2.5")

# Display previous messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_prompt = st.chat_input("Ask me anything...")

if user_prompt:
    # Add and display user message
    st.session_state.chat_history.append(
        {"role": "user", "content": user_prompt}
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    try:
        # Get response from local Ollama model
        response = client.chat.completions.create(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                *st.session_state.chat_history
            ]
        )

        assistant_response = response.choices[0].message.content

        if assistant_response is None:
            assistant_response = "Sorry, I couldn't generate a response."

        # Save and display assistant response
        st.session_state.chat_history.append(
            {"role": "assistant", "content": assistant_response}
        )

        with st.chat_message("assistant"):
            st.markdown(assistant_response)

    except Exception as e:
        st.error(f"An error occurred: {e}")