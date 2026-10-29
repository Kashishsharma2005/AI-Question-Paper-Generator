import sqlite3
from pathlib import Path

DB_PATH = Path("question_generator.db")

def connect():
    return sqlite3.connect(DB_PATH)

def init_db():
    con = connect()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            topic TEXT NOT NULL,
            qtype TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            bloom TEXT NOT NULL,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            option_a TEXT,
            option_b TEXT,
            option_c TEXT,
            option_d TEXT,
            correct_option TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            subject TEXT,
            topic TEXT,
            created_at TEXT,
            question_count INTEGER,
            difficulty TEXT,
            bloom TEXT
        )
    """)
    con.commit()
    con.close()

def add_question(q):
    con = connect()
    con.execute("""
        INSERT INTO questions
        (subject, topic, qtype, difficulty, bloom, question, answer,
         option_a, option_b, option_c, option_d, correct_option)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        q["subject"], q["topic"], q["qtype"], q["difficulty"], q["bloom"],
        q["question"], q["answer"], q.get("A"), q.get("B"),
        q.get("C"), q.get("D"), q.get("correct")
    ))
    con.commit()
    con.close()

def get_questions(subject="", topic="", qtype="", difficulty="", bloom=""):
    con = connect()
    query = "SELECT * FROM questions WHERE 1=1"
    params = []

    if subject:
        query += " AND subject LIKE ?"
        params.append("%" + subject + "%")
    if topic:
        query += " AND topic LIKE ?"
        params.append("%" + topic + "%")
    if qtype:
        query += " AND qtype=?"
        params.append(qtype)
    if difficulty:
        query += " AND difficulty=?"
        params.append(difficulty)
    if bloom:
        query += " AND bloom=?"
        params.append(bloom)

    rows = con.execute(query, params).fetchall()
    con.close()
    return rows

def save_paper(title, subject, topic, count, difficulty, bloom, created_at):
    con = connect()
    con.execute("""
        INSERT INTO papers(title, subject, topic, created_at,
                           question_count, difficulty, bloom)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (title, subject, topic, created_at, count, difficulty, bloom))
    con.commit()
    con.close()

def get_papers():
    con = connect()
    rows = con.execute(
        "SELECT * FROM papers ORDER BY id DESC"
    ).fetchall()
    con.close()
    return rows
