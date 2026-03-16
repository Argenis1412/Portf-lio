export interface MultiLanguageText {
  pt: string;
  en: string;
  es: string;
}

export interface About {
  nome: string;
  titulo: MultiLanguageText;
  bio: MultiLanguageText;
  avatar: string | null;
  links: {
    github: string;
    linkedin: string;
    twitter?: string;
    email: string;
  };
}

export interface Project {
  id: string;
  nome: string;
  descricao_curta: MultiLanguageText;
  descricao_completa?: MultiLanguageText;
  tecnologias: string[];
  funcionalidades?: string[];
  aprendizados?: string[];
  repositorio: string;
  demo: string | null;
  destaque: boolean;
  imagem: string | null;
}

export interface StackItem {
  nome: string;
  nivel: 'Iniciante' | 'Intermediário' | 'Avançado' | 'Especialista';
  categoria: string;
  icone: string | null;
}

export interface Experience {
  id: string;
  cargo: MultiLanguageText;
  empresa: string;
  localizacao: string;
  data_inicio: string;
  data_fim: string | null;
  descricao: MultiLanguageText;
  tecnologias: string[];
  atual: boolean;
}
