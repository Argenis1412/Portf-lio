# 📊 API Reference

> **Documentação completa dos endpoints da API**

---

## 🌐 Base URL

### Desenvolvimento
```
http://localhost:8000/api/v1
```

### Produção
```
https://seu-backend.onrender.com/api/v1
```

---

## 🔑 Endpoints

### 1. Health Check

**GET** `/saude`

Verifica o status da API.

**Resposta 200:**
```json
{
  "status": "ok",
  "versao_api": "1.0.0",
  "ambiente": "producao",
  "uptime_segundos": 3600.5
}
```

---

### 2. Sobre Mim

**GET** `/api/v1/sobre`

Retorna informações pessoais.

**Resposta 200:**
```json
{
  "nome": "Seu Nome",
  "cargo": "Full Stack Developer",
  "descricao": "Desenvolvedor...",
  "resumo": "Resumo profissional...",
  "foto": "/path/to/photo.jpg",
  "linkedin": "https://linkedin.com/in/...",
  "github": "https://github.com/...",
  "email": "email@exemplo.com"
}
```

---

### 3. Projetos

#### Listar Projetos

**GET** `/api/v1/projetos`

Retorna todos os projetos ordenados por destaque.

**Resposta 200:**
```json
[
  {
    "id": "proj-001",
    "titulo": "Sistema XYZ",
    "descricao": "Descrição do projeto",
    "tecnologias": ["React", "FastAPI", "PostgreSQL"],
    "imagem": "/path/to/image.jpg",
    "link_github": "https://github.com/...",
    "link_demo": "https://demo.com",
    "destaque": true
  }
]
```

#### Obter Projeto Específico

**GET** `/api/v1/projetos/{projeto_id}`

Retorna um projeto pelo ID.

**Parâmetros:**
- `projeto_id` (path) - ID do projeto

**Resposta 200:**
```json
{
  "id": "proj-001",
  "titulo": "Sistema XYZ",
  ...
}
```

**Resposta 404:**
```json
{
  "erro": {
    "codigo": "PROJETO_NAO_ENCONTRADO",
    "mensagem": "Projeto 'proj-999' não encontrado"
  }
}
```

---

### 4. Stack Tecnológico

**GET** `/api/v1/stack`

Retorna tecnologias agrupadas por categoria.

**Resposta 200:**
```json
{
  "Frontend": [
    {
      "nome": "React",
      "icone": "⚛️",
      "nivel": "avancado"
    }
  ],
  "Backend": [...],
  "Database": [...],
  "DevOps": [...]
}
```

---

### 5. Experiências

**GET** `/api/v1/experiencias`

Retorna experiências profissionais ordenadas cronologicamente.

**Resposta 200:**
```json
[
  {
    "id": "exp-001",
    "empresa": "Tech Corp",
    "cargo": "Backend Developer",
    "periodo": "2023 - Atual",
    "descricao": "Responsabilidades...",
    "tecnologias": ["Python", "FastAPI", "Docker"]
  }
]
```

---

### 6. Contato

**POST** `/api/v1/contato`

Envia mensagem de contato via email.

**Body:**
```json
{
  "nome": "João Silva",
  "email": "joao@exemplo.com",
  "assunto": "Proposta de Projeto",
  "mensagem": "Olá, gostaria de discutir..."
}
```

**Resposta 200:**
```json
{
  "mensagem": "Contato enviado com sucesso! Retornarei em breve."
}
```

**Resposta 422 (Validação):**
```json
{
  "erro": {
    "codigo": "ERRO_VALIDACAO_ENTRADA",
    "mensagem": "Dados de entrada inválidos",
    "detalhes": [
      {
        "campo": "email",
        "mensagem": "Email inválido"
      }
    ]
  }
}
```

**Resposta 500 (Erro de Envio):**
```json
{
  "erro": {
    "codigo": "ERRO_ENVIO_EMAIL",
    "mensagem": "Falha ao enviar email: SMTP timeout"
  }
}
```

---

## 🔒 Códigos de Erro

| Código | HTTP | Descrição |
|--------|------|-----------|
| `PROJETO_NAO_ENCONTRADO` | 404 | Projeto não existe |
| `EXPERIENCIA_NAO_ENCONTRADA` | 404 | Experiência não existe |
| `ERRO_VALIDACAO_ENTRADA` | 422 | Dados inválidos (Pydantic) |
| `ERRO_ENVIO_EMAIL` | 500 | Falha no envio de email |
| `ERRO_INTERNO` | 500 | Erro genérico do servidor |

---

## 📝 Schemas Pydantic

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

## 🧪 Exemplos de Uso

### cURL

```bash
# Listar projetos
curl http://localhost:8000/api/v1/projetos

# Enviar contato
curl -X POST http://localhost:8000/api/v1/contato \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João",
    "email": "joao@exemplo.com",
    "assunto": "Teste",
    "mensagem": "Olá, esta é uma mensagem de teste."
  }'
```

### Python (httpx)

```python
import httpx

async with httpx.AsyncClient() as client:
    # Obter sobre
    response = await client.get("http://localhost:8000/api/v1/sobre")
    dados = response.json()
    
    # Enviar contato
    response = await client.post(
        "http://localhost:8000/api/v1/contato",
        json={
            "nome": "João",
            "email": "joao@exemplo.com",
            "assunto": "Proposta",
            "mensagem": "Mensagem..."
        }
    )
```

### JavaScript (fetch)

```javascript
// Listar projetos
const response = await fetch('http://localhost:8000/api/v1/projetos');
const projetos = await response.json();

// Enviar contato
const response = await fetch('http://localhost:8000/api/v1/contato', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    nome: 'João',
    email: 'joao@exemplo.com',
    assunto: 'Proposta',
    mensagem: 'Olá...'
  })
});
```

---

## 📚 Documentação Interativa

Quando o servidor estiver rodando, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

✅ **Para mais detalhes, consulte a documentação interativa!**
