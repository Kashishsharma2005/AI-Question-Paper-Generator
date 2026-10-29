import random
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from database import init_db, add_question, get_questions, save_paper
from question_bank import QUESTIONS
from ai_generator import generate_with_huggingface
from paper_generator import make_pdf
from excel_manager import export_excel
from analytics import create_analytics


class QuestionPaperApp:

    def __init__(self, root):
        self.root = root
        self.root.title("AI-Powered Question Paper Generator")
        self.root.geometry("1100x720")
        self.root.minsize(950, 650)

        self.generated = []

        init_db()
        self.load_builtin_questions()

        self.build_gui()

    def load_builtin_questions(self):
        existing = get_questions()
        if not existing:
            for q in QUESTIONS:
                add_question(q)

    def build_gui(self):
        header = tk.Frame(self.root, padx=20, pady=15)
        header.pack(fill="x")

        tk.Label(
            header,
            text="AI-POWERED QUESTION PAPER GENERATOR",
            font=("Arial", 22, "bold")
        ).pack()

        tk.Label(
            header,
            text="Question generation • Bloom's Taxonomy • Assessment • PDF • Excel",
            font=("Arial", 10)
        ).pack(pady=4)

        settings = ttk.LabelFrame(self.root, text="Paper Settings", padding=15)
        settings.pack(fill="x", padx=20, pady=8)

        # Row 1
        ttk.Label(settings, text="Subject:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.subject = ttk.Entry(settings, width=25)
        self.subject.insert(0, "Python")
        self.subject.grid(row=0, column=1, padx=5)

        ttk.Label(settings, text="Topic:").grid(row=0, column=2, sticky="w", padx=5)
        self.topic = ttk.Entry(settings, width=25)
        self.topic.insert(0, "Python")
        self.topic.grid(row=0, column=3, padx=5)

        ttk.Label(settings, text="Questions:").grid(row=0, column=4, sticky="w", padx=5)
        self.count = ttk.Spinbox(settings, from_=1, to=50, width=8)
        self.count.set(10)
        self.count.grid(row=0, column=5, padx=5)

        # Row 2
        ttk.Label(settings, text="Question Type:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.qtype = ttk.Combobox(
            settings,
            values=["Any", "MCQ", "Short Answer", "Long Answer"],
            state="readonly",
            width=22
        )
        self.qtype.set("Any")
        self.qtype.grid(row=1, column=1, padx=5)

        ttk.Label(settings, text="Difficulty:").grid(row=1, column=2, sticky="w", padx=5)
        self.difficulty = ttk.Combobox(
            settings,
            values=["Any", "Easy", "Medium", "Hard"],
            state="readonly",
            width=22
        )
        self.difficulty.set("Any")
        self.difficulty.grid(row=1, column=3, padx=5)

        ttk.Label(settings, text="Bloom Level:").grid(row=1, column=4, sticky="w", padx=5)
        self.bloom = ttk.Combobox(
            settings,
            values=[
                "Any", "Remember", "Understand", "Apply",
                "Analyse", "Evaluate", "Create"
            ],
            state="readonly",
            width=18
        )
        self.bloom.set("Any")
        self.bloom.grid(row=1, column=5, padx=5)

        buttons = tk.Frame(self.root, padx=20, pady=10)
        buttons.pack(fill="x")

        ttk.Button(
            buttons, text="Generate Paper",
            command=self.generate
        ).pack(side="left", padx=5)

        ttk.Button(
            buttons, text="Export PDF",
            command=self.export_pdf
        ).pack(side="left", padx=5)

        ttk.Button(
            buttons, text="Export Excel",
            command=self.export_excel
        ).pack(side="left", padx=5)

        ttk.Button(
            buttons, text="Analytics",
            command=self.analytics
        ).pack(side="left", padx=5)

        ttk.Button(
            buttons, text="Clear",
            command=self.clear
        ).pack(side="left", padx=5)

        ttk.Button(
            buttons, text="Exit",
            command=self.root.destroy
        ).pack(side="right", padx=5)

        output_frame = ttk.LabelFrame(
            self.root,
            text="Generated Question Paper",
            padding=10
        )
        output_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.text = tk.Text(
            output_frame,
            wrap="word",
            font=("Consolas", 11)
        )
        self.text.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(
            output_frame,
            orient="vertical",
            command=self.text.yview
        )
        scrollbar.pack(side="right", fill="y")
        self.text.configure(yscrollcommand=scrollbar.set)

    def get_filter_value(self, widget):
        value = widget.get()
        return "" if value == "Any" else value

    def generate(self):
        subject = self.subject.get().strip()
        topic = self.topic.get().strip()
        qtype = self.get_filter_value(self.qtype)
        difficulty = self.get_filter_value(self.difficulty)
        bloom = self.get_filter_value(self.bloom)

        if not subject or not topic:
            messagebox.showwarning("Input Error", "Enter subject and topic.")
            return

        try:
            count = int(self.count.get())
        except ValueError:
            messagebox.showwarning("Input Error", "Enter a valid question count.")
            return

        # First try optional AI generation
        ai_questions = generate_with_huggingface(
            topic, subject, qtype or "mixed",
            difficulty or "mixed", bloom or "mixed", count
        )

        selected = []

        if ai_questions:
            for item in ai_questions[:count]:
                item.update({
                    "subject": subject,
                    "topic": topic,
                    "qtype": qtype or "AI Generated",
                    "difficulty": difficulty or "Mixed",
                    "bloom": bloom or "Mixed"
                })
                selected.append(item)
        else:
            # Offline fallback
            rows = get_questions(
                subject=subject,
                topic=topic,
                qtype=qtype,
                difficulty=difficulty,
                bloom=bloom
            )

            # If exact subject/topic has no matches, search by subject.
            if not rows:
                rows = get_questions(subject=subject)

            if not rows:
                rows = get_questions()

            random.shuffle(rows)

            for row in rows[:count]:
                selected.append({
                    "id": row[0],
                    "subject": row[1],
                    "topic": row[2],
                    "qtype": row[3],
                    "difficulty": row[4],
                    "bloom": row[5],
                    "question": row[6],
                    "answer": row[7],
                    "A": row[8],
                    "B": row[9],
                    "C": row[10],
                    "D": row[11],
                    "correct": row[12]
                })

        if not selected:
            messagebox.showerror("No Questions", "No questions available.")
            return

        self.generated = selected

        self.text.delete("1.0", tk.END)

        self.text.insert(
            tk.END,
            "=" * 75 + "\n"
            "                 QUESTION PAPER\n"
            + "=" * 75 + "\n\n"
        )

        self.text.insert(tk.END, f"Subject       : {subject}\n")
        self.text.insert(tk.END, f"Topic         : {topic}\n")
        self.text.insert(tk.END, f"Questions     : {len(selected)}\n")
        self.text.insert(tk.END, f"Difficulty    : {difficulty or 'Mixed'}\n")
        self.text.insert(tk.END, f"Bloom Level   : {bloom or 'Mixed'}\n")
        self.text.insert(
            tk.END,
            f"Date          : {datetime.now().strftime('%d-%m-%Y')}\n\n"
        )

        self.text.insert(tk.END, "-" * 75 + "\n")

        for i, q in enumerate(selected, 1):
            self.text.insert(
                tk.END,
                f"\nQ{i}. {q['question']}\n"
            )

            if q.get("qtype") == "MCQ":
                self.text.insert(tk.END, f"    A) {q.get('A','')}\n")
                self.text.insert(tk.END, f"    B) {q.get('B','')}\n")
                self.text.insert(tk.END, f"    C) {q.get('C','')}\n")
                self.text.insert(tk.END, f"    D) {q.get('D','')}\n")

        self.text.insert(tk.END, "\n" + "=" * 75 + "\n")
        self.text.insert(tk.END, "                     ANSWER KEY\n")
        self.text.insert(tk.END, "=" * 75 + "\n\n")

        for i, q in enumerate(selected, 1):
            answer = (
                q.get("correct")
                if q.get("qtype") == "MCQ"
                else q.get("answer", "")
            )
            self.text.insert(tk.END, f"Q{i}. {answer}\n")

        save_paper(
            "Generated Question Paper",
            subject,
            topic,
            len(selected),
            difficulty or "Mixed",
            bloom or "Mixed",
            datetime.now().isoformat(timespec="seconds")
        )

        messagebox.showinfo(
            "Success",
            f"{len(selected)} questions generated successfully."
        )

    def export_pdf(self):
        if not self.generated:
            messagebox.showwarning("No Paper", "Generate a paper first.")
            return

        path = make_pdf(
            "AI-POWERED QUESTION PAPER",
            self.subject.get(),
            self.topic.get(),
            self.difficulty.get(),
            self.bloom.get(),
            self.generated
        )

        messagebox.showinfo("PDF Created", f"Saved:\n{path}")

    def export_excel(self):
        if not self.generated:
            messagebox.showwarning("No Paper", "Generate a paper first.")
            return

        path = export_excel(self.generated)
        messagebox.showinfo("Excel Created", f"Saved:\n{path}")

    def analytics(self):
        if not self.generated:
            messagebox.showwarning("No Paper", "Generate a paper first.")
            return

        path = create_analytics(self.generated)
        messagebox.showinfo("Analytics Created", f"Saved:\n{path}")

    def clear(self):
        self.text.delete("1.0", tk.END)
        self.generated = []


if __name__ == "__main__":
    root = tk.Tk()
    app = QuestionPaperApp(root)
    root.mainloop()
