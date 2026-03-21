# 🎨 Portfolio Frontend

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![TanStack Query](https://img.shields.io/badge/-TanStack%20Query-FF4154?style=for-the-badge&logo=react-query&logoColor=white)
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss_v4-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

Frontend application for a professional portfolio. Featuring declarative data management, advanced caching, and a highly maintainable i18n system.

## ✨ Key Features

- **Declarative Data (React Query)**: Automatic caching (5-10 min stale time), background refetching, and built-in loading/error states.
- **Externalized i18n**: Multi-language support (EN, PT, ES) managed via decoupled JSON files in `src/i18n/`.
- **Responsive & Premium UI**: Mobile-first Tailwind CSS v4 with glassmorphism effects and Framer Motion orchestrations.
- **Performance Optimized**: Image lazy-loading and `fetchPriority` for better LCP metrics.
- **Git Hooks**: Husky + lint-staged prevent committing code with lint errors or failing tests.

## 📂 Source Structure

```
src/
├── api.ts              # API Client & Shared Interfaces
├── hooks/
│   └── useApi.ts       # React Query hooks for all endpoints
├── i18n/
│   ├── en.json         # English translations
│   ├── pt.json         # Portuguese (BR) translations
│   └── es.json         # Spanish translations
├── context/
│   ├── LanguageContext.tsx   # Language state + i18n loader
│   └── ThemeContext.tsx      # Dark/light theme state
├── components/         # Atomic UI components
└── App.tsx             # Main layout orchestrator
```

## 🚀 Getting Started

```bash
cd frontend
npm install
npm run dev
```

### 🛠️ Maintenance Scripts

| Script | Description |
|---|---|
| `npm run build` | Production-ready build with type-checking |
| `npm run lint` | ESLint static analysis |
| `npm run test` | Unit tests with Vitest |
| `npm run prepare`| Initialize Husky (automatically runs on install) |

## 🧪 Testing Strategy

The project uses **Vitest** + **@testing-library/react**.
- **Unit Tests**: Business logic and component rendering.
- **Quality Gate**: Husky blocks commits if `npm run lint` or `npm run test` fail on staged files.
ction |
| `npm run lint` | Run ESLint |
| `npm run preview` | Preview the production build locally |
| `npm run test` | Run tests with Vitest |
