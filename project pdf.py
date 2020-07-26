# How to password project pdf file using python || PyPDF2
from PyPDF2 import PdfFileWriter , PdfFileReader
pdfWriter = PdfFileWriter()
pdf = PdfFileReader("Research Design .pdf")

for page_num in range(pdf.numPages):
    pdfWriter.addPage(pdf.getPage(page_num))

passward = "Shahadat"
pdfWriter.encrypt(passward)

with open("Research.pdf",'wb') as f:
    pdfWriter.write(f)
    f.close()