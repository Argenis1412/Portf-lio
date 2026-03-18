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
            <svg className="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path fillRule="evenodd" d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.372.79 1.102.79 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z" clipRule="evenodd" />
            </svg>
          </a>
          <a href={linkedinUrl} target="_blank" rel="noopener noreferrer" className="text-app-muted hover:text-app-primary transition-colors">
            <span className="sr-only">LinkedIn</span>
            <svg className="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true" strokeWidth="1.5">
              <path strokeLinecap="round" strokeLinejoin="round" d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" />
            </svg>
          </a>
          <a href="https://github.com/Argenis1412/portfolio" target="_blank" rel="noopener noreferrer" className="flex items-center gap-2 text-app-muted hover:text-app-primary transition-colors px-4 py-1.5 bg-app-surface-hover rounded-full text-[10px] font-bold uppercase tracking-widest border border-app-border">
            <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>
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
