import PyPDF2

Reader = PyPDF2.PdfReader(stream="./sample3.pdf", strict=False, password="my-secret-password")
MetaData = Reader.metadata
print("Pdf MetaData Details: \n")
print("MetaData\n", MetaData, "\n")
print('Total No. Of Pages: ', len(Reader.pages))
print("Author: ", MetaData.author)
print("Creator: ", MetaData.creator)
print("Producer: ", MetaData.producer)
print("Subject: ", MetaData.subject)
print("Title: ", MetaData.title)
print("Creation Date & Time: ", MetaData.creation_date)
print("Modification Date & Time: ", MetaData.modification_date)
