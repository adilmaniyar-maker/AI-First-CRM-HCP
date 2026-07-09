# 🏥 AI-First CRM for Healthcare Professionals (HCP)

An AI-powered Customer Relationship Management (CRM) system built for Healthcare Professionals (HCPs). This application enables pharmaceutical representatives to manage doctor profiles, log interactions, and generate AI-powered insights using Groq LLM and LangGraph.

---

## 🚀 Features

### 👨‍⚕️ HCP Management
- Create HCP
- View all HCPs
- View HCP by ID
- Update HCP
- Delete HCP

### 📝 Interaction Management
- Log doctor interactions
- View interaction history
- Update interactions
- Delete interactions

### 🤖 AI Features
- AI-generated interaction summary
- Sentiment analysis (Positive / Neutral / Negative)
- AI-generated next best action
- LangGraph workflow integration
- Groq LLM integration

### 🏗 Backend Architecture
- FastAPI
- SQLAlchemy ORM
- MySQL Database
- Repository Pattern
- Service Layer Architecture
- REST APIs
- Swagger Documentation

---

# 🛠 Tech Stack

- Python 3.12
- FastAPI
- MySQL
- SQLAlchemy
- Pydantic
- Groq API
- LangGraph
- LangChain
- Uvicorn
- Python Dotenv

---

# 📂 Project Structure

```text
backend/
│
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── hcp.py
│   │       └── interaction.py
│   │
│   ├── agents/
│   │       ├── crm_agent.py
│   │       ├── graph.py
│   │       └── state.py
│   │
│   ├── database/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── tools/
│
├── main.py
├── requirements.txt
└── .env
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-First-CRM-HCP.git
```

Go to project

```bash
cd AI-First-CRM-HCP/backend
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
DATABASE_URL=mysql+pymysql://username:password@localhost/database_name
```

Run the application

```bash
uvicorn main:app --reload
```

Open Swagger

```
http://127.0.0.1:8000/docs
```

---

# 🧠 AI Workflow

```
Doctor Interaction
        │
        ▼
FastAPI API
        │
        ▼
LangGraph Workflow
        │
 ┌───────────────┬───────────────┬───────────────┐
 ▼               ▼               ▼
Summary      Sentiment      Next Action
        │
        ▼
Store in MySQL
        │
        ▼
Return API Response
```

---

# 📌 API Endpoints

## HCP APIs

| Method | Endpoint |
|---------|----------|
| POST | /hcp |
| GET | /hcp |
| GET | /hcp/{id} |
| PUT | /hcp/{id} |
| DELETE | /hcp/{id} |

---

## Interaction APIs

| Method | Endpoint |
|---------|----------|
| POST | /interactions |
| GET | /interactions |
| GET | /interactions/{id} |
| PUT | /interactions/{id} |
| DELETE | /interactions/{id} |

---

# 📈 Future Enhancements

- JWT Authentication
- Role-Based Access Control
- React Dashboard
- Docker Deployment
- Analytics Dashboard
- Email Notifications
- Multi-Agent AI Workflow
- Cloud Deployment

---

# 👨‍💻 Author

**Adil Maniyar**

Data Analyst | AI Developer | FastAPI | Python | SQL | LangGraph | Groq AI

---

# ⭐ If you found this project useful, please consider giving it a Star.


<img width="1882" height="907" alt="Screenshot 2026-07-09 224139" src="https://github.com/user-attachments/assets/590b2b6e-5d99-480f-9892-0f0997638abd" />

