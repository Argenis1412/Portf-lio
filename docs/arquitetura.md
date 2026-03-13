# 🏗️ Architectural Decisions

> **Architectural Decision Record (ADR)**  
> This file documents the main technical decisions of the project and their motivations.

---

## 📚 Table of Contents

1. [Clean Architecture](#1-clean-architecture)
2. [JSON Persistence](#2-json-persistence)
3. [FastAPI as Framework](#3-fastapi-as-framework)
4. [API Versioning](#4-api-versioning)
5. [Custom Error Handling](#5-custom-error-handling)

---

## 1. Clean Architecture

### Context
We needed an architecture that would allow for scalability, testability, and long-term maintainability.

### Decision
Adopted **Clean Architecture** with layer separation:
- **Controllers** (interface layer)
- **Use Cases** (business logic)
- **Entities** (domain models)
- **Adapters** (repositories and external services)

### Consequences

**Positive:**
- ✅ Highly testable code (93%+ coverage)
- ✅ Easy dependency swapping (Future JSON → PostgreSQL)
- ✅ Business logic isolated from frameworks

**Negative:**
- ⚠️ Higher initial complexity
- ⚠️ More files to manage

### Status
✅ **Implemented** - Working in production

---

## 2. JSON Persistence

### Context
Initial phase project, need for simplicity without complex infrastructure.

### Decision
Use **JSON files** for data persistence (`dados/projetos.json`, etc.).

### Consequences

**Positive:**
- ✅ Zero database configuration
- ✅ Easy data versioning in Git
- ✅ Ideal for static portfolio

**Negative:**
- ⚠️ Does not scale for high write volume
- ⚠️ No ACID transactions
- ⚠️ Less efficient search

### Future Migration
Prepared for PostgreSQL migration via the Repository pattern:

```python
# Current interface
class Repository:
    def get_all(self) -> List[T]: ...

# Future implementation
class RepositoryPG(Repository):
    def get_all(self) -> List[T]:
        return session.query(Model).all()
```

### Status
✅ **Implemented** - Sufficient for MVP

---

## 3. FastAPI as Framework

### Context
Need for a modern framework with automatic validation, documentation, and performance.

### Decision
Choose **FastAPI** over Flask/Django.

### Reasons

| Criterion | FastAPI | Flask | Django |
|----------|---------|-------|--------|
| Performance | ⚡ Asynchronous | 🐌 Sync | 🐌 Sync |
| Validation | ✅ Pydantic | ❌ Manual | ⚠️ Forms |
| Auto Docs | ✅ OpenAPI | ❌ No | ❌ No |
| Type Hints | ✅ Native | ⚠️ Optional | ⚠️ Optional |
| Learning Curve | 📘 Medium | 📗 Easy | 📕 High |

### Consequences

**Positive:**
- ✅ Automatic Swagger documentation
- ✅ Free input/output validation
- ✅ Better performance in asynchronous I/O

**Negative:**
- ⚠️ Smaller ecosystem than Django
- ⚠️ Fewer third-party libraries

### Status
✅ **Implemented** - Excellent choice

---

## 4. API Versioning

### Context
Production APIs need to evolve without breaking existing clients.

### Decision
Implement versioning via **URL path** (`/api/v1/projetos`).

### Considered Alternatives

| Strategy | Pros | Cons | Decision |
|-----------|------|---------|---------|
| **URL Path** | 🟢 Explicit, easy cache | 🔴 Code duplication | ✅ **Chosen** |
| Header | 🟢 Clean URL | 🔴 Hard to test in browser | ❌ |
| Query Param | 🟢 Easy to implement | 🔴 Inconsistent | ❌ |

### Implementation

```python
# backend/app/controladores/v1.py
router_v1 = APIRouter(prefix="/api/v1")

# Future v2 will have changes without breaking v1
router_v2 = APIRouter(prefix="/api/v2")
```

### Status
✅ **Implemented** - Ready for evolution

---

## 5. Custom Error Handling

### Context
Default FastAPI errors (`{"detail": "..."}`) do not provide structured information for the frontend.

### Decision
Create a **hierarchy of custom exceptions** with error codes:

```json
{
    "error": {
        "code": "PROJECT_NOT_FOUND",
        "message": "Project 'xyz' does not exist",
        "details": {...}
    }
}
```

### Consequences

**Positive:**
- ✅ Frontend can handle specific errors
- ✅ Facilitates internationalization
- ✅ Structured logging

**Negative:**
- ⚠️ More code to maintain

### Error Codes

| Code | HTTP | Description |
|--------|------|-----------|
| `PROJECT_NOT_FOUND` | 404 | Project does not exist |
| `INPUT_VALIDATION_ERROR` | 422 | Invalid data |
| `EMAIL_SEND_ERROR` | 500 | Sending failure |

### Status
✅ **Implemented** - 100% of endpoints

---

## 📝 Template for New Decisions

```markdown
## N. [DECISION TITLE]

### Context
[Situation that motivated the decision]

### Decision
[What was decided]

### Consequences
**Positive:**
- ✅ [Benefit 1]

**Negative:**
- ⚠️ [Cost 1]

### Status
[✅ Implemented | 🚧 In progress | ❌ Reverted]
```

---

## 🔄 Revision History

| Date | Version | Author | Change |
|------|--------|-------|---------|
| 2025-01-XX | 1.0 | [Your Name] | Initial version |

---

**Note**: This document should be updated whenever a significant technical decision is made.
