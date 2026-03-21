// ===================================================
// Tipos compartidos (sincronizados con backend FastAPI)
// ===================================================

export interface LocalizedString {
  pt: string;
  en: string;
  es: string;
}

export interface Project {
  id: string;
  nome: string;
  descricao_curta: LocalizedString;
  descricao_completa: LocalizedString;
  tecnologias: string[];
  funcionalidades: string[];
  aprendizados: string[];
  repositorio: string | null;
  demo: string | null;
  destaque: boolean;
  imagem: string | null;
}

export interface Skill {
  nome: string;
  categoria: string;
  nivel: number;
  icone: string | null;
}

export interface Experience {
  id: string;
  cargo: LocalizedString;
  empresa: string;
  localizacao: string;
  data_inicio: string;
  data_fim: string | null;
  descricao: LocalizedString;
  tecnologias: string[];
  atual: boolean;
}

export interface Formacao {
  id: string;
  curso: LocalizedString;
  instituicao: string;
  localizacao: string;
  data_inicio: string;
  data_fim: string | null;
  descricao: LocalizedString;
  atual: boolean;
}

export interface About {
  nome: string;
  titulo: string;
  localizacao: string;
  email: string;
  telefone: string;
  github: string;
  linkedin: string;
  descricao: LocalizedString;
  disponibilidade: LocalizedString;
}

// ===================================================
// Cliente de API Centralizado
// ===================================================

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api/v1';

class ApiError extends Error {
  status: number;
  constructor(status: number, message: string) {
    super(message);
    this.status = status;
    this.name = 'ApiError';
  }
}


async function apiGet<T>(path: string): Promise<T> {
  const res = await fetch(`${API_BASE_URL}${path}`);
  if (!res.ok) {
    throw new ApiError(res.status, `API request failed: ${res.status} ${res.statusText} (${path})`);
  }
  return res.json() as Promise<T>;
}

// ===================================================
// Funciones de Fetch (usadas por los hooks de React Query)
// ===================================================

export const fetchAbout = (): Promise<About> =>
  apiGet<About>('/sobre');

export const fetchProjects = async (): Promise<Project[]> => {
  const data = await apiGet<{ projetos: Project[] }>('/projetos');
  if (!data.projetos || !Array.isArray(data.projetos)) return [];
  return data.projetos;
};

export const fetchSkills = async (): Promise<Skill[]> => {
  const data = await apiGet<{ stack: Skill[] }>('/stack');
  return data.stack;
};

export const fetchExperience = async (): Promise<Experience[]> => {
  const data = await apiGet<{ experiencias: Experience[] }>('/experiencias');
  return data.experiencias;
};

export const fetchFormacao = async (): Promise<Formacao[]> => {
  const data = await apiGet<{ formacoes: Formacao[] }>('/formacao');
  return data.formacoes;
};

// ===================================================
// Mutaciones (POST/PUT/DELETE)
// ===================================================

export async function postContact(data: {
  nome: string;
  email: string;
  assunto: string;
  mensagem: string;
  website: string; // Honeypot
  fax: string;     // Honeypot
}, idempotencyKey: string): Promise<void> {
  const res = await fetch(`${API_BASE_URL}/contato`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Idempotency-Key': idempotencyKey,
    },
    body: JSON.stringify(data),
  });

  if (!res.ok) {
    throw new ApiError(res.status, `Failed to submit contact form: ${res.status}`);
  }
}
