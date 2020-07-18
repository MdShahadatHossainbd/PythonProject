from PyPDF2 import PdfFileMerger
import os

#book = os.getcwd()

merger = PdfFileMerger()
for items in os.listdir():
    if items.endswith('.pdf'):
        merger.append(items)

merger.write("waste_pdf.pdf")
merger.close()