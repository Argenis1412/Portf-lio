# 📊 API Reference

> **Full documentation of API endpoints**

---

## 🌐 Base URL

### Development
```
http://localhost:8000/api/v1
```

### Production
```
https://your-backend.onrender.com/api/v1
```

---

## 🔑 Endpoints

### 1. Health Check

**GET** `/saude`

Verifies the API status.

**Response 200:**
```json
{
  "status": "ok",
  "api_version": "1.0.0",
  "environment": "production",
  "uptime_seconds": 3600.5
}
```

---

### 2. About Me

**GET** `/api/v1/sobre`

Returns personal information.

**Response 200:**
```json
{
  "nome": "Your Name",
  "cargo": "Full Stack Developer",
  "descricao": "Developer...",
  "resumo": "Professional summary...",
  "foto": "/path/to/photo.jpg",
  "linkedin": "https://linkedin.com/in/...",
  "github": "https://github.com/...",
  "email": "email@example.com"
}
```

---

### 3. Projects

#### List Projects

**GET** `/api/v1/projetos`

Returns all projects ordered by featured status.

**Response 200:**
```json
[
  {
    "id": "proj-001",
    "titulo": "System XYZ",
    "descricao": "Project description",
    "tecnologias": ["React", "FastAPI", "PostgreSQL"],
    "imagem": "/path/to/image.jpg",
    "link_github": "https://github.com/...",
    "link_demo": "https://demo.com",
    "destaque": true
  }
]
```

#### Get Specific Project

**GET** `/api/v1/projetos/{projeto_id}`

Returns a project by ID.

**Parameters:**
- `projeto_id` (path) - Project ID

**Response 200:**
```json
{
  "id": "proj-001",
  "titulo": "System XYZ",
  ...
}
```

**Response 404:**
```json
{
  "erro": {
    "codigo": "PROJECT_NOT_FOUND",
    "mensagem": "Project 'proj-999' not found"
  }
}
```

---

### 4. Technical Stack

**GET** `/api/v1/stack`

Returns technologies grouped by category.

**Response 200:**
```json
{
  "Frontend": [
    {
      "nome": "React",
      "icone": "⚛️",
      "nivel": "advanced"
    }
  ],
  "Backend": [...],
  "Database": [...],
  "DevOps": [...]
}
```

---

### 5. Experiences

**GET** `/api/v1/experiencias`

Returns professional experiences ordered chronologically.

**Response 200:**
```json
[
  {
    "id": "exp-001",
    "empresa": "Tech Corp",
    "cargo": "Backend Developer",
    "periodo": "2023 - Present",
    "descricao": "Responsibilities...",
    "tecnologias": ["Python", "FastAPI", "Docker"]
  }
]
```

---

### 6. Contact

**POST** `/api/v1/contato`

Sends a contact message via email.

**Body:**
```json
{
  "nome": "John Doe",
  "email": "john@example.com",
  "assunto": "Project Proposal",
  "mensagem": "Hello, I would like to discuss..."
}
```

**Response 200:**
```json
{
  "mensagem": "Contact sent successfully! I will return soon."
}
```

**Response 422 (Validation):**
```json
{
  "erro": {
    "codigo": "INPUT_VALIDATION_ERROR",
    "mensagem": "Invalid input data",
    "detalhes": [
      {
        "campo": "email",
        "mensagem": "Invalid email"
      }
    ]
  }
}
```

**Response 500 (Send Error):**
```json
{
  "erro": {
    "codigo": "EMAIL_SEND_ERROR",
    "mensagem": "Failed to send email: SMTP timeout"
  }
}
```

---

## 🔒 Error Codes

| Code | HTTP | Description |
|--------|------|-----------|
| `PROJECT_NOT_FOUND` | 404 | Project does not exist |
| `EXPERIENCE_NOT_FOUND` | 404 | Experience does not exist |
| `INPUT_VALIDATION_ERROR` | 422 | Invalid data (Pydantic) |
| `EMAIL_SEND_ERROR` | 500 | Email sending failure |
| `INTERNAL_ERROR` | 500 | Generic server error |

---

## 📝 Pydantic Schemas

### RespostaSobre
```python
class RespostaSobre(BaseModel):
    nome: str
    cargo: str
    descricao: str
    resumo: str
    foto: str
    linkedin: str
    github: str
    email: EmailStr
```

### RespostaProjeto
```python
class RespostaProjeto(BaseModel):
    id: str
    titulo: str
    descricao: str
    tecnologias: List[str]
    imagem: str
    link_github: Optional[str] = None
    link_demo: Optional[str] = None
    destaque: bool = False
```

### RequisicaoContato
```python
class RequisicaoContato(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    assunto: str = Field(..., min_length=3, max_length=200)
    mensagem: str = Field(..., min_length=10, max_length=2000)
```

---

## 🧪 Usage Examples

### cURL

```bash
# List projects
curl http://localhost:8000/api/v1/projetos

# Send contact
curl -X POST http://localhost:8000/api/v1/contato \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "John",
    "email": "john@example.com",
    "assunto": "Test",
    "mensagem": "Hello, this is a test message."
  }'
```

### Python (httpx)

```python
import httpx

async with httpx.AsyncClient() as client:
    # Get about
    response = await client.get("http://localhost:8000/api/v1/sobre")
    data = response.json()
    
    # Send contact
    response = await client.post(
        "http://localhost:8000/api/v1/contato",
        json={
            "nome": "John",
            "email": "john@example.com",
            "assunto": "Proposal",
            "mensagem": "Message..."
        }
    )
```

### JavaScript (fetch)

```javascript
// List projects
const response = await fetch('http://localhost:8000/api/v1/projetos');
const projects = await response.json();

// Send contact
const response = await fetch('http://localhost:8000/api/v1/contato', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    nome: 'John',
    email: 'john@example.com',
    assunto: 'Proposal',
    mensagem: 'Hello...'
  })
});
```

---

## 📚 Interactive Documentation

When the server is running, access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

✅ **For more details, refer to the interactive documentation!**
