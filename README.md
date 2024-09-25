# PDF Question Answering App

This is a simple Streamlit application that allows users to upload a PDF file and ask questions based on its content. The application uses Hugging Face's API for question answering.

My model "google-bert-large-uncased-whole-word-masking-finetuned-squad".

## Features
- Upload a PDF file.
- Extract text from the PDF.
- Ask questions about the content of the PDF.
- Get answers powered by a Hugging Face model.

## Environment Variables

You'll need to create a `.env` file in the root of the project directory with your Hugging Face API token:

```
HF_API_TOKEN=your_huggingface_api_token_here
```

## Running the App

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Activate on Windows
   venv\Scripts\activate
   # Activate on macOS/Linux
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
