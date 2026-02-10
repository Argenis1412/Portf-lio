# 🗂️ Estrutura do Repositório

> **Visão completa da organização profissional do portfólio**

---

## 📊 Estrutura Visual

```
portafolio/ (RAIZ)
│
├── 📄 README.md ⭐                    # Documentação principal do projeto
├── 📄 LICENSE                         # Licença MIT
├── 📄 CHANGELOG.md                    # Histórico de versões
├── 📄 CONTRIBUTING.md                 # Guia de contribuição
├── 📄 .gitignore                      # Arquivos ignorados pelo Git
├── 📄 .env.example                    # Exemplo de variáveis de ambiente
├── 📄 docker-compose.yml              # Orquestração de containers
│
├── 📁 .github/                        # Configurações do GitHub
│   └── 📁 workflows/
│       ├── backend-ci.yml             # CI/CD do backend
│       └── frontend-ci.yml            # CI/CD do frontend
│
├── 📁 docs/ ⭐                        # Documentação adicional
│   ├── arquitetura.md                 # Decisões arquiteturais (ADR)
│   ├── api.md                         # Referência completa da API
│   ├── testes.md                      # Guia de testes
│   └── deployment.md                  # Guia de deploy
│
├── 📁 backend/ 🚀                     # API FastAPI
│   ├── 📄 README.md ⭐                # Documentação técnica do backend
│   ├── 📄 CHANGELOG_PRODUCAO.md       # Mudanças de produção
│   ├── 📄 requirements.txt            # Dependências Python
│   ├── 📄 pytest.ini                  # Configuração de testes
│   ├── 📄 Dockerfile                  # Imagem Docker do backend
│   ├── 📄 .dockerignore               # Arquivos excluídos do Docker
│   │
│   ├── 📁 app/                        # Código-fonte principal
│   │   ├── principal.py               # Aplicação FastAPI
│   │   ├── configuracao.py            # Configurações
│   │   │
│   │   ├── 📁 core/                   # Núcleo da aplicação
│   │   │   ├── __init__.py
│   │   │   ├── excecoes.py            # Exceções customizadas
│   │   │   ├── handlers.py            # Handlers de erro
│   │   │   └── middleware.py          # Middleware (logging, request_id)
│   │   │
│   │   ├── 📁 controladores/          # Camada HTTP (Controllers)
│   │   │   ├── __init__.py
│   │   │   ├── v1.py                  # Router API v1
│   │   │   ├── api.py                 # Endpoints principais
│   │   │   ├── contato.py             # Endpoint de contato
│   │   │   └── saude.py               # Health check
│   │   │
│   │   ├── 📁 casos_uso/              # Lógica de Negócio (Use Cases)
│   │   │   ├── __init__.py
│   │   │   ├── enviar_contato.py
│   │   │   ├── obter_experiencias.py
│   │   │   ├── obter_projetos.py
│   │   │   ├── obter_sobre.py
│   │   │   └── obter_stack.py
│   │   │
│   │   ├── 📁 entidades/              # Modelos de Domínio (Entities)
│   │   │   ├── __init__.py
│   │   │   ├── experiencia.py
│   │   │   ├── mensagem.py
│   │   │   └── projeto.py
│   │   │
│   │   ├── 📁 esquemas/               # Schemas Pydantic
│   │   │   ├── __init__.py
│   │   │   ├── contato.py
│   │   │   ├── experiencias.py
│   │   │   ├── projetos.py
│   │   │   ├── saude.py
│   │   │   ├── sobre.py
│   │   │   └── stack.py
│   │   │
│   │   └── 📁 adaptadores/            # Camada de Infraestrutura
│   │       ├── __init__.py
│   │       ├── repositorio.py         # Persistência JSON
│   │       ├── email_adaptador.py     # Envio de emails
│   │       └── logger_adaptador.py    # Sistema de logs
│   │
│   ├── 📁 dados/                      # Persistência JSON
│   │   ├── sobre.json
│   │   ├── projetos.json
│   │   ├── experiencias.json
│   │   └── stack.json
│   │
│   ├── 📁 testes/ ✅                  # Testes automatizados
│   │   ├── __init__.py
│   │   ├── conftest.py                # Fixtures compartilhadas
│   │   ├── test_casos_uso.py          # Testes de lógica
│   │   └── test_controladores.py      # Testes HTTP
│   │
│   └── 📁 htmlcov/                    # Relatório de cobertura (gerado)
│
└── 📁 frontend/ ⚛️ (em desenvolvimento)
    ├── 📄 README.md
    ├── 📄 package.json                # Dependências Node
    ├── 📄 vite.config.ts              # Configuração Vite
    ├── 📄 tsconfig.json               # Configuração TypeScript
    ├── 📄 tailwind.config.ts          # Configuração Tailwind
    ├── 📄 eslint.config.js            # Configuração ESLint
    ├── 📄 postcss.config.js           # Configuração PostCSS
    ├── 📄 index.html                  # HTML raiz
    │
    ├── 📁 public/
    │   ├── manifest.json
    │   └── robots.txt
    │
    └── 📁 src/
        ├── main.tsx                   # Entry point
        ├── App.tsx                    # Componente raiz
        ├── index.css                  # Estilos globais
        ├── 📁 componentes/
        ├── 📁 contextos/
        ├── 📁 servicos/
        ├── 📁 tipos/
        ├── 📁 utils/
        └── 📁 assets/
```

---

## 🎯 Propósito de Cada Arquivo Raiz

| Arquivo | Propósito | Impacto para Recrutadores |
|---------|-----------|---------------------------|
| **README.md** | Primeira impressão do projeto | ⭐⭐⭐⭐⭐ CRÍTICO |
| **LICENSE** | Define uso legal do código | ⭐⭐⭐ Mostra profissionalismo |
| **CONTRIBUTING.md** | Guia para colaboradores | ⭐⭐ Projetos colaborativos |
| **CHANGELOG.md** | Histórico de versões | ⭐⭐⭐ Demonstra organização |
| **.gitignore** | Evita commit de lixo | ⭐⭐⭐⭐ Essencial |
| **.env.example** | Template de configuração | ⭐⭐⭐⭐ Facilita setup |
| **docker-compose.yml** | Orquestração de containers | ⭐⭐⭐⭐ DevOps skills |

---

## 📁 Propósito de Cada Diretório

### `/backend` - API FastAPI

**Camadas da Clean Architecture:**

```
┌─────────────────────────────────────────┐
│  Controladores (HTTP)                   │  ← Recebe requests
│  app/controladores/                     │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│  Casos de Uso (Business Logic)          │  ← Lógica de negócio
│  app/casos_uso/                         │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│  Entidades (Domain Models)               │  ← Regras de domínio
│  app/entidades/                          │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│  Adaptadores (Infrastructure)            │  ← Acesso a dados
│  app/adaptadores/                        │
└─────────────────────────────────────────┘
```

### `/frontend` - React App

**Estrutura moderna:**

- **componentes/**: Componentes React reutilizáveis
- **servicos/**: Cliente HTTP para consumir API
- **contextos/**: State management com Context API
- **tipos/**: TypeScript interfaces/types
- **utils/**: Funções auxiliares

### `/docs` - Documentação

**Documentação técnica profunda:**

- `arquitetura.md`: Decisões técnicas (ADR)
- `api.md`: Referência completa de endpoints
- `testes.md`: Como escrever e executar testes
- `deployment.md`: Guia de deploy passo a passo

### `/.github` - Automação

**CI/CD com GitHub Actions:**

- Testes automáticos em cada PR
- Build validation
- Coverage reports
- Pronto para deploy automático

---

## 📊 Estatísticas do Projeto

| Categoria | Quantidade | Status |
|-----------|-----------|--------|
| **Endpoints de API** | 6 | ✅ Funcionando |
| **Testes Automatizados** | 17 | ✅ 100% passing |
| **Cobertura de Código** | 93.05% | ✅ Acima de 70% |
| **Documentação (páginas)** | 7 | ✅ Completa |
| **Camadas de Arquitetura** | 4 | ✅ Clean Architecture |
| **Workflows CI/CD** | 2 | ✅ Configurados |
| **Dockerfiles** | 1 | ✅ Multi-stage |

---

## 🎨 Destaques para Recrutadores

### 🏗️ Clean Architecture
```
Separação clara de responsabilidades
Código testável e manutenível
Mudança de tecnologias sem quebrar lógica
```

### ✅ Testes Automatizados
```
93% de cobertura
17 testes (casos de uso + endpoints)
CI/CD automático no GitHub Actions
```

### 📚 Documentação Profissional
```
README detalhado com badges
ADR (Architecture Decision Records)
API reference completa
Guias de deploy e testes
```

### 🐳 DevOps Ready
```
Dockerfile otimizado (multi-stage)
Docker Compose configurado
GitHub Actions (CI/CD)
Health checks implementados
```

### 🔒 Boas Práticas
```
Tratamento de erros padronizado
Validação robusta (Pydantic V2)
Logging estruturado
Middleware de observabilidade
Versionamento de API
```

---

## 🚀 Próximos Passos

### Backend (Completo ✅)
- [x] API REST com FastAPI
- [x] Clean Architecture
- [x] Testes automatizados
- [x] Documentação completa
- [x] CI/CD configurado

### Frontend (Em Desenvolvimento 🚧)
- [ ] UI completa
- [ ] Consumo da API
- [ ] Testes de componentes
- [ ] Deploy no Vercel

### DevOps (Estruturado ✅)
- [x] Docker configurado
- [x] CI/CD no GitHub Actions
- [ ] Deploy automático
- [ ] Monitoramento (Sentry)

---

## 📝 Checklist de Organização

✅ **Raiz do Repositório:**
- [x] README.md profissional com badges
- [x] LICENSE (MIT)
- [x] .gitignore completo
- [x] .env.example documentado
- [x] CONTRIBUTING.md
- [x] CHANGELOG.md
- [x] docker-compose.yml

✅ **Documentação:**
- [x] docs/arquitetura.md (ADR)
- [x] docs/api.md
- [x] docs/testes.md
- [x] docs/deployment.md

✅ **Backend:**
- [x] README.md detalhado
- [x] Dockerfile otimizado
- [x] .dockerignore
- [x] pytest.ini
- [x] 93%+ cobertura de testes

✅ **CI/CD:**
- [x] .github/workflows/backend-ci.yml
- [x] .github/workflows/frontend-ci.yml

---

## 🎓 O que Recrutadores Vão Ver

1. **README raiz**: Projeto bem estruturado, profissional
2. **Badges**: Builds passando, cobertura alta
3. **Documentação**: Desenvolvedor que se importa com manutenibilidade
4. **Testes**: 93% de cobertura, 17 testes passando
5. **Clean Architecture**: Conhecimento de design patterns
6. **CI/CD**: Experiência com DevOps
7. **Docker**: Containerização profissional
8. **API versionada**: Pensamento em evolução

---

✅ **Repositório 100% profissional e pronto para impressionar!**
