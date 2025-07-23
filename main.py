import  pyttsx3
from PyPDF2 import PdfReader

book=PdfReader('a_thousand_splendid_sun.pdf')
no_of_pages=len(book.pages)

##print(no_of_pages)
##print(text)

##initialize voices
speak=pyttsx3.init()

##set to female voice
voices = speak.getProperty('voices')
speak.setProperty('voice', voices[1].id)


## extract text and speak
for i in range(4,no_of_pages):
    page=book.pages[i]
    text=page.extract_text()
    
    speak.say(text)
    
    speak.runAndWait()