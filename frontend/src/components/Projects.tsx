import { useEffect, useState } from 'react';
import { fetchProjects } from '../api';
import type { Project } from '../api';
import { useLanguage } from '../context/LanguageContext';
import { useReveal } from '../hooks/useReveal';

export default function Projects() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);
  const { language, t } = useLanguage();
  const { ref, isVisible } = useReveal();

  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    console.log('Projects component mounted, fetching data...');
    fetchProjects()
      .then(data => {
        console.log('Projects set in state:', data);
        setProjects(data);
      })
      .catch(err => {
        console.error('Projects fetch error:', err);
        setError(err.message || 'Unknown error');
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <section id="projects" className="py-24 max-w-6xl mx-auto px-4 text-center">
        <div className="animate-pulse text-xl text-slate-600 dark:text-slate-400">
          {t('loading')}
        </div>
      </section>
    );
  }

  if (error) {
    return (
      <section id="projects" className="py-24 max-w-6xl mx-auto px-4 text-center text-red-500">
        <h2 className="text-2xl font-bold mb-4">{t('error.generic')}</h2>
        <p>{error}</p>
      </section>
    );
  }

  // If no projects found but no error
  if (projects.length === 0) {
    return (
      <section id="projects" className="py-24 max-w-6xl mx-auto px-4 text-center">
        <h2 className="text-3xl font-bold mb-8 text-slate-900 dark:text-slate-100">{t('nav.projects')}</h2>
        <p className="text-slate-600 dark:text-slate-400">No projects found.</p>
      </section>
    );
  }

  console.log(`Rendering Projects component. Projects count: ${projects.length}`);

  return (
    <section id="projects" className="py-24 max-w-6xl mx-auto px-4">
      <div 
        ref={ref} 
        className={`${isVisible ? 'reveal-visible' : ''}`}
      >
        <h2 className="text-3xl md:text-5xl font-bold mb-12 text-center text-slate-900 dark:text-slate-100">
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-amber-500 to-yellow-500">
            {t('nav.projects')}
          </span>
        </h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {projects.map((project, index) => {
            console.log(`Mapping project ${index}: ${project.nome}`);
            return (
              <div key={project.id} className="glass rounded-2xl p-6 md:p-8 hover:-translate-y-2 transition-smooth group relative overflow-hidden">
                <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-amber-500 to-yellow-500 opacity-0 group-hover:opacity-100 transition-smooth"></div>
                
                <h3 className="text-2xl font-bold text-slate-900 dark:text-slate-100 mb-3">{project.nome}</h3>
                <p className="text-slate-600 dark:text-slate-400 mb-6 leading-relaxed">
                  {project.descricao_curta[language as keyof typeof project.descricao_curta]}
                </p>
                
                <div className="flex flex-wrap gap-2 mb-6">
                  {project.tecnologias.slice(0, 5).map(tech => (
                    <span key={tech} className="bg-slate-200 dark:bg-slate-800 text-amber-600 dark:text-amber-400 text-xs font-medium px-3 py-1 rounded-full border border-slate-300 dark:border-slate-700/50">
                      {tech}
                    </span>
                  ))}
                  {project.tecnologias.length > 5 && (
                    <span className="bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-400 text-xs font-medium px-3 py-1 rounded-full border border-slate-300 dark:border-slate-700/50">
                      +{project.tecnologias.length - 5}
                    </span>
                  )}
                </div>
                
                <div className="flex gap-4 mt-auto pt-4 border-t border-slate-200 dark:border-slate-800">
                  {project.repositorio && (
                    <a href={project.repositorio} target="_blank" rel="noopener noreferrer" className="flex-1 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-200 hover:border-amber-500 hover:text-amber-500 dark:hover:border-amber-500 dark:hover:text-amber-400 transition-colors flex items-center justify-center gap-2 py-2.5 rounded-xl text-sm font-semibold shadow-sm">
                      <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                        <path fillRule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clipRule="evenodd"></path>
                      </svg>
                      GitHub
                    </a>
                  )}
                  {project.demo && (
                    <a href={project.demo} target="_blank" rel="noopener noreferrer" className="flex-1 bg-amber-500 hover:bg-amber-600 text-slate-900 transition-colors flex items-center justify-center gap-2 py-2.5 rounded-xl text-sm font-bold shadow-md shadow-amber-500/20">
                      <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                      Live Demo
                    </a>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
