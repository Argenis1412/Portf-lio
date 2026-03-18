import { motion, AnimatePresence } from 'framer-motion';
import { Github, Linkedin, Code2, Mail, Copy, Check } from 'lucide-react';
import { useEffect, useState } from 'react';
import { useLanguage } from '../context/LanguageContext';
import { fetchAbout } from '../api';
import type { About } from '../api';

export default function Footer() {
  const { t } = useLanguage();
  const [about, setAbout] = useState<About | null>(null);
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    fetchAbout()
      .then(setAbout)
      .catch(err => console.error('Error fetching about data for footer:', err));
  }, []);

  const handleCopyEmail = () => {
    const email = about?.email || 'argenis.developer@gmail.com';
    navigator.clipboard.writeText(email);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const githubUrl = about?.github || "https://github.com/Argenis1412";
  const linkedinUrl = about?.linkedin || "https://www.linkedin.com/in/argenis1412/";

  return (
    <footer className="w-full bg-transparent border-t border-app-border py-12 mt-12 transition-colors duration-300">
      <div className="max-w-6xl mx-auto px-4 text-center">
        
        {/* Email Copy Badge - Highly valued by recruiters */}
        <div className="flex justify-center mb-8">
          <motion.button 
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={handleCopyEmail}
            className="group flex items-center gap-3 px-5 py-2.5 bg-app-surface border border-app-border rounded-2xl hover:border-app-primary transition-all duration-300 shadow-sm relative overflow-hidden"
          >
            <div className="flex items-center justify-center w-8 h-8 rounded-full bg-app-primary/10 text-app-primary group-hover:bg-app-primary group-hover:text-white transition-colors duration-300">
              <Mail className="w-4 h-4" />
            </div>
            <div className="text-left">
              <p className="text-[10px] uppercase tracking-widest text-app-muted font-bold leading-none mb-1">Email</p>
              <p className="text-sm font-semibold text-app-text">{about?.email || 'argenis.developer@gmail.com'}</p>
            </div>
            <div className="ml-2 pl-3 border-l border-app-border flex items-center justify-center">
              <AnimatePresence mode="wait">
                {copied ? (
                  <motion.div
                    key="check"
                    initial={{ scale: 0, opacity: 0 }}
                    animate={{ scale: 1, opacity: 1 }}
                    exit={{ scale: 0, opacity: 0 }}
                  >
                    <Check className="w-4 h-4 text-emerald-500" />
                  </motion.div>
                ) : (
                  <motion.div
                    key="copy"
                    initial={{ scale: 0, opacity: 0 }}
                    animate={{ scale: 1, opacity: 1 }}
                    exit={{ scale: 0, opacity: 0 }}
                  >
                    <Copy className="w-4 h-4 text-app-muted group-hover:text-app-primary transition-colors" />
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          </motion.button>
        </div>

        <div className="flex items-center justify-center space-x-6 mb-8">
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
        
        <p className="text-xs text-app-muted font-medium tracking-wide">
          {t('footer.rights')}
        </p>
      </div>
    </footer>
  );
}
