from src.resume_parser import extract_text


resume_path = "data/resumes/sahana_resume01.pdf"

text = extract_text(resume_path)

print(text)