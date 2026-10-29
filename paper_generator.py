from datetime import datetime
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

OUTPUT = Path("output")
OUTPUT.mkdir(exist_ok=True)

def make_pdf(title, subject, topic, difficulty, bloom, questions):
    filename = OUTPUT / "generated_question_paper.pdf"

    doc = SimpleDocTemplate(
        str(filename),
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "CenterTitle", parent=styles["Title"], alignment=TA_CENTER
    )

    story = [
        Paragraph(title, title_style),
        Spacer(1, 12),
        Paragraph(f"<b>Subject:</b> {subject}", styles["Normal"]),
        Paragraph(f"<b>Topic:</b> {topic}", styles["Normal"]),
        Paragraph(f"<b>Difficulty:</b> {difficulty}", styles["Normal"]),
        Paragraph(f"<b>Bloom's Level:</b> {bloom}", styles["Normal"]),
        Paragraph(f"<b>Date:</b> {datetime.now().strftime('%d-%m-%Y')}", styles["Normal"]),
        Spacer(1, 18)
    ]

    for i, q in enumerate(questions, 1):
        story.append(Paragraph(
            f"<b>Q{i}. {q['question']}</b>", styles["Normal"]
        ))

        if q.get("qtype") == "MCQ":
            data = [
                [f"A) {q.get('A','')}", f"B) {q.get('B','')}"],
                [f"C) {q.get('C','')}", f"D) {q.get('D','')}"]
            ]
            table = Table(data, colWidths=[240, 240])
            table.setStyle(TableStyle([
                ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
                ("VALIGN", (0,0), (-1,-1), "TOP"),
                ("LEFTPADDING", (0,0), (-1,-1), 6),
                ("RIGHTPADDING", (0,0), (-1,-1), 6),
            ]))
            story.append(Spacer(1, 5))
            story.append(table)

        story.append(Spacer(1, 14))

    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>ANSWER KEY</b>", title_style))
    story.append(Spacer(1, 10))

    for i, q in enumerate(questions, 1):
        if q.get("qtype") == "MCQ":
            ans = q.get("correct", "")
        else:
            ans = q.get("answer", "")
        story.append(Paragraph(f"<b>Q{i}:</b> {ans}", styles["Normal"]))
        story.append(Spacer(1, 6))

    doc.build(story)
    return str(filename)
