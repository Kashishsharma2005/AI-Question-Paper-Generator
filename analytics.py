from pathlib import Path
import matplotlib.pyplot as plt

OUTPUT = Path("output")
OUTPUT.mkdir(exist_ok=True)

def create_analytics(questions):
    if not questions:
        return None

    counts = {}
    for q in questions:
        key = q.get("difficulty", "Unknown")
        counts[key] = counts.get(key, 0) + 1

    labels = list(counts.keys())
    values = list(counts.values())

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values)
    plt.title("Question Distribution by Difficulty")
    plt.xlabel("Difficulty")
    plt.ylabel("Number of Questions")
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    path = OUTPUT / "difficulty_analysis.png"
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

    return str(path)
