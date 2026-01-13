# Documentation du fichier package.json

## Vue d'ensemble

Le fichier `package.json` est le manifeste du projet Next.js. Il définit les métadonnées, dépendances et scripts nécessaires au fonctionnement de l'application.

## Structure du fichier

### Informations du projet

- **name** : Identifiant unique du projet (format kebab-case)
- **version** : Version sémantique (MAJOR.MINOR.PATCH)
- **description** : Description courte du projet
- **private** : Empêche la publication accidentelle sur npm

### Scripts disponibles

| Ordre | Commande | Description | Utilisation |
| ----- |----------|-------------|-------------|
| 0 | `npm install` | Installation des dépendances | Lit le fichier `package.json` |
| 1 | `npm run dev` | Lance le serveur de développement sur http://localhost:3000 | Développement local avec hot-reload |
| 2 | `npm run lint` | Vérifie la qualité du code avec ESLint | Avant commit |
| 3 | `npm run build` | Génère la version optimisée pour la production | Avant déploiement |
| 4 | `npm run start` | Démarre le serveur de production | Après `npm run build` |

Vercel utilise automatiquement les scripts définis :

- **Lors du déploiement** : `npm install` puis `npm run build`
- **Lors de l'exécution** : `npm run start` (ou Next.js start optimisé)

### Dépendances de production

- **next** : Framework React pour le rendu côté serveur et génération statique
- **react** : Bibliothèque principale pour construire l'interface utilisateur
- **react-dom** : Package pour le rendu DOM de React

> **Note** : Le symbole `^` permet les mises à jour mineures automatiques (ex: ^14.0.0 accepte 14.x.x)

### Dépendances de développement

- **eslint** : Outil de vérification de la qualité du code
- **eslint-config-next** : Configuration ESLint optimisée pour Next.js

### Exigences moteur

Les `engines` garantissent que Vercel utilise les bonnes versions de Node.js et npm.

Définit les versions minimales requises :

- Node.js version 18 ou supérieure
- npm version 9 ou supérieure

> **Important** : Vercel utilise automatiquement ces contraintes lors du déploiement

### Informations du dépôt

- type: git,
- url: https://github.com/WyloW2Ricard0/wylow2ricard0.github.io.git

### Métadonnées

- **keywords** : Mots-clés pour le référencement du projet
- **author** : Créateur du projet
- **license** : Type de licence open-source (MIT = permissive)

## Bonnes pratiques

1. **Versionning sémantique** : Respecter le format MAJOR.MINOR.PATCH
2. **Scripts clairs** : Utiliser des noms de scripts explicites
3. **Dépendances minimales** : N'installer que le strict nécessaire
4. **Lock file** : Toujours versionner `package-lock.json`
5. **Engines** : Définir les versions minimales pour éviter les incompatibilités

## Ressources

- [Documentation Next.js](https://nextjs.org/docs)
- [Documentation npm](https://docs.npmjs.com/cli/v9/configuring-npm/package-json)
- [Versioning sémantique](https://semver.org/lang/fr/)
- [Vercel CLI](https://vercel.com/docs/cli)