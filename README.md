# 🤖 AI Resume Analyzer

An AI-powered web application built with Flask and PostgreSQL that analyzes PDF resumes against a target job role using the Groq API. The application extracts resume text, generates structured AI feedback, identifies missing skills, suggests interview questions, creates a learning roadmap, and recommends project ideas.


## 🚀 Features

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


## 🛠 Tech Stack

### Backend
- Python
- Flask
- SQLAlchemy
- Flask-Login
- Flask-Migrate

### Database
- PostgreSQL

### Frontend
- HTML
- Bootstrap 5
- Jinja2

### AI
- Groq API
- Llama 3.3 70B Versatile

### Libraries
- PyMuPDF
- Werkzeug


## 📂 Project Structure

AI-Resume-Analyzer/
│
├── app/
│ ├── models/
│ ├── routes/
│ ├── services/
│ ├── templates/
│
├── migrations/
├── uploads/
├── config.py
├── run.py
├── requirements.txt

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git

cd AI-Resume-Analyzer

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

flask db upgrade

python run.py
```

---

## 📸 Screenshots

(Add screenshots after deployment.)

---

## 🎯 Future Improvements

- Resume score
- ATS compatibility score
- Resume comparison
- Cover letter generation
- Download PDF report
- Admin dashboard

---

## 👩‍💻 Author

**Sonia**

Built as a portfolio project using Flask, PostgreSQL and Gorq AI

## 📄 License

This project is for educational and portfolio purposes.