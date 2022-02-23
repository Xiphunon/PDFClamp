import os
from pdfrw import PdfReader, PdfWriter

pdfFullPathArray = []

def findPdf(dir_name):
    for name in os.listdir(dir_name):
        pathName = os.path.join(dir_name, name)
        if os.path.isdir(pathName):
            findPdf(pathName)
        elif os.path.isfile(pathName) and pathName.endswith('.pdf'):
            pdfFullPathArray.append(pathName)

findPdf(os.getcwd())

if pdfFullPathArray:
    print("Found", len(pdfFullPathArray), ".pdf files. Creating merged pdf file...")
    pdfWriter = PdfWriter()
    for pdfPath in pdfFullPathArray:
        pdfWriter.addpages(PdfReader(pdfPath).pages)
    pdfWriter.write("Final.pdf")
else:
    print("No .pdf files found. Exiting...")

exit()
