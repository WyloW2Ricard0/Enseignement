---
# Variable
showMiniToc: true
permissions: true
effectiveDate: 2026-01-04
image: "https://tommisaltiola.gallerycdn.vsassets.io/extensions/tommisaltiola/autofold-md-frontmatter/1.0.5/1710533937767/Microsoft.VisualStudio.Services.Icons.Default"

# Content pour faciliter la recherche
title: Personnalisation de la Palette Material UI
intro: Maîtrisez la personnalisation des couleurs dans Material UI avec les palettes, seuils de contraste et décalages tonals
type: Composants UI
topics:
  - Material UI
  - Palette
  - Personnalisation

# Information
author: RICHARD Wilfried
featuredLinks:
  prev: Web\composants\mui-theme.md
changelog:
  - 2026-01-04 : Création du guide sur la personnalisation de la palette MUI
---

# Personnalisation de la Palette Material UI

## Vue d'ensemble

La palette définit les couleurs de votre thème Material UI. Vous pouvez personnaliser les couleurs primaires, secondaires et autres couleurs sémantiques.

## Personnaliser les Couleurs de Base

### Couleurs disponibles

- **primary** : Couleur primaire (boutons, liens, accents)
- **secondary** : Couleur secondaire (accents complémentaires)
- **error** : Couleur d'erreur
- **warning** : Couleur d'avertissement
- **info** : Couleur d'information
- **success** : Couleur de succès

## Variantes de Couleur

Pour chaque couleur, vous pouvez définir :

- **main** : La couleur principale (obligatoire)
- **light** : Variante claire
- **dark** : Variante foncée
- **contrastText** : Couleur du texte pour le contraste

Si `light` et `dark` ne sont pas définis, Material UI les calcule automatiquement.

```javascript
const theme = createTheme({
  palette: {
    primary: {
      light: '#757ce8',
      main: '#3f50b5',
      dark: '#002884',
      contrastText: '#fff',
    },
  },
});
```

## Seuil de Contraste (contrastThreshold)

Contrôle comment Material UI décide si le texte doit être clair ou foncé sur un fond.

```javascript
const theme = createTheme({
  palette: {
    contrastThreshold: 4.5, // Pour respecter WCAG AA ; par defaut 3
  },
});
```

## Décalage Tonal (tonalOffset)

Modifie la luminance des variantes `light` et `dark` à partir de `main`.

- **Défaut** : `0.2` (déplace la luminance d'environ 2 indices)
- **Plus élevé** : `0.5` (différence plus marquée)
- **Asymétrique** : `{ light: 0.1, dark: 0.9 }`

```javascript
// 
const theme = createTheme({
  palette: {
    primary: { main: blue[500] },               // Décalage par défaut light: blue[300], dark: blue[700]
    tonalOffset: 0.5,                           // Décalage par défaut 0.2
    //tonalOffset: { light: 0.1, dark: 0.9 },   // Décalage asymétrique
  },
});
```

## Thèmes Clair et Sombre

### Créer les deux schémas

```javascript
const theme = createTheme({
  colorSchemes: {
    light: true,
    dark: true,
  },
});
```

### Personnaliser chaque schéma

```javascript
const theme = createTheme({
  colorSchemes: {
    light: {
      palette: {
        primary: { main: '#3f50b5' },
        background: { default: '#fff' },
      },
    },
    dark: {
      palette: {
        primary: { main: '#90caf9' },
        background: { default: '#121212' },
      },
    },
  },
});
```

**Note** : `colorSchemes` est préféré à partir de Material UI v6. S'il est fourni avec `palette`, `colorSchemes` prévaut.

## Ajouter une Couleur Personnalisée

Étape 1 : Créer le thème

```javascript
import { createTheme } from '@mui/material/styles';

let theme = createTheme({
  palette: {
    primary: { main: '#3f50b5' },
  },
});

// Ajouter une couleur personnalisée avec augmentColor
theme = createTheme(theme, {
  palette: {
    salmon: theme.palette.augmentColor({
      color: { main: '#FF5733' },
      name: 'salmon',
    }),
  },
});
```

Étape 2 : TypeScript - Augmentation de module

```typescript
declare module '@mui/material/styles' {
  interface Palette {
    salmon: Palette['primary'];
  }

  interface PaletteOptions {
    salmon?: PaletteOptions['primary'];
  }
}

declare module '@mui/material/Button' {
  interface ButtonPropsColorOverrides {
    salmon: true;
  }
}
```
