import requests
import PyPDF2
import re

CHUNK_SIZE = 1024


# Function to get text from the PDF using PyPDF2 and convert it for the VoiceAI
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(open(pdf_file, 'rb'))
    cleaned_text = '' 
    for page in pdf_reader.pages:
        raw_text = page.extract_text().strip().replace('\n', ' ')
        cleaned_text += raw_text + ' '
    # Remove any additional whitespace
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    #Add pauses for improvement in quality speech
    cleaned_text = cleaned_text.replace('.', '.\n')
    return cleaned_text


pdf_file = "Pyramids_Info_Fixed.pdf" 
text1 = extract_text_from_pdf(pdf_file) # For the pdf 
text = "Eyad is the next Tony Stark" # For testing purposes
model_id = "eleven_monolingual_v1"
url = "https://api.elevenlabs.io/v1/text-to-speech/voice_id"
api_key = "api_key"

def text_to_speech(text, model_id, url, api):
    # Provided from Eleven Labs 
    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": api_key
    }

    data = {
    "text": text,
    "model_id": model_id,
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
    }

    response = requests.post(url, json=data, headers=headers)
    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

text_to_speech(text, model_id, url, api_key)