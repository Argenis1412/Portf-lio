# 🚀 Portfólio Profissional

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](.)
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Sistema completo de portfólio profissional com backend FastAPI e frontend moderno (em desenvolvimento)**

Este repositório contém um sistema de portfólio full-stack construído com as melhores práticas de arquitetura limpa, separação de responsabilidades e preparado para produção.

---
// este es un comentario
// kalsjas
## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Arquitetura](#-arquitetura)
- [Tecnologias](#-tecnologias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Início Rápido](#-início-rápido)
- [Documentação](#-documentação)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

---

## 🎯 Visão Geral

Sistema de portfólio profissional desenvolvido para demonstrar habilidades em:

- **Backend**: API REST com FastAPI, Clean Architecture, validação robusta
- **Qualidade**: Testes automatizados (93%+ cobertura), linting, padronização
- **Produção**: Logging estruturado, monitoramento, tratamento de erros
- **Documentação**: OpenAPI/Swagger interativo, README detalhado
- **DevOps**: Containerização (em desenvolvimento), CI/CD ready

### 🌟 Funcionalidades

✅ **API REST completa** com versionamento (`/api/v1/`)  
✅ **Gestão de experiências profissionais**  
✅ **Showcase de projetos** com detalhes técnicos  
✅ **Sistema de contato** com envio de e-mail  
✅ **Health check** com métricas de uptime  
✅ **Tratamento de erros padronizado** com códigos customizados  
✅ **Middleware de observabilidade** (Request ID, logging estruturado, performance)  
✅ **Logs estruturados** com structlog (JSON em produção, Console em dev)  
✅ **CI/CD com GitHub Actions** (tests, lint, deploy)  
✅ **Configuração para deploy** em Railway/Render  
⏳ **Frontend em React + TypeScript** (em desenvolvimento)  

---

## 🏗️ Arquitetura

O projeto segue princípios de **Clean Architecture** com separação clara de camadas:

```
┌─────────────────────────────────────────────┐
│           Camada de Interface               │
│         (Controllers/Routers)               │
│   → Recebe requisições HTTP                 │
│   → Valida entrada com Pydantic             │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│         Camada de Casos de Uso              │
│      (Business Logic/Use Cases)             │
│   → Orquestra lógica de negócio             │
│   → Independente de frameworks              │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│          Camada de Entidades                │
│         (Domain Models)                     │
│   → Regras de negócio puras                 │
│   → Validações de domínio                   │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│       Camada de Adaptadores                 │
│    (Repositories/Services)                  │
│   → Acesso a dados (JSON, DB)               │
│   → Integrações externas (Email)            │
└─────────────────────────────────────────────┘
```

### Benefícios

- 🔄 **Testabilidade**: Cada camada pode ser testada isoladamente
- 🔌 **Desacoplamento**: Fácil substituição de implementações
- 📦 **Manutenibilidade**: Código organizado e localizado
- 🎯 **Escalabilidade**: Estrutura pronta para crescimento

---

## 🛠️ Tecnologias

### Backend

| Tecnologia | Versão | Propósito |
|-----------|--------|-----------|
| **Python** | 3.12+ | Linguagem principal |
| **FastAPI** | 0.115+ | Framework web assíncrono |
| **Pydantic** | 2.10+ | Validação de dados |
| **Uvicorn** | 0.34+ | Servidor ASGI |
| **pytest** | 8.3+ | Framework de testes |
| **pytest-cov** | 6.0+ | Cobertura de código |

### Frontend *(em desenvolvimento)*

| Tecnologia | Versão | Propósito |
|-----------|--------|-----------|
| **React** | 18+ | Biblioteca UI |
| **TypeScript** | 5+ | Tipagem estática |
| **Vite** | 7+ | Build tool |
| **TailwindCSS** | 3+ | Estilização |

### DevOps *(planejado)*

- **Docker** / **Docker Compose** - Containerização
- **GitHub Actions** - CI/CD
- **Nginx** - Reverse proxy

---

## 📁 Estrutura do Projeto

```
portafolio/
│
├── backend/                    # API FastAPI
│   ├── app/
│   │   ├── core/              # Núcleo (exceções, middleware)
│   │   ├── controladores/     # Endpoints HTTP
│   │   ├── casos_uso/         # Lógica de negócio
│   │   ├── entidades/         # Modelos de domínio
│   │   ├── esquemas/          # Schemas Pydantic
│   │   └── adaptadores/       # Repositórios, serviços
│   ├── dados/                 # Persistência JSON
│   ├── testes/                # Testes automatizados
│   ├── requirements.txt       # Dependências Python
│   └── README.md              # Documentação detalhada
│
├── frontend/                  # Aplicação React (em dev)
│   ├── src/
│   │   ├── componentes/       # Componentes React
│   │   ├── servicos/          # Cliente API
│   │   └── tipos/             # TypeScript types
│   ├── package.json
│   └── README.md
│
├── docs/                      # Documentação adicional
│   ├── arquitetura.md         # Decisões arquiteturais
│   ├── api.md                 # Guia de API
│   └── deployment.md          # Guia de deploy
│
├── .github/                   # GitHub workflows
│   └── workflows/
│       ├── backend-ci.yml     # CI para backend
│       └── frontend-ci.yml    # CI para frontend
│
├── .gitignore                 # Arquivos ignorados
├── .env.example               # Exemplo de variáveis
├── LICENSE                    # Licença MIT
├── docker-compose.yml         # Orquestração (planejado)
└── README.md                  # Este arquivo
```

---

## 🚀 Início Rápido

### Pré-requisitos

- **Python 3.12+** instalado
- **Node.js 20+** (para frontend)
- **Git** configurado

### 1️⃣ Clone o Repositório

```bash
git clone https://github.com/argenis972/Portf-lio.git
cd portafolio
```

### 2️⃣ Configure o Backend

```bash
cd backend

# Crie um ambiente virtual
python -m venv .venv

# Ative o ambiente (Windows)
.venv\Scripts\activate

# Ative o ambiente (Linux/Mac)
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute os testes
pytest

# Inicie o servidor
uvicorn app.principal:app --reload
```

🌐 API disponível em: **http://localhost:8000**  
📚 Documentação: **http://localhost:8000/docs**

### 3️⃣ Configure o Frontend *(em desenvolvimento)*

```bash
cd frontend

# Instale as dependências
npm install

# Inicie o servidor de desenvolvimento
npm run dev
```

🌐 Aplicação: **http://localhost:5173**

---

## 📖 Documentação

### Backend

- **[README detalhado](backend/README.md)**: Arquitetura, endpoints, exemplos
- **[Swagger UI](http://localhost:8000/docs)**: Documentação interativa (quando servidor rodando)
- **[ReDoc](http://localhost:8000/redoc)**: Documentação alternativa

### Recursos Adicionais

- 📄 [Changelog de Produção](backend/CHANGELOG_PRODUCAO.md)
- 🧪 [Guia de Testes](docs/testes.md) *(em breve)*
- 🚀 [Guia de Deploy](docs/deployment.md) *(em breve)*

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Este é um projeto pessoal de portfólio, mas sinta-se à vontade para:

1. **Reportar bugs** via Issues
2. **Sugerir melhorias** via Issues
3. **Enviar PRs** com correções/features

### Diretrizes

- Siga os padrões de código existentes
- Adicione testes para novas funcionalidades
- Atualize a documentação quando necessário
- Commits em inglês ou português

---

##  Deploy em Produção

### Backend

O backend está pronto para deploy em múltiplas plataformas:

#### Railway (Recomendado)
```bash
# Via Dashboard
1. Acesse railway.app
2. New Project → Deploy from GitHub
3. Selecione o repositório
4. Configure variáveis de ambiente
```

#### Render
```bash
# Via Blueprint
1. Acesse render.com
2. New → Blueprint
3. Conecte o repositório
4. render.yaml será detectado automaticamente
```

**Documentação completa**: [backend/DEPLOY.md](backend/DEPLOY.md)

### Frontend (Em Desenvolvimento)

Plataformas suportadas:
- Vercel (Recomendado para React/Next.js)
- Netlify
- Cloudflare Pages

### CI/CD Automático

✅ **GitHub Actions** configurado:
- Tests automáticos em push
- Build da imagem Docker
- Deploy automático (configurar secrets)

**Workflows**:
- [`.github/workflows/backend-ci.yml`](.github/workflows/backend-ci.yml)
- [`.github/workflows/frontend-ci.yml`](.github/workflows/frontend-ci.yml)

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para detalhes.

```
MIT License

Copyright (c) 2025 Argenis Mauricio Lopez Salazar

Permission is hereby granted, free of charge, to any person obtaining a copy...
```

---

## 👨‍💻 Autor

**Argenis Lopez**

- 🌐 Website: (em breve)
- 💼 LinkedIn: [LinkedIn](https://www.linkedin.com/in/argenis972/)
- 📧 Email: [Email](mailto:argenislopez28708256@gmail.com)
- 🐙 GitHub: [argenis972](https://github.com/argenis972)

---

## 🙏 Agradecimentos

- FastAPI pela excelente documentação
- Comunidade Python pelo suporte
- Você por visualizar este projeto!

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela!**

[![GitHub stars](https://img.shields.io/github/stars/argenis972/Portf-lio?style=social)](https://github.com/argenis972/Portf-lio/stargazers)

</div>
