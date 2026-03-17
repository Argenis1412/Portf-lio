import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import App from '../App';
import { LanguageProvider } from '../context/LanguageContext';
import { ThemeProvider } from '../context/ThemeContext';

describe('App Component', () => {
  it('renders without crashing and displays the Navbar', () => {
    render(
      <ThemeProvider>
        <LanguageProvider>
          <App />
        </LanguageProvider>
      </ThemeProvider>
    );
    
    // The Navbar contains the "Portfolio." brand text
    const brandElements = screen.getAllByText(/Portfolio\./i);
    expect(brandElements.length).toBeGreaterThan(0);
  });
});
