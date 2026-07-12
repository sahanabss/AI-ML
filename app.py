import streamlit as st
import os
import shutil

from src.ranker import rank_resumes


st.title("AI Resume Screening Agent")

st.write(
    "Upload a Job Description and multiple resumes to rank candidates."
)


# Upload Job Description
jd_file = st.file_uploader(
    "Upload Job Description",
    type=["txt"]
)


# Upload Resumes
resume_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True
)


if st.button("Analyze Resumes"):

    if jd_file and resume_files:

        # Read JD
        job_description = jd_file.read().decode(
            "utf-8"
        )


        # Temporary folder
        temp_folder = "temp_resumes"


        # Remove previous uploads
        if os.path.exists(temp_folder):
            shutil.rmtree(temp_folder)


        os.makedirs(
            temp_folder,
            exist_ok=True
        )


        # Save uploaded resumes
        for file in resume_files:

            with open(
                os.path.join(
                    temp_folder,
                    file.name
                ),
                "wb"
            ) as f:

                f.write(
                    file.getbuffer()
                )


        # Run ranking
        result, required_skills = rank_resumes(
            temp_folder,
            job_description
        )


        # Job requirements section
        st.subheader(
            "Job Requirements"
        )

        st.write(
            "Maximum Match Score: 100%"
        )


        st.write(
            "Required Skills:"
        )


        for skill in required_skills:
            st.write(
                "✓ " + skill.title()
            )


        # Candidate ranking
        st.subheader(
            "Candidate Ranking"
        )


        st.dataframe(
            result,
            hide_index=True
        )


        # Download CSV
        csv = result.to_csv(
            index=False
        )


        st.download_button(
            "Download Ranked Results CSV",
            csv,
            "ranked_candidates.csv",
            "text/csv"
        )


    else:

        st.warning(
            "Please upload JD and resumes."
        )