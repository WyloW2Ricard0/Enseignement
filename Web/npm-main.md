---
versions: 1.0.0
effectiveDate: 2025-12-19
author: RICHARD Wilfried

title: npm : l’essentiel
intro: Guide pratique pour comprendre et utiliser npm, le gestionnaire de paquets Node.js.
type: guide
topics:
  - npm
  - nodejs
  - javascript
  - gestionnaire de paquets
image: "https://upload.wikimedia.org/wikipedia/commons/d/db/Npm-logo.svg"
---

# npm : l’essentiel

npm est le gestionnaire de paquets officiel de Node.js. Il permet d’installer, partager et gérer des dépendances JavaScript pour vos projets.

## Composants principaux
- **Site web** : recherche et gestion de paquets (https://www.npmjs.com)
- **CLI** : interface en ligne de commande (`npm` et `npx`)
- **Registry** : base de données publique des paquets

## Usages courants
- Installer un paquet : `npm install <nom>`
- Installer une dépendance de développement : `npm install --save-dev <nom>`
- Exécuter un paquet sans l’installer : `npx <nom>`
- Initialiser un projet : `npm init`
- Mettre à jour les dépendances : `npm update`
- Publier un paquet : `npm publish`

## Collaboration
- Partage public gratuit, privé payant
- Organisations pour gérer les accès
- Possibilité d’utiliser un registre privé (ex : GitHub Packages, Verdaccio)

## Documentation
- Aide CLI : `npm help` ou `npm <commande> --help`
- Docs officielles : https://docs.npmjs.com/

---
*npm simplifie la gestion des dépendances et le partage de code JavaScript.*