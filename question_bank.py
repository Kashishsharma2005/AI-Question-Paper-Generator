# Built-in question bank.
# Add more dictionaries using the same structure to expand the project.

QUESTIONS = [
    # Python - Remember
    {
        "subject": "Python", "topic": "Python Basics",
        "qtype": "Short Answer", "difficulty": "Easy", "bloom": "Remember",
        "question": "What is Python?",
        "answer": "Python is a high-level, interpreted programming language."
    },
    {
        "subject": "Python", "topic": "Variables",
        "qtype": "Short Answer", "difficulty": "Easy", "bloom": "Remember",
        "question": "What is a variable in Python?",
        "answer": "A variable is a name used to store a value in a program."
    },
    {
        "subject": "Python", "topic": "Data Types",
        "qtype": "MCQ", "difficulty": "Easy", "bloom": "Remember",
        "question": "Which of the following is an immutable Python data type?",
        "answer": "Tuple",
        "A": "List", "B": "Dictionary", "C": "Tuple", "D": "Set",
        "correct": "C"
    },
    {
        "subject": "Python", "topic": "Loops",
        "qtype": "MCQ", "difficulty": "Easy", "bloom": "Understand",
        "question": "Which loop is commonly used to iterate over a sequence?",
        "answer": "for loop",
        "A": "switch", "B": "for", "C": "goto", "D": "case",
        "correct": "B"
    },

    # Python - Apply/Analyse
    {
        "subject": "Python", "topic": "Conditions",
        "qtype": "Short Answer", "difficulty": "Medium", "bloom": "Apply",
        "question": "Write a Python statement that checks whether a number is even.",
        "answer": "Use: if number % 2 == 0:"
    },
    {
        "subject": "Python", "topic": "Functions",
        "qtype": "Long Answer", "difficulty": "Medium", "bloom": "Analyse",
        "question": "Explain how functions improve the structure of a Python program.",
        "answer": "Functions divide a program into reusable logical units, improving readability, testing, maintenance and code reuse."
    },
    {
        "subject": "Python", "topic": "Lists",
        "qtype": "MCQ", "difficulty": "Medium", "bloom": "Apply",
        "question": "Which method adds an element to the end of a Python list?",
        "answer": "append()",
        "A": "add()", "B": "insertEnd()", "C": "append()", "D": "push()",
        "correct": "C"
    },

    # Python - Evaluate/Create
    {
        "subject": "Python", "topic": "Programming",
        "qtype": "Long Answer", "difficulty": "Hard", "bloom": "Evaluate",
        "question": "Evaluate the advantages of using Python for rapid application development.",
        "answer": "Python provides readable syntax, extensive libraries, rapid prototyping and a large ecosystem, although execution can be slower than some compiled languages."
    },
    {
        "subject": "Python", "topic": "Project Design",
        "qtype": "Long Answer", "difficulty": "Hard", "bloom": "Create",
        "question": "Design a Python application for managing student marks and generating grades.",
        "answer": "The application should collect marks, validate input, calculate totals and percentages, assign grades, store records and display a report."
    },

    # DBMS
    {
        "subject": "DBMS", "topic": "Database Basics",
        "qtype": "Short Answer", "difficulty": "Easy", "bloom": "Remember",
        "question": "What is a DBMS?",
        "answer": "A DBMS is software used to create, store, organize and manage data in databases."
    },
    {
        "subject": "DBMS", "topic": "Keys",
        "qtype": "MCQ", "difficulty": "Easy", "bloom": "Remember",
        "question": "Which key uniquely identifies a record in a table?",
        "answer": "Primary key",
        "A": "Foreign key", "B": "Primary key", "C": "Candidate value", "D": "Null key",
        "correct": "B"
    },
    {
        "subject": "DBMS", "topic": "Normalization",
        "qtype": "Short Answer", "difficulty": "Medium", "bloom": "Understand",
        "question": "Why is normalization used in databases?",
        "answer": "Normalization reduces data redundancy and helps maintain data consistency."
    },
    {
        "subject": "DBMS", "topic": "SQL",
        "qtype": "Long Answer", "difficulty": "Hard", "bloom": "Create",
        "question": "Design SQL operations for inserting, updating and retrieving student records.",
        "answer": "Use INSERT to add records, UPDATE to modify records and SELECT to retrieve records."
    },

    # OS
    {
        "subject": "Operating System", "topic": "OS Basics",
        "qtype": "Short Answer", "difficulty": "Easy", "bloom": "Remember",
        "question": "What is an operating system?",
        "answer": "An operating system is system software that manages computer hardware and provides services to applications."
    },
    {
        "subject": "Operating System", "topic": "Process Management",
        "qtype": "MCQ", "difficulty": "Medium", "bloom": "Understand",
        "question": "Which component of an OS manages running processes?",
        "answer": "Process management",
        "A": "File management", "B": "Process management", "C": "User interface", "D": "Compiler",
        "correct": "B"
    },
    {
        "subject": "Operating System", "topic": "Memory Management",
        "qtype": "Short Answer", "difficulty": "Medium", "bloom": "Apply",
        "question": "What is the purpose of memory management?",
        "answer": "It allocates and deallocates memory and keeps track of memory usage by processes."
    },
    {
        "subject": "Operating System", "topic": "Security",
        "qtype": "Long Answer", "difficulty": "Hard", "bloom": "Evaluate",
        "question": "Evaluate why security and protection are important functions of an operating system.",
        "answer": "They help protect files, processes, memory and system resources from unauthorized access or misuse."
    }
]
