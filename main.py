import PyPDF2
from gtts import gTTS 
import re

# Open and read the PDF
pdf_file = "Pyramids_Info_Fixed.pdf"
pdf_reader = PyPDF2.PdfReader(open(pdf_file, 'rb'))

all_text = ''
for page in pdf_reader.pages:
    raw_text = page.extract_text().strip().replace('\n', ' ')
    all_text += raw_text + ' '

all_text = re.sub(r'\s+', ' ', all_text)
all_text = all_text.replace('.', '.\n')

print(all_text)

output_file = "audio.mp3"
tts = gTTS(text=all_text, lang='en')
tts.save(output_file)

print(f"Audio saved to {output_file}")
