from openai import OpenAI
from PyPDF2 import PdfReader
client = OpenAI()
print("\n📑AI Resume Reviewer")
print("---------------------")
file_path = input("📂 Enter the path to your resume PDF: ")
reader = PdfReader(file_path)
resume_text = ""
for page in reader.pages:
    resume_text += page.extract_text()
response = client.responses.create(
    model="gpt-4.1-mini",
    input=f"""
    You are an expert resume reviewer.
    Analyze the resume below and return:
    1. 3 strengths
    2. 3 specific improvements
    3. A rewritten professional summary (2-3 lines)
      Resume:
    {resume_text}
    """
)
review = response.output_text
print ("\n✅AI REVIEW:\n")
print(review)
with open("resume_review.txt", "w") as file:
    file.write(review)
print("\n✅ Resume review saved to resume_review.txt")