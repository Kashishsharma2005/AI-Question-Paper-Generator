import os
import json
import requests

def generate_with_huggingface(topic, subject, qtype, difficulty, bloom, count):
    """
    Optional online AI generator.
    Set:
      HF_API_TOKEN = your Hugging Face token
      HF_MODEL = a text-generation model endpoint
    If these variables are not set, the main application uses the offline
    question bank.
    """
    token = os.getenv("HF_API_TOKEN")
    model = os.getenv("HF_MODEL")

    if not token or not model:
        return []

    prompt = f"""
Generate {count} {qtype} questions for undergraduate students.
Subject: {subject}
Topic: {topic}
Difficulty: {difficulty}
Bloom's Taxonomy: {bloom}

Return ONLY valid JSON as a list. Each item must contain:
question, answer, A, B, C, D, correct.
For non-MCQ questions, use empty strings for A-D-correct.
"""

    url = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.post(
            url,
            headers=headers,
            json={"inputs": prompt},
            timeout=60
        )
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and data and "generated_text" in data[0]:
            text = data[0]["generated_text"]
            start = text.find("[")
            end = text.rfind("]")
            if start != -1 and end != -1:
                return json.loads(text[start:end + 1])
    except Exception:
        pass

    return []
