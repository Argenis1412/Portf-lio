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
    <section id="contact" className="py-24 max-w-4xl mx-auto px-4">
      <div ref={ref} className={`reveal-hidden ${isVisible ? 'reveal-visible' : ''}`}>
        <h2 className="text-3xl md:text-5xl font-bold mb-16 text-center text-slate-900 dark:text-slate-100">
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-amber-500 to-yellow-500">
            {t('contact.title')}
          </span>
        </h2>

        <div className="glass rounded-2xl p-8 md:p-12 shadow-xl shadow-amber-500/5">
          <form onSubmit={handleSubmit} className="flex flex-col gap-6">
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="flex flex-col gap-2">
                <label htmlFor="nome" className="text-sm font-semibold text-slate-700 dark:text-slate-300">
                  {t('contact.name')}
                </label>
                <input 
                  type="text" 
                  id="nome" 
                  name="nome"
                  required
                  value={formData.nome}
                  onChange={handleChange}
                  className="bg-slate-50 dark:bg-[#121212] border border-slate-300 dark:border-slate-800 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-amber-500 text-slate-900 dark:text-slate-100 transition-smooth"
                />
              </div>

              <div className="flex flex-col gap-2">
                <label htmlFor="email" className="text-sm font-semibold text-slate-700 dark:text-slate-300">
                  {t('contact.email')}
                </label>
                <input 
                  type="email" 
                  id="email" 
                  name="email"
                  required
                  value={formData.email}
                  onChange={handleChange}
                  className="bg-slate-50 dark:bg-[#121212] border border-slate-300 dark:border-slate-800 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-amber-500 text-slate-900 dark:text-slate-100 transition-smooth"
                />
              </div>
            </div>

            <div className="flex flex-col gap-2">
              <label htmlFor="mensagem" className="text-sm font-semibold text-slate-700 dark:text-slate-300">
                {t('contact.message')}
              </label>
              <textarea 
                id="mensagem" 
                name="mensagem"
                required
                rows={5}
                value={formData.mensagem}
                onChange={handleChange}
                className="bg-slate-50 dark:bg-[#121212] border border-slate-300 dark:border-slate-800 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-amber-500 text-slate-900 dark:text-slate-100 transition-smooth resize-none"
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
              className="mt-4 bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-600 hover:to-yellow-600 text-slate-900 font-bold py-4 px-8 rounded-xl transition-all shadow-lg shadow-amber-500/20 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {status === 'loading' ? t('contact.sending') : t('contact.send')}
            </button>

          </form>
        </div>
      </div>
    </section>
  );
}
