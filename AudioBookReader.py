"""
install python ide(python.org)
install pyCharm
Write pyCharm Terminal
            pip install pyttsx3
            pip install PyPDF3
"""
import pyttsx3
import PyPDF2

book = open('automate.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
friend = pyttsx3.init()
for num in range(10, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    friend.say(text)
    friend.runAndWait()
