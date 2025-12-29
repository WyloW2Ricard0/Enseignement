# Frontends

## Définition

- **Frameworks** : Un framework est un ***ensemble d’outils***, de bibliothèques et de conventions qui facilite et structure le développement d’applications. 
    - Il fournit une ***architecture de base***, des composants réutilisables et des bonnes pratiques, permettant aux développeurs de se concentrer sur la logique métier plutôt que sur les détails techniques. 
    - Exemples : React, Angular, Vue, Next.js, Svelte.
- **Le frontend** désigne la ***partie visible*** et interactive d'une application ou d'un site web, avec laquelle l'utilisateur interagit directement.
    - Il inclut l'***interface utilisateur***, la navigation, la présentation des données et l'expérience visuelle.
    - Les technologies courantes du frontend sont HTML, CSS, JavaScript et des frameworks.
- **Backends** : Le backend désigne la ***partie invisible*** d’une application ou d’un site web, responsable du traitement des données, de la logique métier, de la gestion des utilisateurs, de la sécurité et de la communication avec les bases de données ou d’autres services.
    - Il fonctionne côté serveur et ***fournit les données ou services nécessaires au frontend***.
    - Exemples de technologies backend : Node.js, Python (Django, Flask), Ruby on Rails, PHP, Java (Spring), .NET.
- **FullStack** : Un développeur ou une application fullstack maîtrise à la fois le frontend (partie visible) et le backend (partie serveur).
    - Le fullstack permet de concevoir, développer et maintenir l’ensemble d’un projet web, de l’interface utilisateur à la gestion des données et de la logique métier côté serveur.
    - Cette polyvalence facilite la compréhension globale du projet et l’intégration entre les différentes couches.

## Comparaison

| Fonctionnalité | Next.js | SvelteKit | Nuxt | TanStack | Astro | Remix | Vite | CRA |
|----------------|:-------:|:---------:|:----:|:--------:|:-----:|:-----:|:----:|:---:|
| Static Assets | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Edge Routing Rules | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Routing Middleware | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | – | – |
| Server-Side Rendering | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | – | – |
| Streaming SSR | ✅ | ✅ | 🟡 | ✅ | ✅ | 🟡 | – | – |
| Incremental Static Regeneration | ✅ | ✅ | ✅ | 🟡 | 🟡 | 🟡 | – | – |
| Image Optimization | ✅ | ✅ | ✅ | – | ✅ | 🟡 | – | – |
| Data Cache | ✅ | – | – | – | – | – | – | – |
| Native OG Image Generation | ✅ | – | ✅ | – | – | – | – | – |
| Multi-runtime support (diff routes) | ✅ | ✅ | ✅ | – | – | – | – | – |
| Multi-runtime support (app) | ✅ | ✅ | ✅ | – | – | – | – | – |
| Output File Tracing | ✅ | ✅ | ✅ | – | – | – | – | – |
| Skew Protection | ✅ | ✅ | 🟡 | – | – | – | – | – |
| Framework Routing Middleware | ✅ | – | 🟡 | – | – | – | – | – |

https://vercel.com/docs/frameworks/full-stack#frameworks-infrastructure-support-matrix