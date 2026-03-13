# 🚀 Deployment Guide

> **Full manual for deploying the portfolio to production**

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Backend Deployment](#backend-deployment)
3. [Frontend Deployment](#frontend-deployment)
4. [Monitoring](#monitoring)

---

## Prerequisites

### Required Accounts

- [ ] **GitHub** - Versioning
- [ ] **Render/Railway** - Backend hosting (free)
- [ ] **Vercel/Netlify** - Frontend hosting (free)
- [ ] **Gmail App Password** - Email sending

### Tools

```bash
# Git
git --version  # >= 2.0

# Python
python --version  # >= 3.12

# Node.js
node --version  # >= 20
```

---

## Backend Deployment

### Option 1: Render.com (Recommended)

1. **Create an account at [render.com](https://render.com)**

2. **New → Web Service**

3. **Settings:**
   ```
   Name: portfolio-api
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn app.principal:app --host 0.0.0.0 --port $PORT
   ```

4. **Environment Variables:**
   ```env
   ENVIRONMENT=production
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   EMAIL_SENDER=your@email.com
   EMAIL_PASSWORD=gmail_app_password
   EMAIL_DESTINATION=your@email.com
   CORS_ORIGINS=https://your-frontend.vercel.app
   ```

5. **Create `backend/Dockerfile`:**
   ```dockerfile
   FROM python:3.12-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   COPY . .
   CMD ["uvicorn", "app.principal:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

### Option 2: Railway

Similar to Render, but with free PostgreSQL included.

---

## Frontend Deployment

### Option 1: Vercel (Recommended)

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy:**
   ```bash
   cd frontend
   vercel --prod
   ```

3. **Configure environment variable:**
   ```
   VITE_API_URL=https://your-backend.onrender.com/api/v1
   ```

### Option 2: Netlify

```bash
cd frontend
npm run build
npx netlify-cli deploy --prod --dir=dist
```

---

## Monitoring

### Logs

**Render:**
```bash
# Via dashboard in real-time
```

**Vercel:**
```bash
vercel logs https://your-app.vercel.app
```

### Health Check

Configure monitoring in **[UptimeRobot](https://uptimerobot.com)**:

```
URL: https://your-backend.onrender.com/saude
Interval: 5 minutes
```

---

## Deployment Checklist

- [ ] Backend responding on `https://`
- [ ] CORS configured with frontend
- [ ] Environment variables set
- [ ] Email working
- [ ] Frontend consuming API correctly
- [ ] HTTPS active on both
- [ ] Monitoring configured

---

## ✅ Done! Your portfolio is live!
