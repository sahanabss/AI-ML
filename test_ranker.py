from src.ranker import rank_resumes


resume_folder = "data/resumes"


with open(
    "data/job_description.txt",
    "r",
    encoding="utf-8"
) as file:
    job_description = file.read()


ranking = rank_resumes(
    resume_folder,
    job_description
)


# Add ranking column
ranking.insert(
    0,
    "Rank",
    range(1, len(ranking)+1)
)


# Save CSV
ranking.to_csv(
    "output/ranked_candidates.csv",
    index=False
)


print(ranking)

print("\nCSV file created successfully!")