# 🚀 Professional Portfolio

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](.)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Complete professional portfolio system with FastAPI backend and modern frontend.**

This repository contains a full-stack portfolio system built with Clean Architecture best practices, separation of concerns, and production-ready configuration.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

Professional portfolio system developed to demonstrate skills in:

- **Backend**: REST API with FastAPI, Clean Architecture, robust validation.
- **Quality**: Automated tests (93%+ coverage), linting, standardization.
- **Production**: Structured logging, monitoring, error handling.
- **Documentation**: Interactive OpenAPI/Swagger, detailed READMEs.
- **DevOps**: Containerization (Docker), CI/CD.

### 🌟 Key Features

✅ **Complete REST API** with versioning (`/api/v1/`)  
✅ **Professional Experience Management**  
✅ **Project Showcase** with technical details  
✅ **Contact System** with email sending integration  
✅ **Professional Health Check** with uptime metrics  
✅ **Standardized Error Handling** with custom error codes  
✅ **Observability Middleware** (Request ID, structured logging, performance timing)  
✅ **Structured Logs** with structlog (JSON in production, Console in dev)  
✅ **CI/CD with GitHub Actions** (tests, lint, build)  
✅ **Deployment Ready** for platforms like Railway/Render  
⏳ **Frontend in React + TypeScript** (in development)

---

## 🏗️ Architecture

The project follows **Clean Architecture** principles with clear layer separation:

```
┌─────────────────────────────────────────────┐
│           Interface Layer                   │
│         (Controllers/Routers)               │
│   → Handles HTTP requests                   │
│   → Validates input with Pydantic           │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│           Use Case Layer                    │
│      (Business Logic/Use Cases)             │
│   → Orchestrates business logic             │
│   → Independent of frameworks               │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│           Entity Layer                      │
│         (Domain Models)                     │
│   → Pure business rules                     │
│   → Domain validations                      │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│           Adapter Layer                     │
│    (Repositories/Services)                  │
│   → Data access (JSON, DB)                  │
│   → External integrations (Email)           │
└─────────────────────────────────────────────┘
```

### Benefits

- 🔄 **Testability**: Each layer can be tested in isolation.
- 🔌 **Decoupling**: Easy to swap implementations (e.g., JSON → Database).
- 📦 **Maintainability**: Organized and localized code.
- 🎯 **Scalability**: Structure ready for growth.

---

## 🛠️ Technologies

### Backend

| Technology | Version | Purpose |
|-----------|--------|-----------|
| **Python** | 3.12 | Core language |
| **FastAPI** | 0.115+ | Async web framework |
| **Pydantic** | 2.10+ | Data validation |
| **Uvicorn** | 0.34+ | ASGI server |
| **pytest** | 8.3+ | Test framework |
| **pytest-cov** | 6.0+ | Code coverage |

### Frontend *(in development)*

| Technology | Version | Purpose |
|-----------|--------|-----------|
| **React** | 18+ | UI library |
| **TypeScript** | 5+ | Static typing |
| **Vite** | 7+ | Build tool |
| **TailwindCSS** | 3+ | Styling |

---

## 📁 Project Structure

```
portfolio/
│
├── backend/                    # FastAPI API
│   ├── app/
│   │   ├── core/              # Core (exceptions, middleware, limits)
│   │   ├── controladores/     # HTTP Endpoints (Controllers)
│   │   ├── casos_uso/         # Business logic (Use Cases)
│   │   ├── entidades/         # Domain models (Entities)
│   │   ├── esquemas/          # Pydantic Schemas
│   │   └── adaptadores/       # Repositories, external services
│   ├── dados/                 # JSON persistence
│   ├── testes/                # Automated tests
│   ├── requirements.txt       # Python dependencies
│   └── README.md              # Detailed documentation
│
├── frontend/                  # React Application (in dev)
│   ├── src/
│   ├── package.json
│   └── README.md
│
├── .github/                   # GitHub workflows
│   └── workflows/
│       ├── backend-ci.yml     # CI for backend
│
├── .gitignore                 # Ignored files
├── .env.example               # Environment variables example
├── LICENSE                    # MIT License
├── docker-compose.yml         # Container orchestration
└── README.md                  # This file
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.12** installed
- **Git** configured

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Argenis1412/Portf-lio.git
cd portfolio
```

### 2️⃣ Configure the Backend

```bash
cd backend

# Create a virtual environment
py -3.12 -m venv .venv  # Windows (recommended)
# or: python -m venv .venv

# Activate the environment (Windows)
.venv\Scripts\activate

# Activate the environment (Linux/Mac)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Start the server
uvicorn app.principal:app --reload
```

🌐 API available at: **http://localhost:8000**  
📚 Documentation: **http://localhost:8000/docs**

---

## 📖 Documentation

### Backend

- **[Detailed README](backend/README.md)**: Architecture, endpoints, examples.
- **[Swagger UI](http://localhost:8000/docs)**: Interactive documentation.
- **[ReDoc](http://localhost:8000/redoc)**: Alternative documentation.

---

## 🤝 Contributing

Contributions are welcome!

1. **Report bugs** via Issues.
2. **Suggest improvements** via Issues.
3. **Submit PRs** with fixes/features.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Argenis Lopez**

- 💼 LinkedIn: [LinkedIn](https://www.linkedin.com/in/argenis972/)
- 🐙 GitHub: [Argenis1412](https://github.com/Argenis1412)
