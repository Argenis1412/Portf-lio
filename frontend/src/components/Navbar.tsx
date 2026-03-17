import { useLanguage } from '../context/LanguageContext';
import { useTheme } from '../context/ThemeContext';

export default function Navbar() {
  const { language, setLanguage, t } = useLanguage();
  const { theme, toggleTheme } = useTheme();

  return (
    <nav className="fixed top-0 w-full z-50 glass">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex-shrink-0 hidden md:block">
            {/* Optional logo or leave empty. Kept div for flex spacing. */}
          </div>
          <div className="hidden md:block">
            <div className="ml-10 flex items-baseline space-x-6">
              <a href="#hero" className="hover:text-app-primary-hover px-3 py-2 rounded-md text-sm font-medium transition-colors text-app-text">
                {t('nav.about')}
              </a>
              <a href="#stack" className="hover:text-app-primary-hover px-3 py-2 rounded-md text-sm font-medium transition-colors text-app-text">
                {t('nav.stack')}
              </a>
              <a href="#projects" className="hover:text-app-primary-hover px-3 py-2 rounded-md text-sm font-medium transition-colors text-app-text">
                {t('nav.projects')}
              </a>
              <a href="#experience" className="hover:text-app-primary-hover px-3 py-2 rounded-md text-sm font-medium transition-colors text-app-text">
                {t('nav.journey')}
              </a>
              <a href="#contact" className="hover:text-app-primary-hover px-3 py-2 rounded-md text-sm font-medium transition-colors text-app-text">
                {t('nav.contact')}
              </a>
            </div>
          </div>
          <div className="flex items-center gap-4">
            <button
              onClick={toggleTheme}
              className="p-2 rounded-full hover:bg-app-surface-hover transition-colors text-app-text"
              aria-label="Toggle Theme"
            >
              {theme === 'dark' ? (
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
              ) : (
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" /></svg>
              )}
            </button>
            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value as any)}
              className="bg-app-surface border border-app-border text-sm rounded-lg focus:ring-amber-500 focus:border-amber-500 block p-2 transition-smooth shadow-sm text-app-text"
            >
              <option value="pt">PT</option>
              <option value="en">EN</option>
              <option value="es">ES</option>
            </select>
          </div>
        </div>
      </div>
    </nav>
  );
}
