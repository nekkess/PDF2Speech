import requests
import webbrowser
import tkinter as tk
from tkinter import filedialog
from pdfminer.high_level import extract_text
import os

# paste your own API key here
API_key = os.environ['API_KEY']
API = 'http://api.voicerss.org/?'

# opens the file search
window = tk.Tk()
window.withdraw()

file_path = filedialog.askopenfilename(
    filetypes=[('PDF Files', '*.pdf')],
    title='Select a PDF file'
)

if file_path:
    text = 'Sorry, no text was detected'
    text = extract_text(file_path)
    print(text)

params = {
    'key': API_key,
    'src': text,
    'hl': 'en-us',
    'v': 'Mike'
}

# convert the text into audio using API
response = requests.get(url=API, params=params)
with open('response.mp3', 'wb') as f:
    f.write(response.content)
# open & play
webbrowser.open('response.mp3')


