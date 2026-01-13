---
versions: 1.0.0
effectiveDate: 2025-12-23
author: RICHARD Wilfried
title: Démarrer avec Turbopack (Next.js)
intro: Guide essentiel pour activer et configurer Turbopack dans Next.js
type: guide
topics:
  - turbopack
  - nextjs
  - bundler
  - performance
  - configuration
image: https://nextjs.org/static/favicon/safari-pinned-tab.svg
---

# Turbopack – Guide de démarrage

Turbopack est un bundler ultra-rapide pour JavaScript et TypeScript, écrit en Rust et intégré à Next.js.

## Pourquoi utiliser Turbopack ?
- Compilation et rafraîchissement ultra-rapides
- Bundling incrémental et paresseux (seulement ce qui est demandé)
- Support natif de React, TypeScript, CSS, images, polices
- Zéro configuration pour les cas courants

## Activation rapide
Ajoutez le flag `--turbopack` à vos scripts dans package.json :

```json
{
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "next build --turbopack",
    "start": "next start"
  }
}
```

## Configuration avancée
Personnalisez Turbopack dans next.config.js :

```js
module.exports = {
  turbopack: {
    resolveAlias: { underscore: 'lodash' },
    resolveExtensions: ['.mdx', '.tsx', '.ts', '.jsx', '.js', '.json'],
    // autres options disponibles
  },
}
```

## À retenir
- Turbopack pour dev est stable, build est en alpha
- Pour les grandes apps, Turbopack accélère le développement
- Consultez la doc officielle Next.js pour les fonctionnalités avancées et limitations
