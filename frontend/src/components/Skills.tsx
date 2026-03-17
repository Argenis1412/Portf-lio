import { useEffect, useState } from 'react';
import { fetchSkills } from '../api';
import type { Skill } from '../api';
import { useLanguage } from '../context/LanguageContext';
import { useReveal } from '../hooks/useReveal';

export default function Skills() {
  const [skills, setSkills] = useState<Skill[]>([]);
  const { t } = useLanguage();
  const { ref, isVisible } = useReveal();

  useEffect(() => {
    fetchSkills()
      .then(data => setSkills(data))
      .catch(err => console.error(err));
  }, []);

  const categories = Array.from(new Set(skills.map(s => s.categoria)));

  return (
    <section id="stack" className="py-16 bg-transparent transition-colors duration-300 relative group overflow-hidden">
      {/* Dynamic hover glow */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-app-primary/5 rounded-full blur-[120px] -z-10 opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
      <div className="max-w-6xl mx-auto px-4">
        <div ref={ref} className={`reveal-hidden ${isVisible ? 'reveal-visible' : ''}`}>
          <h2 className="text-3xl md:text-5xl font-bold mb-12 text-center text-app-text">
            {t('nav.stack')}
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {categories.map(category => (
              <div key={category} className="glass rounded-xl p-6 border border-app-border hover:border-app-primary hover:shadow-[0_0_20px_rgba(212,163,115,0.2)] transition-all duration-300">
                <h3 className="text-xl font-bold text-app-primary mb-5 capitalize tracking-widest">
                  {category.replace('_', ' ')}
                </h3>
                <div className="flex flex-wrap gap-2">
                  {skills.filter(s => s.categoria === category).map(skill => (
                    <span
                      key={skill.nome}
                      className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-sm font-medium bg-app-primary/5 text-app-primary border border-app-primary/20 hover:bg-app-primary/10 transition-colors duration-200"
                    >
                      {skill.nome}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
