# Deployment Guide - Portfolio Backend

## 🚀 Production Deployment

This guide shows how to deploy the backend on different platforms.

---

## 📋 Prerequisites

- ✅ Account on the chosen platform (Railway, Render, etc.)
- ✅ Configured Git repository
- ✅ Defined environment variables

---

## 🚂 Deploy on Railway

### 1. Railway CLI Installation (Optional)

```bash
# Windows (PowerShell)
iwr https://railway.app/install.ps1 | iex

# Linux/Mac
curl -fsSL https://railway.app/install.sh | sh
```

### 2. Deploy via Dashboard (Recommended)

1. Access [railway.app](https://railway.app)
2. Click on **"New Project"** → **"Deploy from GitHub repo"**
3. Select the `Portf-lio` repository
4. Railway will automatically detect the `railway.toml`
5. Configure secret environment variables:
   - `FORMSPREE_FORM_ID`: Your Formspree ID
   - `ALLOWED_ORIGINS`: Allowed domains (e.g., `https://yourdomain.com`)

### 3. Deploy via CLI

```bash
# Login
railway login

# Initialize new project
railway init

# Deploy
railway up

# List variables
railway variables

# Add secret variables
railway variables set FORMSPREE_FORM_ID=your_form_id
railway variables set ALLOWED_ORIGINS=https://yourdomain.com
```

### 4. Verify Deployment

```bash
# View logs
railway logs

# Open in browser
railway open
```

**Generated URL**: `https://portfolio-backend-production.up.railway.app`

---

## 🎨 Deploy on Render

### 1. Deploy via Dashboard

1. Access [render.com](https://render.com)
2. Click on **"New +"** → **"Blueprint"**
3. Connect your GitHub repository
4. Render will automatically detect the `render.yaml`
5. Review the settings and click **"Apply"**
6. Configure secret variables in the dashboard:
   - `FORMSPREE_FORM_ID`

### 2. Manual Deployment (Web Service)

1. **New +** → **Web Service**
2. Connect repository
3. Settings:
   - **Name**: `portfolio-backend`
   - **Environment**: `Docker`
   - **Region**: Oregon (or nearest)
   - **Branch**: `main`
   - **Dockerfile Path**: `backend/Dockerfile`
   - **Docker Context**: `backend`
4. **Advanced**:
   - **Health Check Path**: `/saude`
   - **Auto-Deploy**: Yes
5. **Environment Variables**:
   ```
   ENVIRONMENT=production
   API_VERSION=1.0.0
   PORT=10000
   FORMSPREE_FORM_ID=your_form_id
   ALLOWED_ORIGINS=https://yourdomain.com
   ```

### 3. Verify Deployment

**Generated URL**: `https://portfolio-backend.onrender.com`

Test:
```bash
curl https://portfolio-backend.onrender.com/saude
```

---

## 🐳 Deploy with Docker (Generic)

### 1. Image Build

```bash
cd backend
docker build -t portfolio-backend:latest .
```

### 2. Test Locally

```bash
docker run -p 8000:8000 \
  -e ENVIRONMENT=production \
  -e FORMSPREE_FORM_ID=your_form_id \
  portfolio-backend:latest
```

### 3. Push to Registry

```bash
# Docker Hub
docker tag portfolio-backend:latest your-user/portfolio-backend:latest
docker push your-user/portfolio-backend:latest

# GitHub Container Registry
docker tag portfolio-backend:latest ghcr.io/Argenis1412/portfolio-backend:latest
docker push ghcr.io/Argenis1412/portfolio-backend:latest
```

---

## 🔐 Required Environment Variables

| Variable | Required | Default | Description |
|----------|-------------|--------|-----------|
| `ENVIRONMENT` | ❌ | `development` | `production` or `development` |
| `API_VERSION` | ❌ | `1.0.0` | API version |
| `FORMSPREE_FORM_ID` | ✅ | - | Formspree form ID |
| `ALLOWED_ORIGINS` | ⚠️ | `*` | CORS origins (comma-separated) |
| `PORT` | ❌ | `8000` | Server port |

### Obtain FORMSPREE_FORM_ID

1. Access [formspree.io](https://formspree.io)
2. Create new form
3. Copy the ID (e.g., `xpznbqgk`)

---

## 📊 Monitoring

### Health Check

```bash
curl https://your-url.com/saude
```

**Expected response**:
```json
{
  "status": "ok",
  "message": "API working normally",
  "api_version": "1.0.0",
  "environment": "production",
  "uptime_seconds": 3600
}
```

### Structured Logs

Logs in JSON/Console format with structlog:

```json
{
  "event": "request_received",
  "timestamp": "2026-02-10T10:30:00.000000Z",
  "level": "info",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "method": "GET",
  "path": "/api/v1/projects"
}
```

### Tracing

All responses include headers:
- `X-Request-ID`: Unique UUID
- `X-Response-Time`: Time in ms

---

## 🔄 Automatic CI/CD

### GitHub Actions

Already configured in `.github/workflows/backend-ci.yml`:

- ✅ Runs tests on push to `main`
- ✅ Verifies coverage
- ✅ Docker image build
- ✅ Automated deploy (configure secrets)

**Required Secrets on GitHub**:
- `RAILWAY_TOKEN` (for Railway)
- `RENDER_API_KEY` (for Render)

---

## 🐛 Troubleshooting

### Error: "Application failed to respond"

**Cause**: API is not running on the correct port

**Solution**:
```python
# In backend/app/principal.py (already configured)
import os
port = int(os.getenv("PORT", 8000))
```

### Error: CORS blocking requests

**Cause**: Frontend is not in the allowed origins

**Solution**:
```bash
# Add frontend origin
railway variables set ALLOWED_ORIGINS=https://my-frontend.vercel.app

# Or allow all (NOT recommended in production)
railway variables set ALLOWED_ORIGINS=*
```

### Error: "Health check failed"

**Cause**: Endpoint `/saude` is not responding

**Check**:
```bash
# View logs
railway logs

# Test locally
curl http://localhost:8000/saude
```

---

## 📚 References

- [Railway Docs](https://docs.railway.app/)
- [Render Docs](https://render.com/docs)
- [Docker Docs](https://docs.docker.com/)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)

---

## ✅ Deployment Checklist

- [ ] Code committed to GitHub
- [ ] Tests passing
- [ ] Functional Dockerfile
- [ ] Environment variables configured
- [ ] CORS correctly configured
- [ ] Health check responding
- [ ] Structured logs configured
- [ ] Active monitoring
- [ ] Custom domain (optional)

---

**Author**: Argenis Lopez  
**Email**: argenislopez28708256@gmail.com  
**GitHub**: [@Argenis1412](https://github.com/Argenis1412)
