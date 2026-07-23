# AI Resume Analyzer

An AI-powered web app built using Flask and PostgreSQL that analyzes PDF resumes based on a target job role, using the Groq API. It extracts text from the resume, generates AI feedback, finds missing skills, gives interview questions, suggests a learning roadmap, and recommends project ideas.

## What It Does

You upload your resume as a PDF and enter the job role you're targeting. The app reads the text from your resume and sends it to an AI model (Llama 3.3 70B through Groq) along with the job role. It then gives back a summary of your resume, the skills you're missing for that role, some interview questions you might get asked, a roadmap of what to learn, and a few project ideas you could build. It also saves your past analyses so you can check them again later.

## Why I Built It

I was applying for jobs myself and using different resume tools to check my resume. I wanted to understand how these AI-based analysis tools actually work under the hood, instead of just using one. So I built my own version — one that takes a resume and a target job role, and uses an LLM to generate feedback like missing skills, interview questions, a learning roadmap, and project ideas.

This was as much about the build as the result — going from "upload a PDF" to "get structured AI feedback back" touches a lot of real-world skills: file handling, prompt design, API integration, auth, and a database, all in one project.

## What I Learned

- How to get an AI model to return proper structured output that I could actually use in the app, instead of just plain text
- How to extract text from PDFs properly, since not every resume format extracts cleanly
- How to build login and registration from scratch using Flask-Login, and hash passwords properly
- How to handle database changes using Flask-Migrate instead of manually changing tables every time
- How to organize a Flask project properly (models, routes, services) instead of writing everything in one file
- How to actually use a real AI API in a project, not just test it in a notebook — handling errors, slow responses, etc.



## Features

- User Registration & Login
- Secure Password Hashing
- Resume Upload (PDF)
- PDF Text Extraction (PyMuPDF)
- AI-Powered Resume Analysis
- Resume Summary Generation
- Missing Skills Detection
- Interview Question Suggestions
- Personalized Learning Roadmap
- Project Recommendations
- Analysis History
- Delete Resume
- PostgreSQL Database
- Responsive Bootstrap Dashboard

## Tech Stack

**Backend:** Python, Flask, SQLAlchemy, Flask-Login, Flask-Migrate
**Database:** PostgreSQL
**Frontend:** HTML, Bootstrap 5, Jinja2
**AI:** Groq API, Llama 3.3 70B Versatile
**Libraries:** PyMuPDF, Werkzeug

## Project Structure

```
AI-Resume-Analyzer/
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── templates/
│   └── migrations/
├── uploads/
├── config.py
├── run.py
└── requirements.txt
```

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
flask db upgrade
python run.py
```

## Future Improvements

- Resume score
- ATS compatibility score
- Resume comparison
- Cover letter generation
- Download PDF report
- Admin dashboard

## Author

**Sonia**
Built this as a portfolio project using Flask, PostgreSQL, and Groq AI.
