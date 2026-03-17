import { useState } from 'react';
import { useLanguage } from '../context/LanguageContext';
import { useReveal } from '../hooks/useReveal';

export default function Contact() {
  const { t } = useLanguage();
  const { ref, isVisible } = useReveal();
  
  const [formData, setFormData] = useState({
    nome: '',
    email: '',
    assunto: 'Contato via Portfólio',
    mensagem: ''
  });
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');

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
    } catch (error) {
      setStatus('error');
    }
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
        <h2 className="text-3xl md:text-5xl font-bold mb-16 text-center text-app-text tracking-widest">
            {t('contact.title')}
        </h2>

        <div className="glass rounded-xl p-8 md:p-12 border border-app-border hover:border-app-primary hover:shadow-[0_0_30px_rgba(212,163,115,0.25)] transition-all duration-300">
          <form onSubmit={handleSubmit} className="flex flex-col gap-6">
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="flex flex-col gap-2">
                <label htmlFor="nome" className="text-sm font-semibold text-app-text">
                  {t('contact.name')}
                </label>
                <input 
                  type="text" 
                  id="nome" 
                  name="nome"
                  required
                  value={formData.nome}
                  onChange={handleChange}
                  className="bg-app-surface border border-app-border rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-app-primary text-app-text transition-smooth"
                />
              </div>

              <div className="flex flex-col gap-2">
                <label htmlFor="email" className="text-sm font-semibold text-app-text">
                  {t('contact.email')}
                </label>
                <input 
                  type="email" 
                  id="email" 
                  name="email"
                  required
                  value={formData.email}
                  onChange={handleChange}
                  className="bg-app-surface border border-app-border rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-app-primary text-app-text transition-smooth"
                />
              </div>
            </div>

            <div className="flex flex-col gap-2">
              <label htmlFor="mensagem" className="text-sm font-semibold text-app-text">
                {t('contact.message')}
              </label>
              <textarea 
                id="mensagem" 
                name="mensagem"
                required
                rows={5}
                value={formData.mensagem}
                onChange={handleChange}
                className="bg-app-surface border border-app-border rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-app-primary text-app-text transition-smooth resize-none"
              ></textarea>
            </div>

            {status === 'success' && (
              <div className="bg-emerald-100 dark:bg-emerald-900/30 text-emerald-700 dark:text-emerald-400 p-4 rounded-xl text-center text-sm font-medium">
                {t('contact.success')}
              </div>
            )}
            
            {status === 'error' && (
              <div className="bg-red-100 dark:bg-red-900/30 text-red-700 dark:text-red-400 p-4 rounded-xl text-center text-sm font-medium">
                {t('contact.error')}
              </div>
            )}

            <button 
              type="submit" 
              disabled={status === 'loading' || status === 'success'}
              className="mt-4 bg-app-primary hover:bg-app-primary-hover text-white font-bold py-4 px-8 rounded-xl transition-all premium-shadow disabled:opacity-50 disabled:cursor-not-allowed uppercase tracking-widest text-sm"
            >
              {status === 'loading' ? t('contact.sending') : t('contact.send')}
            </button>

          </form>
        </div>
      </div>
    </section>
  );
}
