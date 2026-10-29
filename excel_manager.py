from pathlib import Path
import openpyxl

OUTPUT = Path("output")
OUTPUT.mkdir(exist_ok=True)

def export_excel(questions):
    path = OUTPUT / "question_bank_export.xlsx"

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Questions"

    headers = [
        "No.", "Subject", "Topic", "Type", "Difficulty",
        "Bloom Level", "Question", "Answer",
        "Option A", "Option B", "Option C", "Option D", "Correct"
    ]
    ws.append(headers)

    for i, q in enumerate(questions, 1):
        ws.append([
            i, q.get("subject",""), q.get("topic",""),
            q.get("qtype",""), q.get("difficulty",""),
            q.get("bloom",""), q.get("question",""),
            q.get("answer",""), q.get("A",""), q.get("B",""),
            q.get("C",""), q.get("D",""), q.get("correct","")
        ])

    for col in ws.columns:
        max_length = 0
        letter = col[0].column_letter
        for cell in col:
            max_length = max(max_length, len(str(cell.value or "")))
        ws.column_dimensions[letter].width = min(max_length + 2, 45)

    wb.save(path)
    return str(path)
