# 🧪 Testing Guide

> **Full manual for running and writing tests**

---

## 📋 Testing Structure

```
backend/
├── .venv/                   # Virtual Environment
├── test.ps1                 # Shortcut (Windows PowerShell)
├── test.bat                 # Shortcut (Windows CMD)
├── test.sh                  # Shortcut (Linux/Mac)
├── testes/                  # Test directory
│   ├── conftest.py          # Shared fixtures
│   └── test_casos_uso.py    # Business logic tests
```

---

## 🚀 Running Tests

### All tests with coverage

> [!IMPORTANT]
> To run `pytest` directly, you must first activate the virtual environment (`.venv\Scripts\activate`).
> Alternatively, use the **shortcut** below (Windows only).

```bash
cd backend

# Standard (needs venv)
pytest

# Quick (no venv needed)
.\test
```

### Specific tests

```bash
# A specific file
.\test testes/test_casos_uso.py

# A specific test
.\test testes/test_casos_uso.py::test_get_about_returns_correct_data

# Verbose mode
.\test -v

# With print output
.\test -s
```

### Coverage report

```bash
# Terminal
.\test --cov=app --cov-report=term-missing

# HTML (opens htmlcov/index.html)
.\test --cov=app --cov-report=html
```

---

## 📊 Current Metrics

| Metric | Value | Status |
|---------|-------|--------|
| **Total Tests** | 17 | ✅ |
| **Coverage** | >=85% | ✅ |
| **Minimum Goal** | 70% | ✅ |
| **Tested Lines** | 482/518 | ✅ |

---

## ✍️ Writing Tests

### Test Template

```python
import pytest
from httpx import AsyncClient

async def test_descriptive_name(client: AsyncClient):
    """Description of what is being tested."""
    # Arrange
    data = {"field": "value"}
    
    # Act
    response = await client.post("/api/v1/endpoint", json=data)
    
    # Assert
    assert response.status_code == 200
    assert response.json()["result"] == expected
```

### Available Fixtures

Defined in `conftest.py`:

```python
@pytest.fixture
async def client():
    """HTTP client for tests."""
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c
```

---

## 🎯 Best Practices

✅ **Clear naming**: `test_<action>_<returns>_<result>`  
✅ **One assert per concept**: Separate into different tests  
✅ **Independence**: Each test must run in isolation  
✅ **Arrange-Act-Assert**: Structure in 3 blocks  
✅ **Docstrings**: Explain complex cases  
---

## 🔍 Coverage Analysis

### Areas with lower coverage

| Module | Coverage | Action |
|--------|-----------|------|
| `email_adaptador.py` | 79% | Add SMTP error tests |
| `logger_adaptador.py` | 82% | Test different log levels |
| `repositorio.py` | 89% | Test corrupted file cases |

### How to improve

```bash
# Identify uncovered lines
.\test --cov=app --cov-report=term-missing
```

**Output example:**
```text
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
app/core/excecoes.py        14      4    71%   39, 62-65
```
> [!TIP]
> The "Missing" column shows exactly which lines need more tests!

---

## 🐛 Debugging Tests

### Failing test?

```bash
# View full output
.\test -vv -s

# Stop at first error
.\test -x

# Debug mode (pdb)
.\test --pdb
```

### Common error: AsyncIO

```python
# ❌ Wrong
def test_async():
    result = async_function()

# ✅ Correct
async def test_async():
    result = await async_function()
```

---

## 📝 PR Checklist

Before opening Pull Request:

- [ ] All tests pass: `.\test`
- [ ] Coverage >= 70%: `.\test --cov-fail-under=70`
- [ ] New features have tests
- [ ] Tests pass without warnings
- [ ] Tests documented with docstrings

---

## 🔄 CI/CD

Tests run automatically on GitHub Actions:

```yaml
# .github/workflows/backend-ci.yml
- name: 🧪 Run tests
  run: |
    cd backend
    pytest --cov=app --cov-fail-under=70
```

---

✅ **Keep coverage high and tests fast!**
