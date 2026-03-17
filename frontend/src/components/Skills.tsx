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
    <section id="stack" className="py-24 bg-slate-100/50 dark:bg-slate-900/50 transition-colors duration-300">
      <div className="max-w-6xl mx-auto px-4">
        <div ref={ref} className={`reveal-hidden ${isVisible ? 'reveal-visible' : ''}`}>
          <h2 className="text-3xl md:text-5xl font-bold mb-12 text-center text-slate-900 dark:text-slate-100">
            {t('nav.stack')}
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {categories.map(category => (
              <div key={category} className="glass rounded-xl p-6">
                <h3 className="text-xl font-bold text-amber-600 dark:text-amber-500 mb-5 capitalize">
                  {category.replace('_', ' ')}
                </h3>
                <div className="flex flex-wrap gap-2">
                  {skills.filter(s => s.categoria === category).map(skill => (
                    <span
                      key={skill.nome}
                      className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-sm font-medium bg-amber-500/10 text-amber-700 dark:text-amber-300/90 border border-amber-500/20 hover:bg-amber-500/20 transition-colors duration-200"
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
