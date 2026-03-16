import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';

type Language = 'pt' | 'en' | 'es';

interface LanguageContextType {
  language: Language;
  setLanguage: (lang: Language) => void;
  t: (key: string) => string; // Basic fallback translation or keys if needed
}

const LanguageContext = createContext<LanguageContextType | undefined>(undefined);

export const LanguageProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  // Try to get language from localStorage or browser settings
  const getInitialLanguage = (): Language => {
    const saved = localStorage.getItem('portfolio_lang') as Language;
    if (saved && ['pt', 'en', 'es'].includes(saved)) return saved;
    
    const browserLang = navigator.language.split('-')[0];
    if (['pt', 'en', 'es'].includes(browserLang)) return browserLang as Language;
    
    return 'en'; // Default
  };

  const [language, setLanguageState] = useState<Language>(getInitialLanguage);

  const setLanguage = (lang: Language) => {
    setLanguageState(lang);
    localStorage.setItem('portfolio_lang', lang);
    document.documentElement.lang = lang;
  };

  useEffect(() => {
    document.documentElement.lang = language;
  }, [language]);

  // Simple translations for UI elements that don't come from the backend
  const translations: Record<Language, Record<string, string>> = {
    pt: {
      'nav.about': 'Sobre',
      'nav.projects': 'Projetos',
      'nav.stack': 'Stack',
      'nav.experience': 'Experiência',
      'nav.contact': 'Contato',
      'loading': 'Carregando...',
      'error.generic': 'Ocorreu um erro ao carregar os dados.'
    },
    en: {
      'nav.about': 'About',
      'nav.projects': 'Projects',
      'nav.stack': 'Stack',
      'nav.experience': 'Experience',
      'nav.contact': 'Contact',
      'loading': 'Loading...',
      'error.generic': 'An error occurred while loading data.'
    },
    es: {
      'nav.about': 'Sobre',
      'nav.projects': 'Proyectos',
      'nav.stack': 'Stack',
      'nav.experience': 'Experiencia',
      'nav.contact': 'Contacto',
      'loading': 'Cargando...',
      'error.generic': 'Ocurrió un error al cargar los datos.'
    }
  };

  const t = (key: string) => translations[language][key] || key;

  return (
    <LanguageContext.Provider value={{ language, setLanguage, t }}>
      {children}
    </LanguageContext.Provider>
  );
};

export const useLanguage = () => {
  const context = useContext(LanguageContext);
  if (context === undefined) {
    throw new Error('useLanguage must be used within a LanguageProvider');
  }
  return context;
};
