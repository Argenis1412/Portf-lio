Write-Host "Iniciando Backend FastAPI..." -ForegroundColor Cyan
cd backend
.\.venv\Scripts\python.exe -m uvicorn app.principal:app --reload --port 8000
