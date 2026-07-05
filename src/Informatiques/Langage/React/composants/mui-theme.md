---
# Variable
showMiniToc: true
permissions: true
effectiveDate: 2026-01-04
image: "https://tommisaltiola.gallerycdn.vsassets.io/extensions/tommisaltiola/autofold-md-frontmatter/1.0.5/1710533937767/Microsoft.VisualStudio.Services.Icons.Default"

# Content pour faciliter la recherche
title: Personnalisation des Thèmes Material UI
intro: Apprenez à créer et personnaliser des thèmes Material UI pour adapter vos applications à votre charte graphique
type: Composants UI
topics:
  - Material UI
  - Thèmes
  - Personnalisation

# Information
author: RICHARD Wilfried
featuredLinks:
  prev: Web\composants\mui-color.md
  next: Web\composants\mui-palette.md
changelog:
  - 2026-01-04 : Création du guide sur la personnalisation des thèmes MUI
type:
topics:
image:
---

# Personnalisation des Thèmes Material UI

## Vue d'ensemble

Material UI permet de personnaliser les thèmes pour adapter les couleurs, la typographie et tous les autres aspects de votre projet.

## Variables de configuration principales

- **palette** : Couleurs des composants
- **typography** : Styles de texte
- **spacing** : Espacement
- **breakpoints** : Points de rupture responsifs
- **zIndex** : Ordre de superposition
- **transitions** : Animations
- **components** : Configuration des composants

**Pour la liste complète des variables de thème disponibles**, consultez la [documentation officielle Material UI](https://mui.com/material-ui/customization/default-theme/?expand-path=$.palette)

Un outil pour aider à concevoir et personnaliser les thèmes pour la bibliothèque de composants Material UI. Inclut des modèles de sites basiques pour montrer les différents composants et comment ils sont affectés par le thème : https://zenoo.github.io/mui-theme-creator/

## Variables CSS du thème

Pour générer des variables CSS à partir du thème :

```javascript
const theme = createTheme({
  cssVariables: true,
});
```

Cela génère un style global :

```css
:root {
  --mui-palette-primary-main: #1976d2;
}
```

Générez un thème basé sur les options reçues. Ensuite, passez-le comme accessoire à ThemeProvider. : https://mui.com/material-ui/customization/theming/#api
