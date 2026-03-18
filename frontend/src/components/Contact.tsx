import { useState, useEffect } from 'react';
import { useLanguage } from '../context/LanguageContext';
import { useReveal } from '../hooks/useReveal';
import { fetchAbout } from '../api';
import type { About } from '../api';

export default function Contact() {
  const { t, language } = useLanguage();
  const { ref, isVisible } = useReveal();
  const [about, setAbout] = useState<About | null>(null);
  
  const [formData, setFormData] = useState({
    nome: '',
    email: '',
    assunto: 'Contato via Portfólio',
    mensagem: ''
  });
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');

  useEffect(() => {
    fetchAbout()
      .then(setAbout)
      .catch(err => console.error('Error fetching about data for contact:', err));
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (formData.mensagem.length < 10) {
      setStatus('error');
      return;
    }
    
    setStatus('loading');
    
    try {
      const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';
      const response = await fetch(`${API_BASE_URL}/contato`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      });

      if (response.ok) {
        setStatus('success');
        setFormData({ nome: '', email: '', assunto: 'Contato via Portfólio', mensagem: '' });
      } else {
        setStatus('error');
      }
    } catch {
      setStatus('error');
    }
  };

  const handleWhatsApp = () => {
    if (!about?.telefone) return;
    
    // Clean phone number: remove non-digits
    const cleanNumber = about.telefone.replace(/\D/g, '');
    // Ensure it has country code (BR is 55) if it doesn't already
    const finalNumber = cleanNumber.startsWith('55') ? cleanNumber : `55${cleanNumber}`;
    
    const message = language === 'es' 
      ? '¡Hola Argenis! Vi tu portafolio y me gustaría hablar contigo.'
      : language === 'en'
      ? 'Hello Argenis! I saw your portfolio and would like to talk!'
      : 'Olá Argenis! Vi seu portfólio e gostaria de conversar!';
      
    window.open(`https://wa.me/${finalNumber}?text=${encodeURIComponent(message)}`, '_blank');
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
    if (status === 'error') {
      setStatus('idle');
    }
  };

  return (
    <section id="contact" className="py-16 max-w-4xl mx-auto px-4 relative group overflow-hidden">
      {/* Dynamic hover glow */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-app-primary/5 dark:bg-app-primary/10 rounded-full blur-[120px] -z-10 opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
      <div ref={ref} className={`reveal-hidden ${isVisible ? 'reveal-visible' : ''}`}>
        <h2 className="text-3xl md:text-5xl font-bold mb-16 text-center text-app-text tracking-widest uppercase">
            {t('contact.title')}
        </h2>

        <div className="glass rounded-2xl p-8 md:p-12 border border-app-border hover:border-app-primary/50 hover:shadow-[0_0_40px_rgba(212,163,115,0.15)] transition-all duration-500">
          <form onSubmit={handleSubmit} className="flex flex-col gap-8">
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div className="flex flex-col gap-2.5">
                <label htmlFor="nome" className="text-xs font-bold text-app-muted uppercase tracking-widest ml-1">
                  {t('contact.name')}
                </label>
                <input 
                  type="text" 
                  id="nome" 
                  name="nome"
                  required
                  placeholder={t('contact.placeholder.name')}
                  value={formData.nome}
                  onChange={handleChange}
                  className="bg-app-surface/50 border border-app-border rounded-xl px-5 py-3.5 focus:outline-none focus:ring-2 focus:ring-app-primary/50 text-app-text transition-all duration-300 placeholder:text-app-muted/30"
                />
              </div>

              <div className="flex flex-col gap-2.5">
                <label htmlFor="email" className="text-xs font-bold text-app-muted uppercase tracking-widest ml-1">
                  {t('contact.email')}
                </label>
                <input 
                  type="email" 
                  id="email" 
                  name="email"
                  required
                  placeholder={t('contact.placeholder.email')}
                  value={formData.email}
                  onChange={handleChange}
                  className="bg-app-surface/50 border border-app-border rounded-xl px-5 py-3.5 focus:outline-none focus:ring-2 focus:ring-app-primary/50 text-app-text transition-all duration-300 placeholder:text-app-muted/30"
                />
              </div>
            </div>

            <div className="flex flex-col gap-2.5">
              <label htmlFor="mensagem" className="text-xs font-bold text-app-muted uppercase tracking-widest ml-1">
                {t('contact.message')}
              </label>
              <textarea 
                id="mensagem" 
                name="mensagem"
                required
                rows={5}
                placeholder={t('contact.placeholder.message')}
                value={formData.mensagem}
                onChange={handleChange}
                className="bg-app-surface/50 border border-app-border rounded-xl px-5 py-3.5 focus:outline-none focus:ring-2 focus:ring-app-primary/50 text-app-text transition-all duration-300 placeholder:text-app-muted/30 resize-none"
              ></textarea>
            </div>

            {status === 'success' && (
              <div className="bg-emerald-500/10 border border-emerald-500/20 text-emerald-500 p-4 rounded-xl text-center text-sm font-semibold animate-in fade-in slide-in-from-top-2 duration-300">
                {t('contact.success')}
              </div>
            )}
            
            {status === 'error' && (
              <div className="bg-red-500/10 border border-red-500/20 text-red-500 p-4 rounded-xl text-center text-sm font-semibold animate-in fade-in slide-in-from-top-2 duration-300">
                {t('contact.error')}
              </div>
            )}

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-2">
              <button 
                type="submit" 
                disabled={status === 'loading' || status === 'success'}
                className="bg-app-primary hover:bg-app-primary-hover text-white font-bold py-4 px-8 rounded-xl transition-all duration-300 shadow-lg shadow-app-primary/20 disabled:opacity-50 disabled:cursor-not-allowed uppercase tracking-widest text-xs flex items-center justify-center gap-3 active:scale-95"
              >
                {status === 'loading' ? (
                  <svg className="animate-spin h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                ) : (
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                  </svg>
                )}
                {status === 'loading' ? t('contact.sending') : t('contact.send')}
              </button>

              <button 
                type="button" 
                onClick={handleWhatsApp}
                className="bg-[#25D366] hover:bg-[#128C7E] text-white font-bold py-4 px-8 rounded-xl transition-all duration-300 shadow-lg shadow-green-500/20 flex items-center justify-center gap-3 uppercase tracking-widest text-xs active:scale-95"
              >
                <svg className="w-5 h-5 flex-shrink-0" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L0 24l6.335-1.662c1.72 1.041 3.712 1.585 5.703 1.585h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>
                </svg>
                {t('contact.whatsapp')}
              </button>
            </div>

          </form>
        </div>
      </div>
    </section>
  );
}
