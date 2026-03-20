import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import App from '../App';
import { LanguageProvider } from '../context/LanguageContext';
import { ThemeProvider } from '../context/ThemeContext';

describe('App Component', () => {
  it('renders without crashing and displays the Navbar', async () => {
    render(
      <ThemeProvider>
        <LanguageProvider>
          <App />
        </LanguageProvider>
      </ThemeProvider>
    );
    
    // The Navbar contains the "Portfolio." brand text.
    // Using findAllByText() waits for async state updates triggered by initial fetches,
    // preventing React's "not wrapped in act(...)" warnings.
    const brandElements = await screen.findAllByText(/Portfolio\./i);
    expect(brandElements.length).toBeGreaterThan(0);
  });
});
