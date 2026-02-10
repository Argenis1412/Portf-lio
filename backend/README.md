# 🎯 Portfolio Backend API

API REST desenvolvida com **FastAPI** seguindo **Clean Architecture** para demonstrar boas práticas de desenvolvimento backend em Python.

## 📝 Descrição

Backend profissional para portfólio de desenvolvedor, implementando:
- ✅ **Clean Architecture** simplificada (Controllers → Use Cases → Entities → Adapters)
- ✅ **API Versionada** (/api/v1/*)
- ✅ **Error Handling Global** com exceções customizadas
- ✅ **Middleware** com request_id, logging e medição de performance
- ✅ **Health Check** profissional com uptime e versão
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

### Camadas Transversais (Core)

```
┌──────────────────────────────────────────────────────┐
│  Core (Cross-cutting Concerns)                       │
│  - Exceções customizadas                             │
│  - Handlers globais de erros                         │
│  - Middleware (request_id, logging, timing)          │
│  - Configurações centralizadas                       │
└──────────────────────────────────────────────────────┘
```

### Fluxo de Request

```
1. Request HTTP
   ↓
2. Middleware (adiciona request_id, loga entrada)
   ↓
3. Controller (v alida Pydantic)
   ↓
4. Use Case (executa lógica)
   ↓
5. Adapter (acessa dados/serviços externos)
   ↓
6. Retorna Response
   ↓
7. Middleware (loga saída, adiciona headers)
   ↓
8. Cliente recebe resposta + X-Request-ID + X-Response-Time
```

---

## 📂 Estrutura de Pastas

```
backend/
├── app/
│   ├── __init__.py
│   ├── principal.py              # Aplicação FastAPI
│   ├── configuracao.py           # Configurações (pydantic-settings)
│   │
│   ├── core/                     # 🔷 Camada Transversal
│   │   ├── __init__.py
│   │   ├── excecoes.py           # Exceções customizadas
│   │   ├── handlers.py           # Handlers globais de erro
│   │   └── middleware.py         # Request ID, logging, timing
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
│       ├── api.py                # Endpoints de dados
│       ├── contato.py            # POST /contato
│       └── v1.py                 # Router API v1
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

## 📋 Contratos HTTP

### Padrão de Resposta de Sucesso

Todas as respostas de sucesso retornam dados validados pelo Pydantic diretamente:

```json
{
  "campo1": "valor1",
  "campo2": "valor2"
}
```

### Padrão de Resposta de Erro

Todas as respostas de erro seguem estrutura padronizada:

```json
{
  "erro": {
    "codigo": "CODIGO_INTERNO",
    "mensagem": "Descrição legível do erro",
    "detalhes": {}  // Opcional: informações adicionais
  }
}
```

### Códigos HTTP

| Código | Significado | Uso |
|--------|-------------|-----|
| `200` | OK | Requisição bem-sucedida |
| `400` | Bad Request | Erro de regra de negócio/domínio |
| `404` | Not Found | Recurso não encontrado |
| `422` | Unprocessable Entity | Validação de entrada falhou |
| `500` | Internal Server Error | Erro inesperado do servidor |

### Headers Customizados

Toda resposta inclui headers adicionais para rastreamento:

```http
X-Request-ID: 550e8400-e29b-41d4-a716-446655440000
X-Response-Time: 45.23ms
```

**`X-Request-ID`**: UUID único para rastreamento de log  
**`X-Response-Time`**: Tempo de processamento em milissegundos

---

## ⚠️ Tratamento de Erros

### Hierarquia de Exceções

```
Exception
├── ErroDominio (400 Bad Request)
│   ├── ErroValidacao (422 Unprocessable Entity)
│   └── ErroRecursoNaoEncontrado (404 Not Found)
└── ErroInfraestrutura (500 Internal Server Error)
```

### Exemplos de Erros

#### Recurso Não Encontrado (404)

```http
GET /api/v1/projetos/xyz
```

```json
 {
  "erro": {
    "codigo": "PROJETO_NAO_ENCONTRADO",
    "mensagem": "Projeto 'xyz' não encontrado"
  }
}
```

#### Validação de Entrada (422)

```http
POST /api/v1/contato
Content-Type: application/json

{
  "nome": "",
  "email": "invalido"
}
```

```json
{
  "erro": {
    "codigo": "ERRO_VALIDACAO_ENTRADA",
    "mensagem": "Dados de entrada inválidos",
    "detalhes": [
      {
        "campo": "nome",
        "mensagem": "ensure this value has at least 1 characters",
        "tipo": "value_error.any_str.min_length"
      },
      {
        "campo": "email",
        "mensagem": "value is not a valid email address",
        "tipo": "value_error.email"
      }
    ]
  }
}
```

#### Erro Interno (500)

```json
{
  "erro": {
    "codigo": "ERRO_INTERNO",
    "mensagem": "Erro interno do servidor. Tente novamente mais tarde."
  }
}
```

---

## 🔄 Versionamento de API

### Versões Disponíveis

| Versão | Prefixo | Status | Recomendado |
|--------|---------|--------|-------------|
| **v1** | `/api/v1/*` | ✅ Estável | ✅ Sim |
| Legacy | `/api/*` | ⚠️ Retrocompatibilidade | ❌ Não (será descontinuado) |

### Migração v1

#### Antes (Legacy)

```http
GET /api/sobre
GET /api/projetos
POST /api/contato
```

#### Depois (v1 - Recomendado)

```http
GET /api/v1/sobre
GET /api/v1/projetos
POST /api/v1/contato
```

### Política de Versão

- **v1**: Mantida com retrocompatibilidade
- **Legacy**: Ainda funcional, mas será removida em versão futura
- **Breaking changes**: Sempre resultam em nova versão (v2, v3...)
- **Deprecation**: Mínimo 6 meses de aviso antes de remoção

---

## 🌐 Como Integrar com Frontend

### 1. Configurar CORS

O backend já está configurado para aceitar requisições de:
- `http://localhost:5173` (Vite dev server)
- `http://127.0.0.1:5173`

Para adicionar outras origens, edite `backend/.env`:

```env
ORIGENS_PERMITIDAS=http://localhost:5173,https://seudominio.com
```

### 2. Exemplo Fetch (JavaScript/TypeScript)

```typescript
// Configuração base
const API_BASE_URL = 'http://localhost:8000/api/v1';

// Função helper com error handling
async function fetchAPI<T>(endpoint: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    headers: {
      'Content-Type': 'application/json',
      ...options?.headers,
    },
    ...options,
  });

  if (!response.ok) {
    const erro = await response.json();
    throw new Error(erro.erro?.mensagem || 'Erro desconhecido');
  }

  return response.json();
}

// Obter projetos
const projetos = await fetchAPI<RespostaProjetos>('/projetos');

// Enviar contato
await fetchAPI('/contato', {
  method: 'POST',
  body: JSON.stringify({
    nome: 'João',
    email: 'joao@exemplo.com',
    assunto: 'Contato',
    mensagem: 'Olá!',
  }),
});
```

### 3. Exemplo Axios

```typescript
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para tratamento de erro global
api.interceptors.response.use(
  (response) => response,
  (error) => {
    const mensagem = error.response?.data?.erro?.mensagem || 'Erro desconhecido';
    console.error(`[${error.response?.data?.erro?.codigo}] ${mensagem}`);
    return Promise.reject(error);
  }
);

// Uso
const { data } = await api.get('/projetos');
```

### 4. Rastreamento com Request ID

O header `X-Request-ID` pode ser usado para correlacionar logs frontend↔backend:

```typescript
const response = await fetch('/api/v1/sobre');
const requestId = response.headers.get('X-Request-ID');
console.log(`Request ID: ${requestId}`);
```

### 5. Tipos TypeScript (Opcional)

Gere tipos automaticamente a partir do schema OpenAPI:

```bash
# Instalar ferramenta
npm install -D openapi-typescript

# Gerar tipos
npx openapi-typescript http://localhost:8000/openapi.json -o src/types/api.ts
```

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
structlog==24.1.0         # Logging estruturado
```

---

## 🎯 Decisões Técnicas

### 1. Clean Architecture Simplificada

**Por quê?**
- ✅ **Testabilidade**: Use cases testáveis sem dependências externas
- ✅ **Flexibilidade**: Trocar adaptadores (JSON → PostgreSQL) sem mudar lógica
- ✅ **Escalabilidade**: Fácil adicionar novos casos de uso sem quebrar código existente
- ✅ **Manutenibilidade**: Responsabilidades claras em cada camada

**Trade-offs**:
- ⚠️ Mais arquivos e abstrações
- ⚠️ Curva de aprendizado inicial maior
- ✅ Compensa em projetos de médio/longo prazo

### 2. API Versionada (/api/v1)

**Por quê?**
- ✅ **Retrocompatibilidade**: Manter clientes antigos funcionando
- ✅ **Migrations suaves**: Depreciar versões gradualmente
- ✅ **Contratos estáveis**: Frontend não quebra com mudanças backend
- ✅ **Profissionalismo**: Padrão de mercado para APIs públicas

**Implementação**:
- Router v1 agrupa todos os endpoints versionados
- Rotas `/api/*` legacy mantidas para transição
- Breaking changes = nova versão

### 3. Exception Handling Global

**Por quê?**
- ✅ **Consistência**: Todas as respostas de erro seguem mesmo padrão
- ✅ **Rastreabilidade**: Códigos de erro facilitam debugging
- ✅ **DX (Developer Experience)**: Frontend sabe exatamente o que esperar
- ✅ **Logging centralizado**: Todos os erros logados automaticamente

**Hierarquia**:
```
ErroDominio (400) → ErroValidacao (422)
                 → ErroRecursoNaoEncontrado (404)
ErroInfraestrutura (500)
```

### 4. Middleware com Request ID

**Por quê?**
- ✅ **Observabilidade**: Rastrear requisição em logs distribuídos
- ✅ **Debugging**: Correlacionar erro frontend↔backend
- ✅ **Performance**: Medir tempo de resposta de cada endpoint
- ✅ **Auditoria**: Saber quantas requisições, de onde, quanto tempo

**Headers adicionados**:
- `X-Request-ID`: UUID único
- `X-Response-Time`: Tempo em ms

### 5. Health Check Profissional

**Por quê?**
- ✅ **Kubernetes/Docker**: Probes de liveness/readiness
- ✅ **Load Balancers**: Verificar se instância está saudável
- ✅ **Monitoramento**: Alertas quando API cair
- ✅ **Informações úteis**: Versão, ambiente, uptime

**Retorna**:
- Status, mensagem, versão_api, ambiente, uptime_segundos

### 6. Pydantic V2 para Validação

**Por quê?**
- ✅ **Validação automática**: Menos código boilerplate
- ✅ **OpenAPI/Swagger**: Documentação gerada automaticamente
- ✅ **Type Safety**: Integração com mypy/pylance
- ✅ **Performance**: Core em Rust (até 50x mais rápido que V1)

**Vantagens**:
- Contratos HTTP explícitos
- Validação em runtime + tipo estático
- Exemplos na documentação

### 7. JSON Files vs Banco de Dados

**Por quê JSON (por enquanto)?**
- ✅ **Simplicidade**: Portfólio não precisa de queries complexas
- ✅ **Versionamento**: Dados no git = histórico completo
- ✅ **Deploy fácil**: Sem necessidade de provisionar banco
- ✅ **Demonstração**: Foco em arquitetura, não em ORM

**Migração futura**:
- Interface `RepositorioPortfolio` permite trocar implementação
- Migrar para PostgreSQL = só trocar adaptador
- Use cases não mudam

### 8. Logging Estruturado

**Por quê?**
- ✅ **Parsing struturados**: request_id, método, path, status, duração
- ✅ **Filtragem**: Buscar logs por request_id específico
- ✅ **Debugging produção**: Rastrear requisição problemática
- ✅ **JSON em produção**: Logs parseáveis por ferramentas
- ✅ **Console em dev**: Formato legível para humanos

**Implementação com structlog**:
- Processadores configuráveis (JSON/Console)
- Context vars para request_id
- Timestamps ISO 8601
- Stack traces formatados

**Formato**:
```json
{
  "event": "requisicao_recebida",
  "timestamp": "2026-02-10T10:30:00.000000Z",
  "level": "info",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "metodo": "GET",
  "path": "/api/v1/projetos"
}
2026-02-09 15:30:45 | INFO     | app.core.middleware | Resposta enviada | 550e8400-... | duracao_ms=45.23
```

### 9. Código 100% em Português

**Por quê?**
- ✅ **Contexto nacional**: Demonstra alinhamento com mercado brasileiro
- ✅ **Clareza**: Sem tradução mental ao ler código
- ✅ **Consistência**: Domínio e implementação na mesma língua
- ✅ **Acessibilidade**: Mais desenvolvedores podem entender

**Trade-offs**:
- ⚠️ Menos comum em open source internacional
- ✅ Perfeito para empresas brasileiras

### 10. Testes Automatizados

**Por quê?**
- ✅ **Confiança**: Refatorar sem medo de quebrar
- ✅ **Documentação viva**: Testes mostram como usar código
- ✅ **CI/CD**: Deploy automático só se testes passarem
- ✅ **Qualidade**: Cobertura > 70% garante casos principais

**Estratégia**:
- Testes de use cases (lógica de negócio)
- Testes de endpoints (integração)
- Fixtures reutilizáveis (conftest.py)

---

## 🔄 Próximos Passos (Roadmap)

### Curto Prazo

- [x] ~~Versionamento de API (v1)~~
- [x] ~~Error handling global~~
- [x] ~~Middleware com request_id~~
- [x] ~~Health check profissional~~
- [x] ~~Deploy em Railway/Render~~
- [x] ~~CI/CD com GitHub Actions~~
- [x] ~~Logs estruturados com structlog~~

### Médio Prazo

- [ ] Autenticação JWT (opcional para admin)
- [ ] Rate limiting (proteção contra abuso)
- [ ] Cache com Redis (projetos, stack)
- [ ] Migração para PostgreSQL
- [ ] Monitoramento com Sentry

### Longo Prazo

- [ ] GraphQL endpoint (além de REST)
- [ ] WebSockets para notificações real-time
- [ ] Internacionalização (PT/EN/ES)
- [ ] Admin dashboard
- [ ] Analytics de visitas

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