# 🏗️ Decisões Arquiteturais

> **Documento de Registro de Decisões Arquiteturais (ADR)**  
> Este arquivo documenta as principais decisões técnicas do projeto e suas motivações.

---

## 📚 Índice

1. [Clean Architecture](#1-clean-architecture)
2. [Persistência em JSON](#2-persistência-em-json)
3. [FastAPI como Framework](#3-fastapi-como-framework)
4. [Versionamento de API](#4-versionamento-de-api)
5. [Tratamento de Erros Customizado](#5-tratamento-de-erros-customizado)

---

## 1. Clean Architecture

### Contexto
Precisávamos de uma arquitetura que permitisse escalabilidade, testabilidade e manutenibilidade a longo prazo.

### Decisão
Adotamos **Clean Architecture** com separação em camadas:
- **Controllers** (camada de interface)
- **Use Cases** (lógica de negócio)
- **Entities** (modelos de domínio)
- **Adapters** (repositórios e serviços externos)

### Consequências

**Positivas:**
- ✅ Código altamente testável (93%+ cobertura)
- ✅ Fácil substituição de dependências (JSON → PostgreSQL futuro)
- ✅ Lógica de negócio isolada de frameworks

**Negativas:**
- ⚠️ Maior complexidade inicial
- ⚠️ Mais arquivos para gerenciar

### Status
✅ **Implementado** - Funcionando em produção

---

## 2. Persistência em JSON

### Contexto
Projeto em fase inicial, necessidade de simplicidade sem infraestrutura complexa.

### Decisão
Usar **arquivos JSON** para persistência de dados (`dados/projetos.json`, etc.).

### Consequências

**Positivas:**
- ✅ Zero configuração de banco de dados
- ✅ Fácil versionamento dos dados no Git
- ✅ Ideal para portfólio estático

**Negativas:**
- ⚠️ Não escala para alto volume de escrita
- ⚠️ Sem transações ACID
- ⚠️ Busca menos eficiente

### Migração Futura
Preparado para migração para PostgreSQL via padrão Repository:

```python
# Interface atual
class Repositorio:
    def obter_todos(self) -> List[T]: ...

# Futura implementação
class RepositorioPG(Repositorio):
    def obter_todos(self) -> List[T]:
        return session.query(Modelo).all()
```

### Status
✅ **Implementado** - Suficiente para MVP

---

## 3. FastAPI como Framework

### Contexto
Necessidade de framework moderno com validação automática, documentação e performance.

### Decisão
Escolher **FastAPI** ao invés de Flask/Django.

### Razões

| Critério | FastAPI | Flask | Django |
|----------|---------|-------|--------|
| Performance | ⚡ Assíncrono | 🐌 Sync | 🐌 Sync |
| Validação | ✅ Pydantic | ❌ Manual | ⚠️ Forms |
| Docs Auto | ✅ OpenAPI | ❌ Não | ❌ Não |
| Type Hints | ✅ Nativo | ⚠️ Opcional | ⚠️ Opcional |
| Curva Aprendizado | 📘 Médio | 📗 Fácil | 📕 Alto |

### Consequências

**Positivas:**
- ✅ Documentação Swagger automática
- ✅ Validação de entrada/saída grátis
- ✅ Melhor performance em I/O assíncrono

**Negativas:**
- ⚠️ Ecossistema menor que Django
- ⚠️ Menos bibliotecas third-party

### Status
✅ **Implementado** - Excelente escolha

---

## 4. Versionamento de API

### Contexto
APIs em produção precisam evoluir sem quebrar clientes existentes.

### Decisão
Implementar versionamento via **caminho da URL** (`/api/v1/projetos`).

### Alternativas Consideradas

| Estratégia | Prós | Contras | Decisão |
|-----------|------|---------|---------|
| **URL Path** | 🟢 Explícito, fácil cache | 🔴 Duplicação de código | ✅ **Escolhido** |
| Header | 🟢 URL limpa | 🔴 Difícil testar no browser | ❌ |
| Query Param | 🟢 Fácil implementar | 🔴 Inconsistente | ❌ |

### Implementação

```python
# backend/app/controladores/v1.py
roteador_v1 = APIRouter(prefix="/api/v1")

# Futuro v2 terá mudanças sem quebrar v1
roteador_v2 = APIRouter(prefix="/api/v2")
```

### Status
✅ **Implementado** - Pronto para evolução

---

## 5. Tratamento de Erros Customizado

### Contexto
Erros padrão do FastAPI (`{"detail": "..."}`) não fornecem informações estruturadas para o frontend.

### Decisão
Criar **hierarquia de exceções customizadas** com códigos de erro:

```python
{
    "erro": {
        "codigo": "PROJETO_NAO_ENCONTRADO",
        "mensagem": "Projeto 'xyz' não existe",
        "detalhes": {...}
    }
}
```

### Consequências

**Positivas:**
- ✅ Frontend pode tratar erros específicos
- ✅ Facilita internacionalização
- ✅ Logging estruturado

**Negativas:**
- ⚠️ Mais código para manter

### Códigos de Erro

| Código | HTTP | Descrição |
|--------|------|-----------|
| `PROJETO_NAO_ENCONTRADO` | 404 | Projeto não existe |
| `ERRO_VALIDACAO_ENTRADA` | 422 | Dados inválidos |
| `ERRO_ENVIO_EMAIL` | 500 | Falha no envio |

### Status
✅ **Implementado** - 100% dos endpoints

---

## 📝 Template para Novas Decisões

```markdown
## N. [TÍTULO DA DECISÃO]

### Contexto
[Situação que motivou a decisão]

### Decisão
[O que foi decidido]

### Consequências
**Positivas:**
- ✅ [Benefício 1]

**Negativas:**
- ⚠️ [Custo 1]

### Status
[✅ Implementado | 🚧 Em progresso | ❌ Revertido]
```

---

## 🔄 Histórico de Revisões

| Data | Versão | Autor | Mudança |
|------|--------|-------|---------|
| 2025-01-XX | 1.0 | [Seu Nome] | Versão inicial |

---

**Nota**: Este documento deve ser atualizado sempre que uma decisão técnica significativa for tomada.
