---
versions: 1.0.0
effectiveDate: 2025-12-19
author: RICHARD Wilfried

title: GitHub Pages – Guide pratique
excerpt: Tutoriel pour activer, configurer et publier un site statique avec GitHub Pages.
type: guide
topics:
  - github
  - pages
  - site web
  - hébergement
image: "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"

---

# GitHub Pages - Guide Pratique

## Introduction

GitHub Pages héberge gratuitement des sites statiques depuis un dépôt GitHub.

## Activer GitHub Pages

1. Allez dans **Settings** > **Pages**
2. Source : branche `main`
3. Cliquez **Save**
4. Votre site : `https://USERNAME.github.io/mon-site`

## Transformer un dépôt en site web

- **Fichier d'entrée obligatoire** : `index.html` OU `index.md` OU `README.md`
- Le fichier doit être à la racine ou dans un dossier spécifique (docs/ ou autre)
- Le dépôt doit être **public** (ou privé avec GitHub Pro/Team/Enterprise)
- **Nom du dépôt** : `username.github.io` (exactement) pour avoire comme **URL** : `https://username.github.io`
- Fichiers et technologies supportés
  - HTML, CSS, JavaScript
  - Markdown (converti en HTML)
  - Jekyll (générateur de sites statiques)
  - Fichiers statiques (images, fonts, etc.)
- Limitations
  - Taille max du dépôt : **1 GB recommandé**
  - Taille max des fichiers : **100 MB**
  - Bande passante : **100 GB/mois**
  - Builds : **10 builds/heure**

## Ressources
- [Documentation GitHub Pages](https://docs.github.com/pages)
