import json
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume(resume_text, job_role):

    prompt = f"""
You are an expert technical recruiter.

Analyze the following resume for the role of {job_role}.

Respond ONLY in valid JSON.

Format:

{{
    "summary":"...",
    "missing_skills":[
        "...",
        "..."
    ],
    "interview_questions":[
        "...",
        "..."
    ],
    "learning_roadmap":[
        "...",
        "..."
    ],
    "project_ideas":[
        "...",
        "..."
    ]
}}

Resume:

{resume_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    content = response.choices[0].message.content

    # Remove markdown code fences if AI adds them
    content = content.replace("```json", "").replace("```", "").strip()

    return json.loads(content)