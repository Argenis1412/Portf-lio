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
      'contact.error': 'Erro ao enviar mensagem. Por favor, tente novamente.',
      'contact.whatsapp': 'Conversar no WhatsApp',
      'contact.subject_default': 'Contato via Portfólio',
      'contact.placeholder.name': 'Seu nome',
      'contact.placeholder.email': 'exemplo@email.com',
      'contact.placeholder.message': 'Como posso te ajudar?',
      'contact.subject': 'Assunto',
      'contact.placeholder.subject': 'Assunto da mensagem',
      'contact.copy_email': 'Copiar E-mail',
      'contact.email_copied': 'E-mail copiado!',
      'contact.copy_whatsapp': 'Copiar WhatsApp',
      'contact.whatsapp_copied': 'Número copiado!',
      'contact.error.name_required': 'Por favor, insira seu nome.',
      'contact.error.email_required': 'Por favor, insira seu e-mail.',
      'contact.error.email_invalid': 'Por favor, insira um e-mail válido.',
      'contact.error.subject_required': 'Por favor, insira o assunto.',
      'contact.error.subject_too_short': 'O assunto deve ter pelo menos 5 caracteres.',
      'contact.error.message_required': 'Por favor, insira sua mensagem.',
      'contact.error.message_too_short': 'A mensagem deve ter pelo menos 10 caracteres.',
      'contact.error.duplicate': 'Esta mensagem já foi enviada. Já recebemos sua consulta, obrigado!',
      'contact.error.rate_limit': 'Você atingiu o limite de mensagens permitidas por agora. Tente novamente mais tarde.'
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
      'contact.error': 'Error sending message. Please try again.',
      'contact.whatsapp': 'Chat on WhatsApp',
      'contact.subject_default': 'Contact from Portfolio',
      'contact.placeholder.name': 'Your name',
      'contact.placeholder.email': 'example@email.com',
      'contact.placeholder.message': 'How can I help you?',
      'contact.subject': 'Subject',
      'contact.placeholder.subject': 'Message subject',
      'contact.copy_email': 'Copy Email',
      'contact.email_copied': 'Email copied!',
      'contact.copy_whatsapp': 'Copy WhatsApp',
      'contact.whatsapp_copied': 'Number copied!',
      'contact.error.name_required': 'Please enter your name.',
      'contact.error.email_required': 'Please enter your email.',
      'contact.error.email_invalid': 'Please enter a valid email address.',
      'contact.error.subject_required': 'Please enter a subject.',
      'contact.error.subject_too_short': 'Subject must be at least 5 characters long.',
      'contact.error.message_required': 'Please enter your message.',
      'contact.error.message_too_short': 'Message must be at least 10 characters long.',
      'contact.error.duplicate': 'This message has already been sent. We have already received your inquiry, thank you!',
      'contact.error.rate_limit': 'You have reached the limit of messages allowed for now. Please try again later.'
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
      'contact.error': 'Error al enviar el mensaje. Por favor, inténtelo de nuevo.',
      'contact.whatsapp': 'Chatear por WhatsApp',
      'contact.subject_default': 'Contacto desde Portafolio',
      'contact.placeholder.name': 'Tu nombre',
      'contact.placeholder.email': 'ejemplo@correo.com',
      'contact.placeholder.message': '¿En qué puedo ayudarte?',
      'contact.subject': 'Asunto',
      'contact.placeholder.subject': 'Asunto del mensaje',
      'contact.copy_email': 'Copiar Correo',
      'contact.email_copied': '¡Correo copiado!',
      'contact.copy_whatsapp': 'Copiar WhatsApp',
      'contact.whatsapp_copied': '¡Número copiado!',
      'contact.error.name_required': 'Por favor, ingresa tu nombre.',
      'contact.error.email_required': 'Por favor, ingresa tu correo.',
      'contact.error.email_invalid': 'Por favor, ingresa un correo válido.',
      'contact.error.subject_required': 'Por favor, ingresa el asunto.',
      'contact.error.subject_too_short': 'El asunto debe tener al menos 5 caracteres.',
      'contact.error.message_required': 'Por favor, ingresa tu mensaje.',
      'contact.error.message_too_short': 'El mensaje debe tener al menos 10 caracteres.',
      'contact.error.duplicate': 'Este mensaje ya ha sido enviado. ¡Ya recibimos tu consulta, gracias!',
      'contact.error.rate_limit': 'Has alcanzado el límite de mensajes permitidos por ahora. Inténtalo de nuevo más tarde.'
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
