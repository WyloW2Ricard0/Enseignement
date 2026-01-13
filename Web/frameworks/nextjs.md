# Architecture de Base d'un Projet Next.js (Bonnes Pratiques)

## Structure Recommandée

```
mon-app/
├── app/                          # Routes et pages
│   ├── layout.tsx                # Layout racine (HTML, Body)
│   ├── page.tsx                  # Page d'accueil /
│   ├── error.tsx                 # Gestion des erreurs
│   ├── not-found.tsx             # Page 404
│   │
│   ├── _components/              # Composants privés (non routables)
│   │   ├── Header.tsx
│   │   ├── Footer.tsx
│   │   └── Navigation.tsx
│   │
│   ├── (marketing)/              # Groupe de routes (URL: /)
│   │   ├── layout.tsx            # Layout spécifique
│   │   ├── page.tsx              # /
│   │   ├── about/page.tsx        # /about
│   │   └── contact/page.tsx      # /contact
│   │
│   ├── dashboard/                # Section protégée
│   │   ├── layout.tsx
│   │   ├── page.tsx              # /dashboard
│   │   ├── profile/page.tsx      # /dashboard/profile
│   │   └── settings/page.tsx     # /dashboard/settings
│   │
│   ├── blog/
│   │   ├── page.tsx              # /blog (liste)
│   │   └── [slug]/page.tsx       # /blog/mon-article (dynamique)
│   │
│   └── api/                      # Routes API
│       ├── auth/route.ts
│       ├── posts/route.ts
│       └── users/[id]/route.ts
│
├── lib/                          # Fonctions utilitaires réutilisables
│   ├── db.ts                     # Connexion base de données
│   ├── auth.ts                   # Logique authentification
│   ├── api-client.ts             # Client API
│   └── utils.ts                  # Helpers (cn, formatDate, etc.)
│
├── public/                       # Fichiers statiques (images, icônes)
│   ├── images/
│   ├── icons/
│   └── logos/
│
├── styles/                       # Styles globaux
│   └── globals.css
│
├── .env.local                    # Variables d'environnement (Git ignored)
├── .env.example                  # Modèle documentation
├── next.config.ts
├── tsconfig.json
└── package.json
```

## Principes Fondamentaux

### 1️⃣ Server Components par Défaut

**Concept :** Par défaut, tout composant React dans Next.js est un Server Component. Cela signifie que le code s'exécute sur le serveur, pas dans le navigateur de l'utilisateur.

**Pourquoi c'est important :**

- **Sécurité des secrets** : Les clés d'API, tokens, et informations confidentielles restent sur le serveur et ne sont jamais envoyés au client
- **Accès direct à la base de données** : Pas besoin de créer une API intermédiaire pour chaque requête
- **Réduction du JavaScript** : Le code serveur n'est jamais envoyé au navigateur, le bundle est plus léger
- **Performance améliorée** : Les opérations coûteuses (fetch, requêtes DB) se font côté serveur, plus rapide
- **SEO** : Le contenu est rendu sur le serveur, donc les moteurs de recherche le voient directement

**Quand les utiliser :**

- Accès à la base de données
- Opérations asynchrones (fetch de données)
- Traitement de secrets confidentiels
- Logique métier complexe

### 2️⃣ Client Components Seulement si Nécessaire

**Concept :** Un Client Component est marqué avec `'use client'` et s'exécute dans le navigateur. C'est ici qu'on peut utiliser les hooks React et les APIs du navigateur.

**Pourquoi c'est important :**
- **Interactivité** : Seuls les Client Components peuvent avoir de l'état et réagir aux événements utilisateur
- **Minimaliser la taille** : Chaque `'use client'` augmente le bundle JavaScript. Plus on en a, plus lourd c'est
- **Séparation des responsabilités** : Le serveur gère les données, le client gère l'UI interactive

**Quand les utiliser :**
- État local (useState, useReducer)
- Lifecycle effects (useEffect)
- APIs navigateur (localStorage, window, geolocation)
- Gestionnaires d'événements utilisateur (click, submit, hover)
- Hooks personnalisés avec état

### 3️⃣ Organisation des Composants

**Concept :** Les composants réutilisables doivent être organisés au plus proche de là où ils sont utilisés. Les dossiers `_components` (préfixe underscore) ne créent pas de routes et servent de conteneurs privés.

**Logique :**
- Un composant utilisé par une seule page/section doit être dans le dossier `_components` de cette page/section
- Un composant réutilisé partout (Header, Footer) va dans `app/_components`
- Cela facilite la maintenance : en supprimant une section, on supprime aussi ses composants inutiles
- Évite la pollution de la racine avec des centaines de fichiers

**Hiérarchie :**
```
app/
├── _components/                  # Composants globaux (Header, Footer, etc.)
│   ├── (marketing)/
│   │   └── _components/          # Composants du groupe marketing seulement
│   └── dashboard/
│       └── _components/          # Composants du dashboard seulement
```

### 4️⃣ Utilisation des Alias d'Import

**Concept :** Au lieu d'utiliser des chemins relatifs complexes (`../../../lib/db`), on configure des alias dans `tsconfig.json` pour avoir des imports directs (`@/lib/db`).

**Importance :**
- **Lisibilité** : `@/lib/db` est plus clair que `../../../../lib/db`
- **Maintenabilité** : Quand on déplace un fichier, les imports `@/` restent valides
- **Refactoring** : Les outils de refactoring trouvent plus facilement les imports avec alias
- **Cohérence** : Tout le projet utilise les mêmes patterns d'import

**Convention standard :** `@/` pointe toujours vers la racine du projet (ou src/)

### 5️⃣ Variables d'Environnement

**Concept :** Les configurations qui changent selon l'environnement (dev, staging, production) doivent être externalisées dans des fichiers `.env`.

**Distinction critique :**
- Variables `NEXT_PUBLIC_*` : Compilées dans le code client, visibles à tous
- Variables sans `NEXT_PUBLIC_` : Restent côté serveur, jamais exposées

**Sécurité :**
- Les secrets (API keys, database passwords) ne doivent JAMAIS avoir le préfixe `NEXT_PUBLIC_`
- `.env.local` est git-ignored pour protéger les vraies valeurs
- `.env.example` est commité pour documenter quelles variables sont nécessaires

**Objectif :** Pouvoir deployer le même code sur différents serveurs avec des configurations différentes

### 6️⃣ Gestion des Données

**Concept :** Les fonctions de récupération de données sont centralisées dans `lib/` et réutilisables. Elles encapsulent la logique d'accès aux données et gèrent les erreurs.

**Patterns :**
- **Fonctions réutilisables** : Une fonction `getPosts()` peut être appelée de plusieurs pages, composants ou routes API
- **Gestion des erreurs** : Les fonctions doivent gérer les cas d'erreur gracieusement (retourner un défaut ou lancer une exception)
- **Cache et révalidation** : Next.js permet de cacher les réponses fetch et de les révalider périodiquement ou à la demande
- **Typage** : Les fonctions doivent avoir des types clairs (paramètres et retour)

**Avantages :**
- **DRY** : Ne pas répéter la même requête fetch partout
- **Maintenance** : Modifier le source de données dans un seul endroit
- **Testabilité** : Les fonctions peuvent être testées indépendamment
- **Performance** : Le caching peut être appliqué globalement

### 7️⃣ Routes API

**Concept :** Next.js permet de créer des endpoints REST directement dans `app/api/`. Ce sont des routes HTTP qui gèrent les requêtes externes.

**Rôle :**
- **Backend léger** : Pour les opérations qui ne peuvent pas être faites côté client
- **Intégration externe** : Appeler des services externes avec secrets sécurisés
- **Webhooks** : Recevoir des données d'autres services
- **Actions côté serveur** : Traiter les mutations d'une app frontend (mobile, autre)

**Structure :**
- Chaque fichier `route.ts` peut exporter des fonctions `GET`, `POST`, `PUT`, `DELETE`
- Les paramètres dynamiques utilisent `[id]` comme dans les pages
- La réponse est toujours une `Response` JSON

### 8️⃣ Gestion des Erreurs

**Concept :** Next.js capture automatiquement les erreurs en utilisant des error boundaries. Les fichiers `error.tsx` et `not-found.tsx` permettent une gestion gracieuse des erreurs.

**Logique :**
- `error.tsx` capture les erreurs JavaScript non gérées dans ce segment et ses enfants
- `not-found.tsx` affiche une page spécifique quand une ressource n'existe pas (404)
- `global-error.tsx` capture les erreurs qui échappent à tous les autres error boundaries

**Importance :**
- **Expérience utilisateur** : Au lieu de crash, afficher un message utile
- **Récupération** : Permettre à l'utilisateur de réessayer l'action
- **Isolation** : Une erreur dans un composant n'affecte pas le reste de la page
- **Débogage** : Logger les erreurs pour analyse

### 9️⃣ Types TypeScript

**Concept :** Définir les types des données séparement dans `lib/types.ts`. Tous les fichiers importent ces types pour assurer la cohérence.

**Avantages :**
- **Contrat de données** : Tous les composants savent exactement quelles données attendre
- **Autocomplétion** : L'IDE fournit l'autocomplétion basée sur les types
- **Erreurs détectées tôt** : TypeScript signale les erreurs à la compilation, pas à l'exécution
- **Refactoring sûr** : Changer un type montre immédiatement où c'est cassé
- **Documentation** : Les types servent de documentation

**Pattern :** Un seul fichier `lib/types.ts` comme source de vérité pour tous les types du projet

### 🔟 Layouts Imbriqués

**Concept :** Les layouts peuvent être imbriqués à chaque niveau de la hiérarchie. Un layout au niveau `app/` s'applique à tout le site, un layout dans `app/dashboard/` s'applique seulement aux routes du dashboard.

**Logique :**
- Les layouts s'empilent : enfant reçoit le contenu du parent
- Chaque niveau peut ajouter son propre structure HTML (header, sidebar, nav)
- Permet une réutilisation de structure sans duplication
- Facilite la gestion de différentes layouts pour différentes sections du site

**Hiérarchie des layouts :**
```
app/layout.tsx (tous les enfants)
├── (marketing)/layout.tsx (pages marketing)
│   ├── page.tsx (/)
│   ├── about/page.tsx (/about)
├── dashboard/layout.tsx (pages dashboard)
│   ├── page.tsx (/dashboard)
│   ├── profile/page.tsx (/dashboard/profile)
```

**Avantages :**
- Chaque section (marketing, dashboard) peut avoir un design différent
- Réductions de duplication HTML
- Navigation contextuelle (une nav pour marketing, une autre pour dashboard)
- Isolations logiques claires

## Bonnes Pratiques Résumées

| Pratique | ✅ À Faire | ❌ À Éviter |
|----------|-----------|-----------|
| **Composants** | Server par défaut | Client par défaut |
| **Imports** | Alias `@/lib/...` | Chemins relatifs complexes |
| **Données** | Fetch dans Server Components | Fetch dans Client Components |
| **Secrets** | Variables sans `NEXT_PUBLIC_` | Secrets exposés au client |
| **Organisation** | Composants privés `_components` | Tous les fichiers à la racine |
| **Routes** | `app/` avec structure claire | Routes mélangeant tout |
| **Erreurs** | `error.tsx`, `not-found.tsx` | Pas de gestion d'erreurs |
| **Types** | TypeScript strict | JavaScript sans types |
| **Environnement** | `.env.local` + `.env.example` | Hardcoder les valeurs |
| **Cache** | `next: { revalidate: ... }` | Pas de cache |

## Flux Typique d'une Requête

```
1. Utilisateur visite /blog/mon-article
   ↓
2. Next.js match [slug]/page.tsx
   ↓
3. Fetch du paramètre { slug: 'mon-article' }
   ↓
4. Server Component appelle getPosts(slug)
   ↓
5. Récupération données depuis DB/API
   ↓
6. Rendu HTML côté serveur
   ↓
7. Envoi au client + hydration
   ↓
8. Page interactive (Client Components si nécessaire)
```

## Checklist de Démarrage

- ✅ TypeScript configuré
- ✅ Tailwind CSS installé
- ✅ Alias `@/` dans tsconfig.json
- ✅ Structure `app/`, `lib/`, `public/`
- ✅ Layout racine avec HTML/Body
- ✅ `.env.local` + `.env.example`
- ✅ Types TypeScript pour les données
- ✅ Error boundaries (`error.tsx`, `not-found.tsx`)
- ✅ Server Components par défaut
- ✅ Fetch avec cache/revalidation
