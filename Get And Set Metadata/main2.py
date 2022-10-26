import PyPDF2


Reader = PyPDF2.PdfReader(stream="./sample3.pdf", strict=False, password=None)
Writer = PyPDF2.PdfWriter()

for page in Reader.pages:
    Writer.add_page(page)

metaData = {
    "/Author": "Ankur Jaiswal",
    "/Creator": "Python 3.10.7",
    "/Producer": "CodemyCoder",
    "/Subject": "PyPDF2 File",
    "/Title": "Playing With PyPDF2"
}

Writer.add_metadata(metaData)

with open("sample.pdf", "wb") as pdfFile:
    Writer.write(pdfFile)
