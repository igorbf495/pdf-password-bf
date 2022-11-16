
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

def password_pdf(file, password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)
    
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))

    parser.encrypt(password)
    with open(f"pdf_senha_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"pdf_senha_{file} Criado")

if __name__ == "__main__":
    file = sys.argv[1]
    password = sys.argv[2]
    password_pdf(file, password)

# Exemplo de como usar: (chamando no terminal) python3 pdf-password.py arroz.pdf 123456
