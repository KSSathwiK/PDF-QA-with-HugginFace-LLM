import streamlit as st
import random, time, os, requests
from huggingface_hub import InferenceClient
from pypdf import PdfReader
from dotenv import load_dotenv

upload_folder = 'uploaded_pdf_file'

# check if the folder is available or not
if not os.path.exists(upload_folder):
    os.mkdir(upload_folder)


st.header("upload PDF File and get answers from it")

uploaded_file = st.file_uploader("choose a pdf file .....", type=['pdf','PDF'])

if uploaded_file is not None:
    # get the file name and save path
    file_name = uploaded_file.name
    saved_path = os.path.join(upload_folder, file_name)

    # save the file to a local folder
    with open(saved_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f'PDF file has successfully uploaded to {saved_path}')


    reader = PdfReader(saved_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    # comment if you dont need to display the text
    st.write(text)

# Load environment variables from .env file
load_dotenv()

# Retrieve the Hugging Face API token
hf_token = os.getenv("HUGGING_FACE_API_TOKEN")

# Streamed response emulator
def response_generator(text, prompt):
    API_URL = "https://api-inference.huggingface.co/models/google-bert/bert-large-uncased-whole-word-masking-finetuned-squad"
    # Use the token in your headers
    headers = {"Authorization": f"Bearer {hf_token}"}

    payload = ({
        "inputs": {
        "question": prompt,
        "context": text
    },
    })
    response = requests.post(API_URL, headers=headers, json=payload)
    output = response.json()
    
    return output


st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    response = response_generator(text,prompt)
    with st.chat_message("assistant"):
        st.markdown(response['answer'])
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response['answer']})