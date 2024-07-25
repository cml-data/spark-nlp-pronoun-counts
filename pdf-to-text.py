# importing required modules
from pypdf import PdfReader
f = open("parable.txt", "a")

# creating a pdf reader object
reader = PdfReader('parable-of-the-sower.pdf')

# printing number of pages in pdf file
print(len(reader.pages))

for page in reader.pages:
    # extracting text from page
    text = page.extract_text()
    f.write(text)

f.close()