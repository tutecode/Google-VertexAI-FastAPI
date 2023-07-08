import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

vertexai.init(project="ghc-010", location="us-central1")
chat_model = ChatModel.from_pretrained("chat-bison@001")
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}
chat = chat_model.start_chat(
    context="""Nice person.""",
)
response = chat.send_message("""Hello. How are you?""", **parameters)
print(f"Response from Model: {response.text}")


# sudo pip3 install langchain