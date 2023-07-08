import streamlit as st
from streamlit_chat import message
#import vertexai
from google.cloud import aiplatform
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"

st.title("PaLM Tutorial")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Say something to get started!"}]

# Initialize Vertex AI
aiplatform.init(project="ghc-010", location="us-central1")
chat_model = ChatModel.from_pretrained("chat-bison@001")
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}
chat = chat_model.start_chat(context="Nice person.")

with st.form("chat_input", clear_on_submit=True):
    a, b = st.columns([4, 1])

    user_prompt = a.text_input(
        label="Your message:",
        placeholder="Type something...",
        label_visibility="collapsed",
    )

    b.form_submit_button("Send", use_container_width=True)


for msg in st.session_state.messages:
    message(msg["content"], is_user=msg["role"] == "user")  # display message on the screen

if user_prompt:

    st.session_state.messages.append({"role": "user", "content": user_prompt})
    
    message(user_prompt, is_user=True)

    response = chat.send_message(user_prompt, **parameters)  # get response from Vertex AI chat model

    msg = {"role": "assistant", "content": response.text}  # we are using dictionary to store message and its role. It will be useful later when we want to display chat history on the screen, to show user input at the left and AI's right side of the screen.

    st.session_state.messages.append(msg)  # add message to the chat history

    message(msg["content"])  # display message on the screen


def clear_chat():
    st.session_state.messages = [{"role": "assistant", "content": "Say something to get started!"}]

if len(st.session_state.messages) > 1:
    st.button('Clear Chat', on_click=clear_chat)


# 👇️ installs Google Vertex AI
#pip install google-cloud-aiplatform