# 🧭 Sovereign Career Architect (SCA)

> A Professional Intelligence Platform that turns career evidence into measurable career strategy.

**Developed by ANIREX AI**

## What is SCA?

Sovereign Career Architect (SCA) is designed to move beyond the traditional CV or resume.

Instead of treating a career as a static document, SCA models a professional through:

- Skills
- Experience
- Education
- Projects
- Goals
- Achievements
- Certificates
- Timeline
- Career intelligence

SCA is designed to answer:

> **Where am I now, where am I trying to go, what is missing, and what should I do next?**

## SCA V1 Workflow

```text
Professional Profile
        ↓
Career Analysis
        ↓
Skill Gap Analysis
        ↓
Career Insights
        ↓
Strategic Recommendations
        ↓
Career Roadmap
        ↓
Market Intelligence
```

## V1 Features

### Professional Management

- Create Professional
- Read Professional
- Update Professional
- Delete Professional

### Professional Evidence

- Skills
- Education
- Experience
- Projects
- Goals
- Achievements
- Certificates
- Timeline Events

### Career Intelligence

- Career Score
- Profile Completion
- Career Readiness
- Skill Gap Analysis
- Career Insights
- Strategic Recommendations
- Career Roadmap
- Market Intelligence

## Architecture

SCA Core follows Clean Architecture and Domain-Driven Design principles.

```text
Streamlit Dashboard
        ↓
     FastAPI
        ↓
 Application Layer
        ↓
   Domain Layer
        ↓
 Infrastructure
        ↓
 SQLite + SQLAlchemy
        ↓
     Alembic
```

## Technology Stack

- Python
- FastAPI
- Streamlit
- Pydantic
- SQLAlchemy
- SQLite
- Alembic
- Pytest
- Clean Architecture
- Domain-Driven Design

## Run SCA

### Start the API

```powershell
uvicorn app.main:app --reload
```

API: http://127.0.0.1:8000

Swagger: http://127.0.0.1:8000/docs

Health: http://127.0.0.1:8000/health

### Start the Dashboard

Open another terminal:

```powershell
streamlit run dashboard.py
```

Dashboard: http://localhost:8501

## Testing

```powershell
pytest -q
```

Verified V1 result:

```text
216 passed
```

Migration verification:

```powershell
alembic check
```

Expected:

```text
No new upgrade operations detected.
```

## Career Intelligence API

```text
POST /career-intelligence/{professional_id}/analysis
GET  /career-intelligence/{professional_id}/analysis
GET  /career-intelligence/{professional_id}/insights
GET  /career-intelligence/{professional_id}/recommendations
GET  /career-intelligence/{professional_id}/roadmap
GET  /career-intelligence/{professional_id}/market-intelligence
```

## V1 Scope

SCA V1 uses deterministic intelligence components in several areas.

Market Intelligence currently uses the V1 market-signal implementation.

Future versions are intended to expand toward:

- AI-assisted career reasoning
- Live job-market intelligence
- Autonomous market scouting
- Persistent career memory
- Personalised learning intelligence
- Richer evidence modelling
- AI agents such as Librarian, Scout, Ledger and Architect

## Long-Term Vision

> **A Professional Operating System for individuals and organisations.**

The long-term system should understand:

```text
Who you are
What you know
What you have demonstrated
What you want
What the market needs
What is missing
What you should do next
```

## 🇳🇵 Built from Nepal

SCA is being developed by **ANIREX AI** from Nepal, with the ambition of building a globally useful Professional Intelligence Platform.

## ✅ V1 Status

**SCA Core V1 MVP**

- ✅ Clean Architecture
- ✅ Domain-Driven Design foundation
- ✅ Professional aggregate
- ✅ Professional evidence management
- ✅ Career Intelligence
- ✅ Market Intelligence
- ✅ FastAPI API
- ✅ Streamlit dashboard
- ✅ SQLite persistence
- ✅ Alembic migrations
- ✅ Automated tests
- ✅ API health check
- ✅ GitHub repository

## 👤 Developer

**Anil Khanal**

Founder / Builder — **ANIREX AI**

## 📄 License

Licensing will be defined as the product moves toward its public release strategy.