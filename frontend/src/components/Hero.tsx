import { useLanguage } from '../context/LanguageContext';
import { useReveal } from '../hooks/useReveal';
import profilePic from '../assets/profile/profile.jpg'; // Using the image the user uploaded

export default function Hero() {
  const { t } = useLanguage();
  const { ref, isVisible } = useReveal();

  return (
    <section id="hero" className="pt-32 pb-16 md:pt-48 md:pb-32 px-4 max-w-6xl mx-auto relative overflow-hidden min-h-[85vh] flex items-center">
      {/* Background decoration */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-amber-500/10 dark:bg-amber-500/15 rounded-full blur-3xl -z-10"></div>
      
      <div 
        ref={ref}
        className={`w-full grid grid-cols-1 md:grid-cols-2 gap-12 items-center reveal-hidden ${isVisible ? 'reveal-visible' : ''}`}
      >
        <div className="text-center md:text-left order-2 md:order-1">
          <h1 className="text-4xl md:text-6xl font-extrabold tracking-tight mb-6 text-app-text">
            <span className="block mb-2">Building Digital</span>
            <span className="block text-transparent bg-clip-text bg-gradient-to-r from-amber-500 to-yellow-500">
              Experiences
            </span>
          </h1>
          <p className="mt-4 text-lg md:text-xl text-app-muted mb-10 max-w-xl mx-auto md:mx-0">
            {t('hero.subtitle')}
          </p>
          <div className="flex flex-col sm:flex-row justify-center md:justify-start gap-4">
            <a href="#projects" className="bg-amber-500 hover:bg-amber-600 text-slate-900 font-bold py-3 px-8 rounded-full transition-smooth shadow-lg shadow-amber-500/20">
              {t('nav.projects')}
            </a>
            <a href="#contact" className="bg-white dark:bg-app-surface hover:bg-app-surface-hover text-app-text font-semibold py-3 px-8 rounded-full transition-smooth border border-app-border">
              {t('nav.contact')}
            </a>
          </div>
        </div>

        <div className="order-1 md:order-2 flex justify-center md:justify-end">
          <div className="relative w-64 h-64 md:w-80 md:h-80 rounded-full p-2 bg-gradient-to-tr from-amber-500 to-yellow-500 shadow-2xl shadow-amber-500/10">
            <div className="w-full h-full rounded-full overflow-hidden bg-app-surface-hover flex items-center justify-center">
               <img src={profilePic} alt="Profile" className="w-full h-full object-cover rounded-full" />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
