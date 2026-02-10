# 🧪 Guia de Testes

> **Manual completo para execução e escrita de testes**

---

## 📋 Estrutura de Testes

```
backend/testes/
├── conftest.py              # Fixtures compartilhadas
├── test_casos_uso.py        # Testes de lógica de negócio
└── test_controladores.py    # Testes de endpoints HTTP
```

---

## 🚀 Executando Testes

### Todos os testes com cobertura

```bash
cd backend
pytest
```

### Testes específicos

```bash
# Um arquivo específico
pytest testes/test_casos_uso.py

# Um teste específico
pytest testes/test_casos_uso.py::test_obter_sobre_retorna_dados_corretos

# Modo verbose
pytest -v

# Com output de print
pytest -s
```

### Relatório de cobertura

```bash
# Terminal
pytest --cov=app --cov-report=term-missing

# HTML (abre htmlcov/index.html)
pytest --cov=app --cov-report=html
```

---

## 📊 Métricas Atuais

| Métrica | Valor | Status |
|---------|-------|--------|
| **Total de Testes** | 17 | ✅ |
| **Cobertura** | 93.05% | ✅ |
| **Meta Mínima** | 70% | ✅ |
| **Linhas Testadas** | 482/518 | ✅ |

---

## ✍️ Escrevendo Testes

### Template de Teste

```python
import pytest
from httpx import AsyncClient

async def test_nome_descritivo(cliente: AsyncClient):
    """Descrição do que está sendo testado."""
    # Arrange (preparar)
    dados = {"campo": "valor"}
    
    # Act (executar)
    response = await cliente.post("/api/v1/endpoint", json=dados)
    
    # Assert (verificar)
    assert response.status_code == 200
    assert response.json()["resultado"] == esperado
```

### Fixtures Disponíveis

Definidas em `conftest.py`:

```python
@pytest.fixture
async def cliente():
    """Cliente HTTP para testes."""
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c
```

---

## 🎯 Boas Práticas

✅ **Nomenclatura clara**: `test_<acao>_<retorna>_<resultado>`  
✅ **Um assert por conceito**: Separe em testes diferentes  
✅ **Independência**: Cada teste deve rodar isoladamente  
✅ **Arrange-Act-Assert**: Estruture em 3 blocos  
✅ **Docstrings**: Explique casos complexos  

---

## 🔍 Análise de Cobertura

### Áreas com menor cobertura

| Módulo | Cobertura | Ação |
|--------|-----------|------|
| `email_adaptador.py` | 79% | Adicionar testes de erro SMTP |
| `logger_adaptador.py` | 82% | Testar diferentes níveis de log |
| `repositorio.py` | 89% | Testar casos de arquivo corrompido |

### Como melhorar

```bash
# Identificar linhas não cobertas
pytest --cov=app --cov-report=term-missing

# Exemplo de output:
# app/core/excecoes.py    71%   39, 62-65
#                                ^^ adicione testes para essas linhas
```

---

## 🐛 Debugging Testes

### Teste falhando?

```bash
# Ver output completo
pytest -vv -s

# Parar no primeiro erro
pytest -x

# Modo debug (pdb)
pytest --pdb
```

### Erro comum: AsyncIO

```python
# ❌ Errado
def test_async():
    resultado = funcao_async()

# ✅ Correto
async def test_async():
    resultado = await funcao_async()
```

---

## 📝 Checklist de PR

Antes de abrir Pull Request:

- [ ] Todos os testes passam: `pytest`
- [ ] Cobertura >= 70%: `pytest --cov-fail-under=70`
- [ ] Novos features têm testes
- [ ] Testes passam sem warnings
- [ ] Testes documentados com docstrings

---

## 🔄 CI/CD

Testes rodam automaticamente no GitHub Actions:

```yaml
# .github/workflows/backend-ci.yml
- name: 🧪 Executar testes
  run: |
    cd backend
    pytest --cov=app --cov-fail-under=70
```

---

✅ **Mantenha a cobertura alta e os testes rápidos!**
