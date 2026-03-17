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

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api/v1';

export const fetchAbout = async (): Promise<About> => {
  const res = await fetch(`${API_BASE_URL}/sobre`);
  if (!res.ok) throw new Error('Failed to fetch about info');
  return res.json();
};

export const fetchProjects = async (): Promise<Project[]> => {
  console.log(`Fetching projects from: ${API_BASE_URL}/projetos`);
  try {
    const res = await fetch(`${API_BASE_URL}/projetos`);
    console.log(`Response status: ${res.status}`);
    
    if (!res.ok) {
      const errorText = await res.text();
      console.error(`Fetch failed: ${res.status} ${res.statusText}`, errorText);
      throw new Error(`Failed to fetch projects: ${res.status}`);
    }
    
    const data = await res.json();
    console.log('Projects data received:', data);
    
    if (!data.projetos || !Array.isArray(data.projetos)) {
      console.error('Unexpected data format:', data);
      return [];
    }
    
    return data.projetos;
  } catch (err) {
    console.error('Error fetching projects:', err);
    throw err;
  }
};

export const fetchSkills = async (): Promise<Skill[]> => {
  const res = await fetch(`${API_BASE_URL}/stack`);
  if (!res.ok) throw new Error('Failed to fetch skills');
  const data = await res.json();
  return data.stack; // The backend returns { stack: [...], por_categoria: {...} }
};

export const fetchExperience = async (): Promise<Experience[]> => {
  const res = await fetch(`${API_BASE_URL}/experiencias`);
  if (!res.ok) throw new Error('Failed to fetch experience');
  const data = await res.json();
  return data.experiencias;
};

export const fetchFormacao = async (): Promise<Formacao[]> => {
  const res = await fetch(`${API_BASE_URL}/formacao`);
  if (!res.ok) throw new Error('Failed to fetch formacao');
  const data = await res.json();
  return data.formacoes;
};
