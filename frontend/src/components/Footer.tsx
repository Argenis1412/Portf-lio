import { Github, Linkedin, Code2 } from 'lucide-react';
import { useEffect, useState } from 'react';
import { useLanguage } from '../context/LanguageContext';
import { fetchAbout } from '../api';
import type { About } from '../api';

export default function Footer() {
  const { t } = useLanguage();
  const [about, setAbout] = useState<About | null>(null);

  useEffect(() => {
    fetchAbout()
      .then(setAbout)
      .catch(err => console.error('Error fetching about data for footer:', err));
  }, []);

  const githubUrl = about?.github || "https://github.com/Argenis1412";
  const linkedinUrl = about?.linkedin || "https://www.linkedin.com/in/argenis1412/";

  return (
    <footer className="w-full bg-transparent border-t border-app-border py-12 mt-12 transition-colors duration-300">
      <div className="max-w-6xl mx-auto px-4 text-center">
        <div className="flex items-center justify-center space-x-6 mb-6">
          <a href={githubUrl} target="_blank" rel="noopener noreferrer" className="text-app-muted hover:text-app-primary transition-colors">
            <span className="sr-only">GitHub</span>
            <Github className="h-6 w-6" />
          </a>
          <a href={linkedinUrl} target="_blank" rel="noopener noreferrer" className="text-app-muted hover:text-app-primary transition-colors">
            <span className="sr-only">LinkedIn</span>
            <Linkedin className="h-6 w-6" />
          </a>
          <a href="https://github.com/Argenis1412/portfolio" target="_blank" rel="noopener noreferrer" className="flex items-center gap-2 text-app-muted hover:text-app-primary transition-colors px-4 py-1.5 bg-app-surface-hover rounded-full text-[10px] font-bold uppercase tracking-widest border border-app-border">
            <Code2 className="w-3 h-3" />
            <span>Source Code</span>
          </a>
        </div>
        <p className="text-sm text-app-muted">
          {t('footer.rights')}
        </p>
      </div>
    </footer>
  );
}
