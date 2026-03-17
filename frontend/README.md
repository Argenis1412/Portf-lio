# 🎨 Portfolio Frontend

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)

Frontend application for the professional developer portfolio. It consumes the FastAPI backend to display personal information, projects, career timeline, and a contact form.

## ✨ Features

- **Responsive Design**: Mobile-first approach using Tailwind CSS.
- **Glassmorphism UI**: Modern aesthetic with glass-like components and smooth animations.
- **i18n Support**: Multilingual interface (English, Portuguese, Spanish) with `LanguageContext`.
- **Dark/Light Mode**: User-selectable theme with system preference detection (`ThemeContext`).
- **Dynamic Content**: Fetched directly from the backend API.
- **Scroll Animations**: Elements reveal smoothly on scroll using a custom `useReveal` hook.

## 📂 Structure

```
src/
├── api/             # API client functions (fetch wrappers)
├── assets/          # Static assets (images, etc.)
├── components/      # React functional components
├── context/         # React Context (Language, Theme)
├── hooks/           # Custom React hooks (useReveal)
├── locales/         # i18n translation strings
├── App.tsx          # Main application component
└── main.tsx         # Entry point
```

## 🚀 Getting Started

### Prerequisites

- Node.js 18+
- npm or pnpm

### Installation

```bash
cd frontend
npm install
```

### Development

```bash
# Start the Vite development server
npm run dev
```

The application will be available at `http://localhost:5174` (or another port if 5174 is in use).

### Building for Production

```bash
npm run build
```

The optimized static build will be generated in the `dist/` directory.

## 🔗 Environment Setup

To connect to the backend, ensure your backend is running. By default, the `api/index.ts` determines the base URL:
- In production, it uses the origin of the host.
- In development, it points to `http://localhost:8000`.

## 🛠️ State Management & Contexts

- **ThemeContext**: Manages the `dark` class on the HTML `documentElement`.
- **LanguageContext**: Manages the current language (`en`, `pt`, `es`) and provides the `t()` translation function.

## 📝 Scripts

- `npm run dev`: Starts the development server.
- `npm run build`: Builds the app for production.
- `npm run lint`: Runs ESLint to catch potential issues.
- `npm run preview`: Previews the production build locally.
