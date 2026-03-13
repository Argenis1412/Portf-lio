# 🚀 Professional Portfolio Backend

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](.)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Professional REST API system built with FastAPI, focusing on Clean Architecture and production-ready backend standards.**

This repository serves as a robust backend foundation for a developer portfolio, demonstrating advanced Python patterns and scalable architecture.

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

<a id="overview"></a>
## 🎯 Overview

Professional portfolio system developed to demonstrate skills in:

- **Core**: Professional REST API with FastAPI, Clean Architecture, and robust validation.
- **Quality**: Automated tests (>=85% coverage), strict typing, and standardized patterns.
- **Production**: Structured logging, health monitoring, and performance middleware.
- **Documentation**: Interactive OpenAPI/Swagger and detailed implementation guides.
- **DevOps**: Docker integration and automated CI/CD pipelines.

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
🎨 **Frontend Component**: React + TypeScript client included as an API consumer (in development)

---

<a id="architecture"></a>
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

<a id="technologies"></a>
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

<a id="project-structure"></a>
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

<a id="quick-start"></a>
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
# (Standard needs venv active)
pytest
# (Quick Windows shortcut)
.\test

# Start the server
uvicorn app.principal:app --reload
```

🌐 API available at: **http://localhost:8000**  
📚 Documentation: **http://localhost:8000/docs**

---

<a id="documentation"></a>
## 📖 Documentation

### Backend

- **[Detailed README](backend/README.md)**: Architecture, endpoints, examples.
- **[Swagger UI](http://localhost:8000/docs)**: Interactive documentation.
- **[ReDoc](http://localhost:8000/redoc)**: Alternative documentation.

---

<a id="contributing"></a>
## 🤝 Contributing

Contributions are welcome!

1. **Report bugs** via Issues.
2. **Suggest improvements** via Issues.
3. **Submit PRs** with fixes/features.

---

<a id="license"></a>
## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Argenis Lopez**

- 💼 LinkedIn: [LinkedIn](https://www.linkedin.com/in/argenis972/)
- 🐙 GitHub: [Argenis1412](https://github.com/Argenis1412)
