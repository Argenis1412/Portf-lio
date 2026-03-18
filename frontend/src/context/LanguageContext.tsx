import React, { createContext, useContext, useState, useEffect } from 'react';
import type { ReactNode } from 'react';

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
      'nav.journey': 'Trajetória',
      'nav.contact': 'Contato',
      'hero.subtitle': 'Python • FastAPI • Clean Architecture\n\nCriando APIs seguras e escaláveis com testes automatizados e lógica de negócios determinística.',
      'footer.rights': '© 2026 Portfolio. Todos os direitos reservados.',
      'loading': 'Carregando...',
      'error.generic': 'Ocorreu um erro ao carregar os dados.',
      'contact.title': 'Entre em Contato',
      'contact.name': 'Nome',
      'contact.email': 'E-mail',
      'contact.message': 'Mensagem',
      'contact.send': 'Enviar Mensagem',
      'contact.sending': 'Enviando...',
      'contact.success': 'Mensagem enviada com sucesso!',
      'contact.error': 'Erro ao enviar. A mensagem deve ter pelo menos 10 caracteres.',
      'contact.whatsapp': 'Conversar no WhatsApp',
      'contact.placeholder.name': 'Seu nome',
      'contact.placeholder.email': 'exemplo@email.com',
      'contact.placeholder.message': 'Como posso te ajudar?'
    },
    en: {
      'nav.about': 'About',
      'nav.projects': 'Projects',
      'nav.stack': 'Stack',
      'nav.experience': 'Experience',
      'nav.journey': 'Journey',
      'nav.contact': 'Contact',
      'hero.subtitle': 'Python • FastAPI • Clean Architecture\n\nBuilding secure and scalable APIs with automated testing and deterministic business logic.',
      'footer.rights': '© 2026 Portfolio. All rights reserved.',
      'loading': 'Loading...',
      'error.generic': 'An error occurred while loading data.',
      'contact.title': 'Get in Touch',
      'contact.name': 'Name',
      'contact.email': 'Email',
      'contact.message': 'Message',
      'contact.send': 'Send Message',
      'contact.sending': 'Sending...',
      'contact.success': 'Message sent successfully!',
      'contact.error': 'Error sending. Message must be at least 10 characters long.',
      'contact.whatsapp': 'Chat on WhatsApp',
      'contact.placeholder.name': 'Your name',
      'contact.placeholder.email': 'example@email.com',
      'contact.placeholder.message': 'How can I help you?'
    },
    es: {
      'nav.about': 'Sobre',
      'nav.projects': 'Proyectos',
      'nav.stack': 'Stack',
      'nav.experience': 'Experiencia',
      'nav.journey': 'Trayectoria',
      'nav.contact': 'Contacto',
      'hero.subtitle': 'Python • FastAPI • Clean Architecture\n\nCreando APIs seguras y escalables con pruebas automatizadas y lógica de negocio determinística.',
      'footer.rights': '© 2026 Portfolio. Todos los derechos reservados.',
      'loading': 'Cargando...',
      'error.generic': 'Ocurrió un error al cargar los datos.',
      'contact.title': 'Contáctame',
      'contact.name': 'Nombre',
      'contact.email': 'Correo',
      'contact.message': 'Mensaje',
      'contact.send': 'Enviar Mensaje',
      'contact.sending': 'Enviando...',
      'contact.success': '¡Mensaje enviado con éxito!',
      'contact.error': 'Error al enviar. El mensaje debe tener al menos 10 caracteres.',
      'contact.whatsapp': 'Chatear por WhatsApp',
      'contact.placeholder.name': 'Tu nombre',
      'contact.placeholder.email': 'ejemplo@correo.com',
      'contact.placeholder.message': '¿En qué puedo ayudarte?'
    }
  };

  const t = (key: string) => translations[language][key] || key;

  return (
    <LanguageContext.Provider value={{ language, setLanguage, t }}>
      {children}
    </LanguageContext.Provider>
  );
};

// eslint-disable-next-line react-refresh/only-export-components
export const useLanguage = () => {
  const context = useContext(LanguageContext);
  if (context === undefined) {
    throw new Error('useLanguage must be used within a LanguageProvider');
  }
  return context;
};
