AI-POWERED QUESTION PAPER GENERATOR
===================================

1. Install Python 3.

2. Open the project folder in VS Code.

3. Open PowerShell in the project folder.

4. Install libraries:

   pip install -r requirements.txt

5. Run:

   python main.py

FEATURES
--------
- Tkinter GUI
- Subject and topic selection
- MCQ, Short Answer and Long Answer
- Easy, Medium and Hard difficulty
- Six Bloom's Taxonomy levels
- Random question selection
- Answer key
- PDF export
- Excel export
- Difficulty analytics graph
- SQLite database
- Optional Hugging Face AI generation

OPTIONAL AI MODE
----------------
Set these environment variables before running:

HF_API_TOKEN
HF_MODEL

If they are not set, the application automatically uses its
offline SQLite question bank.

OUTPUT FILES
------------
output/generated_question_paper.pdf
output/question_bank_export.xlsx
output/difficulty_analysis.png
question_generator.db
