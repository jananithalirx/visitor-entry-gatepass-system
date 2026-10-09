# Visitor Entry & Gate Pass Management System

A full-stack visitor management system where visitors register, request digital gate passes, and get tracked through entry/exit — with an AI-powered anomaly detection layer flagging unusual visitor activity.

## Overview
Most offices still track visitor entries on paper — slow, unsearchable, and easy to falsify. This project digitizes the entire visitor lifecycle: registration, host approval, gate pass issuance, and entry/exit logging, plus an AI module that automatically flags risky patterns (overstaying, off-hours entry, repeated denials).

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React.js, Tailwind CSS, Axios |
| Backend | FastAPI (Python 3.14) |
| Auth | JWT (python-jose) + bcrypt password hashing |
| ORM / DB | SQLAlchemy + SQLite (dev) / PostgreSQL (prod) |
| Testing | Pytest |
| API Docs | FastAPI auto-generated Swagger (`/docs`) |
| CI/CD | GitHub Actions |
| Backend Hosting | Render |
| Frontend Hosting | Vercel |

## Features
- Visitor self-registration & login (JWT)
- Gate pass request & approval workflow
- Entry/exit logging at the gate
- Host notification on visitor arrival (Email/SMS)
- **AI/DS Enhancement:** Anomaly detection for irregular visitor activity

## Getting Started

### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python -m uvicorn app.main:app --reload
```
Backend runs at `http://localhost:8000` — Swagger docs at `http://localhost:8000/docs`.

## Environment Variables

| Name | Description | Required |
|---|---|---|
| `DATABASE_URL` | Database connection string | Y |
| `SECRET_KEY` | JWT signing secret | Y |

## Folder Structure