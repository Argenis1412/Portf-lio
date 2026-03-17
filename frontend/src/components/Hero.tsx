import { useLanguage } from '../context/LanguageContext';
import { useReveal } from '../hooks/useReveal';
import profilePic from '../assets/profile/profile.jpg'; // Using the image the user uploaded

export default function Hero() {
  const { t } = useLanguage();
  const { ref, isVisible } = useReveal();

  return (
    <section id="hero" className="pt-20 pb-12 md:pt-28 md:pb-20 px-4 max-w-6xl mx-auto relative overflow-hidden min-h-screen flex items-center">
      {/* Background decoration - very subtle copper glow */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-app-primary/5 rounded-full blur-[120px] -z-10"></div>
      
      <div 
        ref={ref}
        className={`w-full grid grid-cols-1 md:grid-cols-2 gap-12 items-center reveal-hidden ${isVisible ? 'reveal-visible' : ''}`}
      >
        <div className="text-center md:text-left order-2 md:order-1">
          <h1 className="text-4xl md:text-6xl font-extrabold tracking-tight mb-6 text-app-text">
            Backend Developer
          </h1>
          <p className="mt-4 text-lg md:text-xl text-app-muted mb-10 max-w-xl mx-auto md:mx-0">
            {t('hero.subtitle')}
          </p>
          <div className="flex flex-col sm:flex-row justify-center md:justify-start gap-4">
            <a href="#projects" className="bg-app-primary hover:bg-app-primary-hover text-white font-bold py-3 px-8 rounded-full transition-smooth premium-shadow">
              {t('nav.projects')}
            </a>
            <a href="#contact" className="bg-transparent hover:bg-app-surface-hover text-app-text font-semibold py-3 px-8 rounded-full transition-smooth border border-app-border">
              {t('nav.contact')}
            </a>
          </div>
        </div>

        <div className="order-1 md:order-2 flex justify-center md:justify-end relative mr-0 md:mr-4">
          {/* Intense bronze glow background */}
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[308px] h-[308px] md:w-[430px] md:h-[430px] bg-app-primary/20 rounded-full blur-[70px] -z-10 animate-pulse"></div>
          
          <div className="relative w-[276px] h-[276px] md:w-[368px] md:h-[368px] rounded-full p-1.5 bg-gradient-to-tr from-app-primary to-transparent shadow-[0_0_30px_rgba(212,163,115,0.3)]">
            <div className="w-full h-full rounded-full overflow-hidden bg-app-surface-hover flex items-center justify-center relative">
               <img src={profilePic} alt="Profile" className="w-full h-full object-cover rounded-full filter grayscale-[10%] brightness-110" />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
