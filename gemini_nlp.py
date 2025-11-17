import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Main model
model = genai.GenerativeModel(
    "gemini-2.0-flash",
    system_instruction="""
You are a task assistant engine.
You support two modes:
1) Extracting tasks as JSON
2) Breaking tasks into subtasks list
"""
)

def clean_json(text):
    """Remove code fences and extract JSON."""
    text = re.sub(r"```json|```", "", text).strip()
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group(0)
    return text


def parse_task(user_input):
    response = model.generate_content(f"""
Extract task from: "{user_input}"

Respond ONLY with JSON in this format:
{{
 "title": "...",
 "due_date": "... or null",
 "priority": "high/medium/low",
 "category": "work/personal/general"
}}
""")

    text = clean_json(response.text.strip())
    try:
        return json.loads(text)
    except Exception as e:
        return {"error": f"Invalid JSON: {e}", "raw": text}



def break_down_task(task_text):
    response = model.generate_content(f"""
Break down the following task into clear, actionable subtasks:

"{task_text}"

Respond ONLY with a JSON list, example:
[
 "subtask 1",
 "subtask 2"
]
""")

    text = response.text.strip()
    text = re.sub(r"```json|```", "", text).strip()

    try:
        data = json.loads(text)
        return data
    except Exception as e:
        return {"error": f"Invalid JSON in breakdown: {e}", "raw": text}
