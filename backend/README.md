# 🎯 Portfolio Backend API

API REST desenvolvida com **FastAPI** seguindo **Clean Architecture** para demonstrar boas práticas de desenvolvimento backend em Python.

## 📝 Descrição

Backend profissional para portfólio de desenvolvedor, implementando:
- ✅ **Clean Architecture** simplificada (Controllers → Use Cases → Entities → Adapters)
- ✅ **Código 100% em Português Brasileiro** (variáveis, funções, docstrings, comentários)
- ✅ **Validação automática** com Pydantic V2
- ✅ **Documentação interativa** OpenAPI/Swagger
- ✅ **Testes automatizados** com pytest (cobertura > 70%)
- ✅ **Type hints completos** (mypy strict compatível)
- ✅ **Separação clara** de responsabilidades

---

## 🏗️ Arquitetura

### Clean Architecture Simplificada

```
┌─────────────────────────────────────────────────────┐
│  Controllers (HTTP Layer)                           │
│  - Recebe requisições                               │
│  - Valida entrada (Pydantic)                        │
│  - Retorna respostas HTTP                           │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│  Use Cases (Business Logic)                         │
│  - Orquestra lógica de negócio                      │
│  - SEM dependência de frameworks                    │
│  - Testável isoladamente                            │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│  Entities (Domain Models)                           │
│  - Modelos de domínio imutáveis                     │
│  - Lógica de negócio pura                           │
│  - Dataclasses Python                               │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│  Adapters (External Services)                       │
│  - Email (Formspree)                                │
│  - Storage (JSON files)                             │
│  - Logging                                          │
└─────────────────────────────────────────────────────┘
```

### Fluxo de Dados

1. **Request HTTP** → Controller
2. Controller **valida** (Pydantic) → Use Case
3. Use Case **executa lógica** → Entities/Adapters
4. Use Case **retorna dados** → Controller
5. Controller **retorna Response** HTTP

---

## 📂 Estrutura de Pastas

```
backend/
├── app/
│   ├── __init__.py
│   ├── principal.py              # Aplicação FastAPI
│   ├── configuracao.py           # Configurações (pydantic-settings)
│   │
│   ├── entidades/                # 🔵 Domínio (Entities)
│   │   ├── mensagem.py           # Mensagem de contato
│   │   ├── projeto.py            # Projeto do portfólio
│   │   └── experiencia.py        # Experiência profissional
│   │
│   ├── esquemas/                 # 🟢 Contratos HTTP (Schemas)
│   │   ├── saude.py              # Health check
│   │   ├── sobre.py              # Informações pessoais
│   │   ├── projetos.py           # Projetos
│   │   ├── stack.py              # Stack técnico
│   │   ├── experiencias.py       # Experiências
│   │   └── contato.py            # Formulário de contato
│   │
│   ├── casos_uso/                # 🟡 Lógica de Negócio (Use Cases)
│   │   ├── obter_sobre.py
│   │   ├── obter_projetos.py
│   │   ├── obter_stack.py
│   │   ├── obter_experiencias.py
│   │   └── enviar_contato.py
│   │
│   ├── adaptadores/              # 🔴 Serviços Externos (Adapters)
│   │   ├── email_adaptador.py    # Formspree
│   │   ├── repositorio.py        # Arquivos JSON
│   │   └── logger_adaptador.py   # Logging
│   │
│   └── controladores/            # 🟣 Rotas HTTP (Controllers)
│       ├── saude.py              # GET /saude
│       ├── api.py                # GET /api/*
│       └── contato.py            # POST /api/contato
│
├── dados/                        # 📁 Dados JSON
│   ├── sobre.json
│   ├── projetos.json
│   ├── stack.json
│   └── experiencias.json
│
├── testes/                       # 🧪 Testes
│   ├── conftest.py               # Fixtures
│   ├── test_casos_uso.py         # Testes de lógica
│   └── test_controladores.py    # Testes de endpoints
│
├── .env.exemplo                  # Variáveis de ambiente
├── requirements.txt              # Dependências
├── pytest.ini                    # Configuração pytest
└── README.md                     # Este arquivo
```

---

## 🚀 Como Rodar

### 1. Pré-requisitos

- **Python 3.11+**
- **pip** ou **uv**

### 2. Instalação

```bash
# Clone o repositório
git clone https://github.com/argenis972/Portf-lio.git
cd Portf-lio/backend

# Crie ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Instale dependências
pip install -r requirements.txt
```

### 3. Configuração

```bash
# Copie arquivo de exemplo
cp .env.exemplo .env

# Edite .env e configure (opcional):
# - FORMSPREE_FORM_ID (para funcionar o formulário de contato)
```

### 4. Executar

```bash
# Desenvolvimento (com hot reload)
uvicorn app.principal:app --reload --port 8000

# Produção
uvicorn app.principal:app --host 0.0.0.0 --port 8000
```

### 5. Acessar

- **API**: http://localhost:8000
- **Documentação Swagger**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/saude

---

## 📡 Endpoints

### Health Check

```http
GET /saude
```

Retorna status da API.

**Resposta 200:**
```json
{
  "status": "ok",
  "mensagem": "API funcionando normalmente"
}
```

---

### Informações Pessoais

```http
GET /api/sobre
```

Retorna dados da seção "Sobre Mim".

**Resposta 200:**
```json
{
  "nome": "Argenis Lopez",
  "titulo": "Backend Developer | Python | FastAPI",
  "email": "argenislopez28708256@gmail.com",
  "github": "https://github.com/argenis972",
  ...
}
```

---

### Listar Projetos

```http
GET /api/projetos
```

Retorna lista resumida de projetos (destacados primeiro).

**Resposta 200:**
```json
{
  "projetos": [
    {
      "id": "portfolio-api",
      "nome": "Portfolio API",
      "descricao_curta": "API REST com FastAPI...",
      "tecnologias": ["Python", "FastAPI"],
      "destaque": true
    }
  ],
  "total": 3
}
```

---

### Detalhes de Projeto

```http
GET /api/projetos/{projeto_id}
```

Retorna informações completas de um projeto.

**Resposta 200:**
```json
{
  "id": "portfolio-api",
  "nome": "Portfolio API",
  "descricao_completa": "...",
  "tecnologias": [...],
  "funcionalidades": [...],
  "aprendizados": [...],
  "repositorio": "https://github.com/...",
  "demo": null
}
```

**Resposta 404:** Projeto não encontrado

---

### Stack Tecnológico

```http
GET /api/stack
```

Retorna tecnologias organizadas por categoria.

**Resposta 200:**
```json
{
  "stack": [...],
  "por_categoria": {
    "backend": [
      {"nome": "Python", "nivel": 4, "categoria": "backend"}
    ],
    "frontend": [...],
    "devops": [...]
  }
}
```

---

### Experiências Profissionais

```http
GET /api/experiencias
```

Retorna lista de experiências (mais recente primeiro).

**Resposta 200:**
```json
{
  "experiencias": [
    {
      "id": "exp-001",
      "cargo": "Backend Developer Freelancer",
      "empresa": "Autônomo",
      "data_inicio": "2023-06-01",
      "data_fim": null,
      "atual": true,
      "tecnologias": ["Python", "FastAPI"]
    }
  ],
  "total": 2
}
```

---

### Enviar Mensagem de Contato

```http
POST /api/contato
```

Envia mensagem do formulário de contato.

**Body:**
```json
{
  "nome": "Maria Silva",
  "email": "maria@empresa.com",
  "assunto": "Oportunidade de trabalho",
  "mensagem": "Olá, gostaria de conversar sobre..."
}
```

**Resposta 200:**
```json
{
  "sucesso": true,
  "mensagem": "Mensagem enviada com sucesso!"
}
```

**Resposta 422:** Dados inválidos  
**Resposta 500:** Erro ao enviar (verificar `FORMSPREE_FORM_ID`)

---

## 🧪 Testes

### Rodar Todos os Testes

```bash
pytest
```

### Com Cobertura

```bash
pytest --cov=app --cov-report=html
```

### Apenas Casos de Uso

```bash
pytest testes/test_casos_uso.py
```

### Apenas Controladores

```bash
pytest testes/test_controladores.py
```

### Estrutura de Testes

- **`conftest.py`**: Fixtures reutilizáveis (mocks)
- **`test_casos_uso.py`**: Testa lógica de negócio isoladamente
- **`test_controladores.py`**: Testa endpoints HTTP com TestClient

**Cobertura mínima:** 70% (configurado em `pytest.ini`)

---

## 🎓 Decisões Técnicas

### Por que Clean Architecture?

✅ **Testabilidade**: Lógica de negócio sem dependência de HTTP  
✅ **Manutenibilidade**: Fácil entender e modificar  
✅ **Flexibilidade**: Trocar Formspree → SendGrid muda 1 arquivo  
✅ **Profissionalismo**: Arquitetura defendível em entrevistas

### Por que Português no Código?

✅ **Contexto nacional**: Código alinhado ao mercado brasileiro  
✅ **Clareza**: Menos "tradução mental" ao ler  
✅ **Consistência**: Domínio e código na mesma língua

### Por que Pydantic V2?

✅ **Validação automática** de entrada/saída  
✅ **Documentação OpenAPI** gerada automaticamente  
✅ **Type safety** com mypy  
✅ **Performance** (core em Rust)

### Por que Dataclasses Imutáveis?

✅ **Consistência**: Dados não mudam após criação  
✅ **Thread-safe**: Seguro em contextos assíncronos  
✅ **Simplicidade**: Menos bugs relacionados a estado

### Por que JSON ao invés de Banco de Dados?

✅ **Simplicidade**: Portfólio não precisa de banco complexo  
✅ **Versionamento**: Dados ficam no git  
✅ **Demonstração**: Foco em arquitetura, não em banco  
✅ **Fácil trocar**: Interface `RepositorioPortfolio` permite trocar implementação

---

## 📚 Dependências

```
fastapi==0.115.6          # Framework web
uvicorn[standard]==0.34.0 # Servidor ASGI
pydantic==2.10.4          # Validação de dados
pydantic-settings==2.7.0  # Configurações
httpx==0.28.1             # Cliente HTTP async
pytest==8.3.4             # Framework de testes
pytest-asyncio==0.24.0    # Testes async
pytest-cov==6.0.0         # Cobertura de testes
python-dotenv==1.0.1      # Variáveis de ambiente
python-dateutil==2.9.0    # Manipulação de datas
```

---

## 🔄 Próximos Passos

- [ ] Implementar autenticação JWT
- [ ] Adicionar rate limiting
- [ ] Integrar com banco de dados (PostgreSQL)
- [ ] Deploy em Railway/Render
- [ ] CI/CD com GitHub Actions
- [ ] Logs estruturados (structlog)
- [ ] Monitoramento (Sentry)
- [ ] Cache com Redis
- [ ] Versionamento de API (v1, v2)
- [ ] Internacionalização (i18n)

---

## 📖 Referências

- **Clean Architecture**: [The Clean Architecture (Uncle Bob)](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- **FastAPI**: [FastAPI Documentation](https://fastapi.tiangolo.com/)
- **Pydantic V2**: [Pydantic Docs](https://docs.pydantic.dev/latest/)
- **Pytest**: [Pytest Documentation](https://docs.pytest.org/)

---

## 👨‍💻 Autor

**Argenis Lopez**  
Backend Developer | Python | FastAPI | Clean Architecture

- 📧 Email: argenislopez28708256@gmail.com
- 🐙 GitHub: [@argenis972](https://github.com/argenis972)
- 💼 LinkedIn: [argenis972](https://linkedin.com/in/argenis972)

---

## 📄 Licença

Este projeto é open source e está disponível para fins educacionais e demonstração de habilidades técnicas.

---

**Desenvolvido com ❤️ e Clean Architecture**
