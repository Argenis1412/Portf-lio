# 🎨 Portfolio Frontend

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss_v4-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)
![Vitest](https://img.shields.io/badge/vitest-%236E9F18.svg?style=for-the-badge&logo=vitest&logoColor=white)

Frontend application of the professional developer portfolio. Consumes the FastAPI backend to display personal information, projects, career timeline, and a contact form.

## ✨ Features

- **Responsive Design**: Mobile-first approach using Tailwind CSS v4.
- **Glassmorphism UI**: Modern aesthetic with glass-like components and smooth animations.
- **i18n Support**: Multilingual interface (English, Portuguese, Spanish) via `LanguageContext`.
- **Dark/Light Mode**: User-selectable theme with system preference detection (`ThemeContext`).
- **Dynamic Content**: All data fetched from the backend REST API at runtime.
- **Scroll Animations**: Elements reveal on scroll using the custom `useReveal` hook.

## 📂 Source Structure

```
src/
├── api.ts              # TypeScript interfaces and all fetch functions (projects, skills, experience, formação)
├── App.tsx             # Root component — renders all page sections
├── main.tsx            # Entry point
├── App.css             # Global base styles
├── index.css           # Tailwind CSS v4 entry point
├── assets/             # Static assets (images, icons)
├── components/         # React functional components (Navbar, Hero, Stack, Projects, etc.)
├── context/            # React Contexts
│   ├── LanguageContext.tsx   # Language state + t() translation function
│   └── ThemeContext.tsx      # Dark/light theme state
├── hooks/              # Custom hooks
│   ├── useReveal.ts    # IntersectionObserver-based scroll reveal
│   └── useFetch.ts     # Generic data-fetching hook with loading/error states
├── services/           # Low-level API client
│   └── api.ts          # fetchApi() generic wrapper with error handling
├── tests/              # Component tests
│   └── App.test.tsx    # Smoke test: App renders without crashing
└── types/              # Shared TypeScript type definitions
```

> **Note**: `pages/` is an empty directory reserved for future page-level components.

## 🚀 Getting Started

### Prerequisites

- **Node.js 18+**
- **npm** (or pnpm)

### Installation

```bash
cd frontend
npm install
```

### Development

```bash
npm run dev
```

The application starts at `http://localhost:5173` by default.

> To connect to the backend, ensure it is running. The API base URL is read from `VITE_API_URL`.
> - **Development default**: `http://127.0.0.1:8000/api/v1`
> - **Production**: set `VITE_API_URL` in your deployment environment.

### Building for Production

```bash
npm run build
```

The optimized static build is generated in the `dist/` directory.

## 🧪 Running Tests

The frontend uses **Vitest** with `@testing-library/react` and a `jsdom` environment. Browser APIs like `IntersectionObserver` and `matchMedia` are mocked in `vitest.setup.ts`.

```bash
# Run tests once
npm run test

# Run in interactive watch mode
npx vitest

# Run with coverage
npx vitest --coverage
```

Tests are located in `src/tests/`. The test suite includes smoke tests that verify the component tree renders correctly with all required Context providers.

## 🛠️ State Management & Contexts

| Context | Purpose |
|---|---|
| `ThemeContext` | Manages `dark` class on `<html>`. Detects system preference on first load. |
| `LanguageContext` | Manages current language (`en`, `pt`, `es`) and exposes the `t()` translation function for UI strings. |

> **i18n tip**: Backend responses include all three languages simultaneously. Use `data.descricao[idioma]` to render the selected language.

## 📝 npm Scripts

| Script | Description |
|---|---|
| `npm run dev` | Start the Vite development server |
| `npm run build` | Type-check and build for production |
| `npm run lint` | Run ESLint |
| `npm run preview` | Preview the production build locally |
| `npm run test` | Run tests with Vitest |
