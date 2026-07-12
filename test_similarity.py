from src.resume_parser import extract_text
from src.similarity import calculate_similarity


# Resume path
resume_path = "data/resumes/sahana_resume01.pdf"


# Job description path
jd_path = "data/job_description.txt"


# Extract resume text
resume_text = extract_text(resume_path)


# Read job description
with open(jd_path, "r", encoding="utf-8") as file:
    job_description = file.read()


# Calculate score
score = calculate_similarity(
    job_description,
    resume_text
)


print("Resume Match Score:", score, "%")