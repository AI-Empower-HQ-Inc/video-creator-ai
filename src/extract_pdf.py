import fitz

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    return "\n\n".join([page.get_text() for page in doc])