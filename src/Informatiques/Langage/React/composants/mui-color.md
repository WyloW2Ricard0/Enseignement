---
# Variable
showMiniToc: true
permissions: true
effectiveDate: 2026-01-04
image: "https://tommisaltiola.gallerycdn.vsassets.io/extensions/tommisaltiola/autofold-md-frontmatter/1.0.5/1710533937767/Microsoft.VisualStudio.Services.Icons.Default"

# Content pour faciliter la recherche
title: Système de Couleurs Material UI - Guide Complet
intro: Découvrez comment utiliser et personnaliser le système de couleurs Material Design pour créer des interfaces cohérentes et accessibles
type: Composants UI
topics:
  - Material UI
  - Couleurs
  - Accessibilité

# Information
author: RICHARD Wilfried
changelog:
  - 2026-01-04 : Création du guide concis en français sur les couleurs Material UI
---

# Système de Couleurs Material UI

## Vue d'ensemble

Le système de couleurs de Material Design permet de créer un thème de couleurs qui reflète votre marque ou style.

## Choisir les couleurs

### Outil officiel

Material Design propose un outil de configuration de palettes : [material.io/resources/color/](https://material.io/resources/color/). Cet outil vous aide à créer une palette de couleurs et à mesurer le niveau d'accessibilité.

### Utiliser createTheme()

```javascript
import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      light: '#757ce8',
      main: '#3f50b5',
      dark: '#002884',
      contrastText: '#fff',
    },
    secondary: {
      light: '#ff7961',
      main: '#f44336',
      dark: '#ba000d',
      contrastText: '#000',
    },
  },
});
```

### Accéder au thème

#### Aplication du theme

Vous pouvez imbriquer plusieurs `ThemeProvider` pour appliquer des thèmes différents à différentes parties de votre application.

```javascript
function App() {
  return <ThemeProvider theme={theme}>...</ThemeProvider>;
}
```

#### dans un composant

```javascript
import { useTheme } from '@mui/material/styles';

function MonComposant() {
  const theme = useTheme();
  return <span>{theme.spacing}</span>;
}
```

## Palettes de couleurs

### Termes importants

- **Palette** : Collection de couleurs harmonieuses conçues pour fonctionner ensemble
- **Teinte** : La couleur elle-même (rouge, rose, bleu, etc.)
- **Nuance** : La variation de la couleur (50, 500, 900, etc.)
  - 50 : nuance la plus claire
  - 900 : nuance la plus foncée
  - A100, A200, A400, A700 : nuances d'accent

Le générateur de palette de matériaux peut être utilisé pour générer une palette pour n’importe quelle couleur que vous saisis : https://m2.material.io/inline-tools/color/

### Importer des couleurs

```javascript
import { red, purple } from '@mui/material/colors';

const primary = red[500];      // #f44336
const accent = purple['A200'];  // #e040fb
const accent = purple.A200;     // alternative
```

### Couleurs disponibles

red, pink, purple, deepPurple, indigo, blue, lightBlue, cyan, teal, green, lightGreen, lime, yellow, amber, orange, deepOrange, brown, grey, blueGrey

Chaque couleur dispose de nuances : 50, 100, 200, 300, 400, 500, 600, 700, 800, 900 et les accents A100, A200, A400, A700.

## Accessibilité

La [norme WCAG 2.1](https://www.w3.org/TR/WCAG21/) recommande un ratio de contraste minimum de **4.5:1** pour le texte. Material UI applique actuellement un ratio minimum de **3:1**. Pour une meilleure accessibilité, augmentez le ratio de contraste dans la configuration du thème.
