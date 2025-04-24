import pandas as pd
import pdfplumber
import docx
import os 

def load_keywords(filepath):
    df=pd.read_excel(filepath)
    if'Skills' in df.columns:
        keywords = df['Skills'].dropna().tolist()
        return [str(k).strip().lower()for k in keywords]
    return []

def extract_text(filepath):
    text=""
    if filepath.lower().endswith('.pdf'):
        with pdfplumber.open(filepath)as pdf:
            for page in pdf.pages:
                text+=page.extract_text() or""
    elif filepath.lower().endswith('.docx'):
        doc=docx.Document(filepath)
        for para in doc.paragraphs:
            text+=para.text+"\n"
    return text.lower()
def calculate_score(text, keywords, keyword_weights=None):
    scores=[]
    feedback=[]
    total_score=0

    for keyword in keywords:
        count = text.count(keyword.lower())
        weight = keyword_weights.get(keyword, 1) if keyword_weights else 1
        total_score += count*weight
        scores.append(count * weight)
        feedback.append(f"'{keyword}':{'found' if count>0 else 'Not Found'}")
        
    normalized_score=total_score/(len(keywords)if keywords else 1)
    return normalized_score, feedback
def parse_and_score(resume_path,keywords_path, keyword_weights=None):
    keywords = load_keywords(keywords_path)
    text= extract_text(resume_path)
    return calculate_score(text,keywords,keyword_weights)

