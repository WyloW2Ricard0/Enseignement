---
versions: 1.0.0
effectiveDate: 2025-12-23
author: RICHARD Wilfried
title: Démarrer avec ESLint
excerpt: Guide essentiel pour configurer et utiliser ESLint dans vos projets JavaScript
type: guide
topics:
	- eslint
	- javascript
	- qualité
	- linter
	- configuration
image: https://eslint.org/icon.png
---

# ESLint – Guide de démarrage

ESLint est un outil de linting configurable pour JavaScript. Il permet de détecter et corriger les erreurs, les problèmes de style et les mauvaises pratiques dans votre code.

## Points essentiels
- Les règles définissent les attentes et corrections sur le code.
- Utilisez des fichiers de configuration (`.eslintrc.*`) pour personnaliser les règles et plugins.
- Les plugins et configurations partageables (ex: Airbnb, React, TypeScript) étendent les fonctionnalités d’ESLint.
- Les correctifs automatiques peuvent être appliqués avec l’option `--fix`.
- Intégrations disponibles pour la plupart des éditeurs (VS Code, WebStorm, etc.).

## Pratique
- Installez ESLint via npm : `npm install eslint --save-dev`
- Initialisez la configuration : `npx eslint --init`
- Lint du code : `npx eslint .`
- Appliquez les correctifs : `npx eslint . --fix`

Pour aller plus loin, consultez la documentation officielle ESLint et explorez les plugins adaptés à votre stack (React, TypeScript, etc.).