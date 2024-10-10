import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            print(page.extract_text())
            text += page.extract_text()
    return text


pdf_path = 'Publication+05.04.2024.pdf'
pdf_text = extract_text_from_pdf(pdf_path)

print("test")

print(pdf_text)