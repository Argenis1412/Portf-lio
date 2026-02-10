# 🚀 Guia de Deploy

> **Manual completo para deploy do portfólio em produção**

---

## 📋 Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Deploy Backend](#deploy-backend)
3. [Deploy Frontend](#deploy-frontend)
4. [Monitoramento](#monitoramento)

---

## Pré-requisitos

### Contas Necessárias

- [ ] **GitHub** - Versionamento
- [ ] **Render/Railway** - Hosting backend (gratuito)
- [ ] **Vercel/Netlify** - Hosting frontend (gratuito)
- [ ] **Gmail App Password** - Envio de emails

### Ferramentas

```bash
# Git
git --version  # >= 2.0

# Python
python --version  # >= 3.12

# Node.js
node --version  # >= 20
```

---

## Deploy Backend

### Opção 1: Render.com (Recomendado)

1. **Crie conta em [render.com](https://render.com)**

2. **New → Web Service**

3. **Configurações:**
   ```
   Name: portafolio-api
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn app.principal:app --host 0.0.0.0 --port $PORT
   ```

4. **Variáveis de Ambiente:**
   ```env
   AMBIENTE=producao
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   EMAIL_REMETENTE=seu@email.com
   EMAIL_SENHA=senha_app_gmail
   EMAIL_DESTINO=seu@email.com
   CORS_ORIGINS=https://seu-frontend.vercel.app
   ```

5. **Crie `backend/Dockerfile`:**
   ```dockerfile
   FROM python:3.12-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   COPY . .
   CMD ["uvicorn", "app.principal:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

### Opção 2: Railway

Similar ao Render, mas com PostgreSQL grátis incluído.

---

## Deploy Frontend

### Opção 1: Vercel (Recomendado)

1. **Instale Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy:**
   ```bash
   cd frontend
   vercel --prod
   ```

3. **Configure variável de ambiente:**
   ```
   VITE_API_URL=https://seu-backend.onrender.com/api/v1
   ```

### Opção 2: Netlify

```bash
cd frontend
npm run build
npx netlify-cli deploy --prod --dir=dist
```

---

## Monitoramento

### Logs

**Render:**
```bash
# Via dashboard em real-time
```

**Vercel:**
```bash
vercel logs https://seu-app.vercel.app
```

### Health Check

Configure monitoramento em **[UptimeRobot](https://uptimerobot.com)**:

```
URL: https://seu-backend.onrender.com/saude
Interval: 5 minutos
```

---

## Checklist de Deploy

- [ ] Backend respondendo em `https://`
- [ ] CORS configurado com frontend
- [ ] Variáveis de ambiente setadas
- [ ] Email funcionando
- [ ] Frontend consumindo API corretamente
- [ ] HTTPS ativo em ambos
- [ ] Monitoramento configurado

---

✅ **Pronto! Seu portfólio está no ar!**
