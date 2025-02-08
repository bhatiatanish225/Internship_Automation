import spacy
from docx import Document
import pdfplumber

nlp = spacy.load("en_core_web_sm")

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_resume_details(resume_file):
    text = extract_text_from_docx(resume_file) if resume_file.name.endswith(".docx") else extract_text_from_pdf(resume_file)
    doc = nlp(text)
    
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
    return {"text": text, "skills": skills}
