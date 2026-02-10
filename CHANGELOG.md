# 📊 CHANGELOG

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

---

## [1.0.0] - 2025-01-XX

### 🎉 Versão Inicial

#### ✅ Adicionado

**Backend:**
- ✅ API REST completa com FastAPI
- ✅ Clean Architecture (Controllers → Use Cases → Entities → Adapters)
- ✅ Versionamento de API (`/api/v1/`)
- ✅ Sistema de exceções customizadas
- ✅ Handlers globais de erro padronizados
- ✅ Middleware de observabilidade (Request ID, logging, performance)
- ✅ Health check com métricas (versão, ambiente, uptime)
- ✅ Documentação OpenAPI/Swagger interativa
- ✅ Sistema de contato com envio de email
- ✅ 6 endpoints funcionais (sobre, projetos, stack, experiências, contato, saúde)
- ✅ Validação robusta com Pydantic V2
- ✅ Cobertura de testes de 93%+
- ✅ 17 testes automatizados (pytest + asyncio)
- ✅ Persistência em JSON (pronto para migrar para DB)

**Documentação:**
- ✅ README raiz profissional completo
- ✅ README backend detalhado
- ✅ Guia de arquitetura (ADR)
- ✅ Guia de deploy
- ✅ Guia de testes
- ✅ API reference completa
- ✅ CONTRIBUTING.md
- ✅ Changelog de produção

**DevOps:**
- ✅ Dockerfile multi-stage para backend
- ✅ Docker Compose estruturado (pronto para uso)
- ✅ GitHub Actions CI para backend
- ✅ GitHub Actions CI para frontend
- ✅ .gitignore profissional
- ✅ .env.example com variáveis documentadas

**Frontend (em desenvolvimento):**
- ⏳ Estrutura básica com Vite + React + TypeScript
- ⏳ TailwindCSS configurado
- ⏳ Componentes em desenvolvimento

---

## [0.1.0] - 2025-01-XX (Pré-lançamento)

### Adicionado
- Estrutura inicial do projeto
- API básica sem versionamento
- Persistência em JSON

---

## 🔮 Próximas Versões

### [1.1.0] - Planejado

**Backend:**
- [ ] Migração para PostgreSQL
- [ ] Sistema de cache com Redis
- [ ] Rate limiting
- [ ] Autenticação JWT (se necessário)
- [ ] Upload de imagens para S3/Cloudinary

**Frontend:**
- [ ] Landing page completa
- [ ] Seção de projetos interativa
- [ ] Formulário de contato
- [ ] Tema dark/light
- [ ] Animações com Framer Motion

**DevOps:**
- [ ] Deploy automatizado (CI/CD completo)
- [ ] Monitoramento com Sentry
- [ ] Logs centralizados
- [ ] Testes E2E com Playwright

---

## Convenções de Versionamento

- **MAJOR** (1.x.x): Mudanças incompatíveis na API
- **MINOR** (x.1.x): Novas funcionalidades compatíveis
- **PATCH** (x.x.1): Correções de bugs

---

## Tipos de Mudanças

- `✅ Adicionado` - Novas funcionalidades
- `🔄 Modificado` - Mudanças em features existentes
- `⚠️ Deprecated` - Features que serão removidas
- `🗑️ Removido` - Features removidas
- `🐛 Corrigido` - Correções de bugs
- `🔒 Segurança` - Correções de vulnerabilidades

---

[1.0.0]: https://github.com/seu-usuario/portafolio/releases/tag/v1.0.0
[0.1.0]: https://github.com/seu-usuario/portafolio/releases/tag/v0.1.0
