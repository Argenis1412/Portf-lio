# Guia de Deploy - Portfolio Backend

## 🚀 Deploy em Produção

Este guia mostra como fazer deploy do backend em diferentes plataformas.

---

## 📋 Pré-requisitos

- ✅ Conta na plataforma escolhida (Railway, Render, etc.)
- ✅ Repositório Git configurado
- ✅ Variáveis de ambiente definidas

---

## 🚂 Deploy no Railway

### 1. Instalação do Railway CLI (Opcional)

```bash
# Windows (PowerShell)
iwr https://railway.app/install.ps1 | iex

# Linux/Mac
curl -fsSL https://railway.app/install.sh | sh
```

### 2. Deploy via Dashboard (Recomendado)

1. Acesse [railway.app](https://railway.app)
2. Clique em **"New Project"** → **"Deploy from GitHub repo"**
3. Selecione o repositório `Portafolio`
4. Railway detectará automaticamente o `railway.toml`
5. Configure as variáveis de ambiente secretas:
   - `FORMSPREE_FORM_ID`: Seu ID do Formspree
   - `ORIGENS_PERMITIDAS`: Domínios permitidos (ex: `https://seudominio.com`)

### 3. Deploy via CLI

```bash
# Login
railway login

# Criar novo projeto
railway init

# Deploy
railway up

# Listar variáveis
railway variables

# Adicionar variáveis secretas
railway variables set FORMSPREE_FORM_ID=seu_form_id
railway variables set ORIGENS_PERMITIDAS=https://seudominio.com
```

### 4. Verificar Deploy

```bash
# Ver logs
railway logs

# Abrir no browser
railway open
```

**URL gerada**: `https://portfolio-backend-production.up.railway.app`

---

## 🎨 Deploy no Render

### 1. Deploy via Dashboard

1. Acesse [render.com](https://render.com)
2. Clique em **"New +"** → **"Blueprint"**
3. Conecte seu repositório GitHub
4. Render detectará automaticamente o `render.yaml`
5. Revise as configurações e clique em **"Apply"**
6. Configure as variáveis secretas no dashboard:
   - `FORMSPREE_FORM_ID`

### 2. Deploy Manual (Web Service)

1. **New +** → **Web Service**
2. Conecte repositório
3. Configurações:
   - **Name**: `portfolio-backend`
   - **Environment**: `Docker`
   - **Region**: Oregon (ou mais próximo)
   - **Branch**: `main`
   - **Dockerfile Path**: `backend/Dockerfile`
   - **Docker Context**: `backend`
4. **Advanced**:
   - **Health Check Path**: `/saude`
   - **Auto-Deploy**: Yes
5. **Environment Variables**:
   ```
   AMBIENTE=producao
   VERSAO_API=1.0.0
   PORT=10000
   FORMSPREE_FORM_ID=seu_form_id
   ORIGENS_PERMITIDAS=https://seudominio.com
   ```

### 3. Verificar Deploy

**URL gerada**: `https://portfolio-backend.onrender.com`

Teste:
```bash
curl https://portfolio-backend.onrender.com/saude
```

---

## 🐳 Deploy com Docker (Genérico)

### 1. Build da Imagem

```bash
cd backend
docker build -t portfolio-backend:latest .
```

### 2. Testar Localmente

```bash
docker run -p 8000:8000 \
  -e AMBIENTE=producao \
  -e FORMSPREE_FORM_ID=seu_form_id \
  portfolio-backend:latest
```

### 3. Push para Registry

```bash
# Docker Hub
docker tag portfolio-backend:latest seu-usuario/portfolio-backend:latest
docker push seu-usuario/portfolio-backend:latest

# GitHub Container Registry
docker tag portfolio-backend:latest ghcr.io/argenis972/portfolio-backend:latest
docker push ghcr.io/argenis972/portfolio-backend:latest
```

---

## 🔐 Variáveis de Ambiente Necessárias

| Variável | Obrigatória | Padrão | Descrição |
|----------|-------------|--------|-----------|
| `AMBIENTE` | ❌ | `desenvolvimento` | `producao` ou `desenvolvimento` |
| `VERSAO_API` | ❌ | `1.0.0` | Versão da API |
| `FORMSPREE_FORM_ID` | ✅ | - | ID do formulário Formspree |
| `ORIGENS_PERMITIDAS` | ⚠️ | `*` | Origens CORS (separadas por vírgula) |
| `PORT` | ❌ | `8000` | Porta do servidor |

### Obter FORMSPREE_FORM_ID

1. Acesse [formspree.io](https://formspree.io)
2. Crie novo formulário
3. Copie o ID (ex: `xpznbqgk`)

---

## 📊 Monitoramento

### Health Check

```bash
curl https://sua-url.com/saude
```

**Resposta esperada**:
```json
{
  "status": "ok",
  "mensagem": "API funcionando normalmente",
  "versao_api": "1.0.0",
  "ambiente": "producao",
  "uptime_segundos": 3600
}
```

### Logs Estruturados

Logs em formato JSON/Console com structlog:

```json
{
  "event": "requisicao_recebida",
  "timestamp": "2026-02-10T10:30:00.000000Z",
  "level": "info",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "metodo": "GET",
  "path": "/api/v1/projetos"
}
```

### Rastreamento

Todas as respostas incluem headers:
- `X-Request-ID`: UUID único
- `X-Response-Time`: Tempo em ms

---

## 🔄 CI/CD Automático

### GitHub Actions

Já configurado em `.github/workflows/backend-ci.yml`:

- ✅ Roda testes em push para `main`
- ✅ Verifica cobertura
- ✅ Build da imagem Docker
- ✅ Deploy automático (configurar secrets)

**Secrets necessários no GitHub**:
- `RAILWAY_TOKEN` (para Railway)
- `RENDER_API_KEY` (para Render)

---

## 🐛 Troubleshooting

### Erro: "Application failed to respond"

**Causa**: API não está rodando na porta correta

**Solução**:
```python
# Em backend/app/principal.py (já configurado)
import os
port = int(os.getenv("PORT", 8000))
```

### Erro: CORS bloqueando requisições

**Causa**: Frontend não está nas origens permitidas

**Solução**:
```bash
# Adicionar origem do frontend
railway variables set ORIGENS_PERMITIDAS=https://meu-frontend.vercel.app

# Ou permitir todas (NÃO recomendado em produção)
railway variables set ORIGENS_PERMITIDAS=*
```

### Erro: "Health check failed"

**Causa**: Endpoint `/saude` não está respondendo

**Verificar**:
```bash
# Ver logs
railway logs

# Testar localmente
curl http://localhost:8000/saude
```

---

## 📚 Referências

- [Railway Docs](https://docs.railway.app/)
- [Render Docs](https://render.com/docs)
- [Docker Docs](https://docs.docker.com/)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)

---

## ✅ Checklist de Deploy

- [ ] Código commitado no GitHub
- [ ] Testes passando
- [ ] Dockerfile funcional
- [ ] Variáveis de ambiente configuradas
- [ ] CORS configurado corretamente
- [ ] Health check respondendo
- [ ] Logs estruturados configurados
- [ ] Monitoramento ativo
- [ ] Domínio customizado (opcional)

---

**Autor**: Argenis Lopez  
**Email**: argenislopez28708256@gmail.com  
**GitHub**: [@argenis972](https://github.com/argenis972)
