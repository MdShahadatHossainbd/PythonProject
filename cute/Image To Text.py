import pytesseract
import os
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"C:/home/sh/PycharmProjects/python000/project/cute/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe"
    # https://github.com/UB-Mannheim/tesseract/wiki
def convert():
    img = Image.open('web2.png')
    text = pytesseract.image_to_string(img)
    print(text)

convert()