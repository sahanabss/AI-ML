AI Resume Screening Agent

An AI-powered Resume Screening Agent that automatically analyzes and ranks candidate resumes against a given Job Description (JD). The system uses NLP-based semantic similarity, skill extraction, skill gap analysis, and ATS-style recommendations to help recruiters identify suitable candidates efficiently.

📌 Problem Statement

Recruiters often spend significant time manually reviewing resumes for a single job opening. This project automates the initial screening process by comparing resumes with a job description and generating:

Candidate ranking
Resume relevance score
Matched skills
Missing skills
ATS recommendation
🚀 Features
Resume Processing
Supports PDF and DOCX resumes
Extracts resume text automatically
Processes multiple resumes in a single run
AI-Based Resume Matching
Uses NLP semantic similarity to compare resumes with job descriptions
Calculates candidate relevance score
Ranks candidates based on matching percentage
Skill Analysis
Extracts required skills from the Job Description
Identifies skills present in candidate resumes
Finds missing skills
ATS Recommendation System

Generates hiring recommendations:

✅ Strong Fit
👍 Good Fit
⚠️ Needs Improvement
❌ Not Suitable
Output

Provides:

Ranked candidate list
Skill analysis
Recommendation
Downloadable CSV report
🏗️ System Architecture
Job Description
        |
        ↓
Required Skill Extraction
        |
        ↓
Resume Upload (PDF/DOCX)
        |
        ↓
Resume Text Extraction
        |
        ↓
NLP Semantic Similarity
        |
        ↓
Skill Matching
        |
        ↓
Skill Gap Analysis
        |
        ↓
Candidate Ranking
        |
        ↓
ATS Recommendation
🛠️ Tech Stack
Programming Language
Python
Framework
Streamlit
Libraries
Pandas
PyPDF
python-docx
Scikit-learn
Sentence Transformers
NLP techniques
📂 Project Structure
AI-Resume-Screening-Agent
│
├── app.py
├── requirements.txt
├── README.md
│
├── data
│   ├── job_description.txt
│   └── resumes
│       ├── resume1.pdf
│       ├── resume2.pdf
│
├── src
│   ├── resume_parser.py
│   ├── similarity.py
│   ├── ranker.py
│   ├── analyzer.py
│   ├── skill_extractor.py
│   ├── skill_gap.py
│   └── recommendation.py
│
└── output
    └── ranked_candidates.csv
⚙️ Installation & Setup
1. Clone Repository
git clone https://github.com/yourusername/AI-Resume-Screening-Agent.git

Navigate into the project:

cd AI-Resume-Screening-Agent
2. Create Virtual Environment
python -m venv venv

Activate:

Windows
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Run Application
streamlit run app.py

The application will open in your browser:

http://localhost:8501
📖 How It Works
Upload a Job Description file.
Upload multiple resumes.
The system extracts resume text.
Resume and JD content are converted into numerical representations.
Semantic similarity is calculated.
Candidates are ranked according to relevance.
Required, matched, and missing skills are displayed.
ATS recommendation is generated.
🧠 Scoring Method

The system uses NLP semantic similarity.

Process:

Extract text from resumes and job description.
Convert text into embeddings.
Calculate similarity between resume and job description.
Generate a relevance score.
Rank candidates from highest to lowest score.
Advantages
Understands meaning beyond exact keyword matching.
Can identify related skills and experience.
Limitations
Domain-specific skills may require additional customization.
Skill extraction currently uses a predefined skill dictionary.
📊 Sample Output

Example:

Rank	Candidate	Score	Matched Skills	Missing Skills	Recommendation
1	resume1.pdf	85%	Python, ML, TensorFlow	NLP	Strong Fit
2	resume2.pdf	65%	Python, SQL	LLM, RAG	Good Fit
🔮 Future Improvements
Integrate LLM-based resume reasoning
Add automatic interview question generation
Add recruiter dashboard analytics
Support more document formats
Improve skill extraction using Named Entity Recognition (NER)
👩‍💻 Author

Sahana B S

Computer Science Engineering

📌 Project Purpose

Built as part of the Rooman AI Challenge – Junior AI Research Associate Selection Round.

The goal was to design and develop a working AI agent capable of screening resumes, ranking candidates, and providing recruitment insights.