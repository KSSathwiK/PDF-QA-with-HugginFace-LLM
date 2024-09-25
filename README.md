# PDF Question Answering App

This is a simple Streamlit application that allows users to upload a PDF file and ask questions based on its content. The application uses Hugging Face's API for question answering.

My model "google-bert-large-uncased-whole-word-masking-finetuned-squad".

## Features
- Upload a PDF file.
- Extract text from the PDF.
- Ask questions about the content of the PDF.
- Get answers powered by a Hugging Face model.

## Requirements

To run this application, you will need the following Python packages:

- `streamlit`
- `huggingface-hub`
- `pypdf`
- `python-dotenv`
- `requests`

You can install all the required packages by running:

```bash
pip install -r requirements.txt
