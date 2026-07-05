# chroma.js - Guide Essentiel

[chroma.js](https://gka.github.io/chroma.js/) est une bibliothèque JavaScript légère (13.5kB) pour les conversions de couleurs et les échelles chromatiques.

## Installation

```bash
npm install chroma-js
```

```javascript
import chroma from 'chroma-js';
```

## Créer une couleur

### Couleur aléatoire

```javascript
chroma.random()                          // Génère une couleur aléatoire
```

### Formats de base

```javascript
chroma('hotpink')              // nom de couleur
chroma('#ff3399')              // hexadécimal
chroma(255, 51, 153)           // RGB (0-255)
chroma([255, 51, 153])         // RGB en tableau
chroma({ h:120, s:1, l:0.75});
```

### Espaces colorimétriques

```javascript
chroma(330, 1, 0.6, 'hsl')     // HSL: teinte(0-360), saturation(0-1), luminosité(0-1)
chroma.hsl(330, 1, 0.6)        // Syntaxe alternative
```

### Formats de sortie

```javascript
chroma('orange').hex()                   // "#ffa500"
chroma('orange').alpha(0.5).hex()        // "#ffa50080" (avec alpha)
chroma('orange').name()                  // "orange"

chroma('teal').css()                     // "rgb(0 128 128)"
chroma('teal').alpha(0.5).css()          // "rgb(0 128 128 / 0.5)"
chroma('teal').css('hsl')                // "hsl(180deg 100% 25.1%)"

chroma('orange').rgb()                   // [255, 165, 0]
chroma('orange').rgba()                  // [255, 165, 0, 1]
chroma('orange').hsl()                   // [38.82, 1, 0.5]
```

## Manipulation des couleurs

### Luminosité

```javascript
chroma('hotpink').darken()              // Assombrir
chroma('hotpink').darken(2)             // Assombrir davantage
chroma('hotpink').brighten()            // Éclaircir
chroma('hotpink').brighten(2)           // Éclaircir davantage

// Définir une luminance spécifique
chroma('hotpink').luminance()            // 0.347
chroma('hotpink').luminance(0.5)         // Ajuste à 50% de luminance
```

### Saturation

```javascript
chroma('slategray').saturate()          // Augmenter la saturation
chroma('slategray').saturate(2)         // Saturer davantage
chroma('hotpink').desaturate()          // Réduire la saturation
chroma('hotpink').desaturate(2)         // Désaturer davantage
```

### Transparence

```javascript
chroma('red').alpha(0.5)                // Définir l'opacité (0-1)
chroma('rgba(255,0,0,0.35)').alpha()    // Obtenir l'opacité: 0.35
```

### Mélange de couleurs

```javascript
chroma('hotpink').shade(0.5)            // Mélange avec du noir
chroma('hotpink').tint(0.5)             // Mélange avec du blanc
```

### Moyenne de couleurs

accepte plus de deux couleurs. Moyenne simple des composantes R, G, B et du canal alpha.chroma.mix

```javascript
colors = ['#ddd', 'yellow', 'red', 'teal']
chroma.average(colors)                   // Moyenne simple
chroma.average(colors, 'lab')            // Moyenne dans l'espace Lab
chroma.average(colors, 'lch', [1,1,2,1]) // Moyenne pondérée
```

## Fonctions utilitaires

### Distance entre couleurs

Calcule la [distance euclidienne](https://en.wikipedia.org/wiki/Euclidean_distance#Three_dimensions) entre deux couleurs dans un espace colorimétrique donné

```javascript
chroma.distance('#fff', '#ff0', 'rgb')   // 255
chroma.distance('#fff', '#ff0', 'hls')   // 96.948
```

### Température de couleur

Estimez la température en Kelvin d’une couleur donnée

```javascript
chroma.temperature(2000)                 // #ff8b14 (lumière de bougie)
chroma.temperature(3500)                 // #ffc38a (coucher de soleil)
chroma.temperature(6500)                 // #fffafe (lumière du jour)
```

## Accessibilité et contraste

Calcule le rapport de contraste WCAG entre deux couleurs. Un contraste minimum de 4,5:1 [est recommandé](http://www.w3.org/TR/WCAG20-TECHS/G18.html) pour garantir que le texte reste lisible sur une couleur de fond.

```javascript
// Ratio de contraste WCAG (minimum 4.5:1 recommandé)
chroma.contrast('pink', 'hotpink')       // 1.721 (trop faible)
chroma.contrast('pink', 'purple')        // 6.124 (suffisant)
```

### Validation

```javascript
chroma.valid('red')            // true
chroma.valid('invalid')        // false
```

## Échelles de couleurs

### Création de base

fonction qui associe des valeurs numériques à une palette de couleurs.

```javascript
// Échelle par défaut (blanc → noir)
f = chroma.scale()
f(0.5)                                   // gris moyen

// Échelle personnalisée
chroma.scale(['yellow', 'red', 'black'])
chroma.scale(['#fafa6e', '#2A4858'])
```

### Configuration du domaine

modifier le domaine d’entrée pour l’adapter à votre cas d’usage spécifique.

```javascript
// Domaine par défaut [0, 1]
chroma.scale(['yellow', 'navy'])

// Domaine personnalisé [0, 100]
chroma.scale(['yellow', 'navy']).domain([0, 100])

// Positionnement précis des couleurs
chroma.scale(['yellow', 'lightgreen', 'navy'])
    .domain([0, 0.25, 1])
```

### Modes d'interpolation

l’interpolation de couleur dépendra du mode de couleur dans lequel les canaux sont interpolés.

```javascript
chroma.scale(['yellow', 'navy']).mode('rgb')    // RGB (par défaut)
chroma.scale(['yellow', 'navy']).mode('hsl')    // HSL
```

### Correction gamma

utilisé pour souligner des valeurs d’intensité basse ou élevée, par défaut=1

utilisée pour « décaler » davantage le centre d’une échelle au début (gamma < 1) ou à la fin (gamma > 1)

```javascript
chroma.scale('YlGn').gamma(0.5)          // Centre vers le début
chroma.scale('YlGn').gamma(1)            // Normal (défaut)
chroma.scale('YlGn').gamma(2)            // Centre vers la fin
```

### Correction de luminosité

répartie uniformément sur une échelle de couleurs.
avec [des gammes de couleurs multi-teintes](https://www.vis4.net/blog/2013/09/mastering-multi-hued-color-scales/),

```javascript
chroma.scale(['black', 'red', 'yellow', 'white'])
    .correctLightness()                  // Répartition uniforme de la luminosité
```

### Obtenir des couleurs

récupérer rapidement des couleurs à distance égale dans une échelle de couleurs.

```javascript
chroma.scale('OrRd').colors(5)           // 5 couleurs équidistantes
// ['#fff7ec', '#fdd49e', '#fc8d59', '#d7301f', '#7f0000']

chroma.scale(['white', 'black']).colors(12)  // 12 couleurs
```

### Classes de couleurs

fonction d’échelle renvoie un ensemble distinct de couleurs au lieu d’un dégradé continu

```javascript
// Échelle continue (par défaut)
chroma.scale('OrRd')

// Classes équidistantes
chroma.scale('OrRd').classes(5)

// Classes personnalisées
chroma.scale('OrRd').classes([0, 0.3, 0.55, 0.85, 1])
```

### Palettes ColorBrewer

chroma.js inclut les palettes [ColorBrewer](https://colorbrewer2.org/#type=sequential&scheme=Purples&n=3) pour la [visualisation de données](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.361.6082&rep=rep1&type=pdf).

```javascript
// Utiliser une palette prédéfinie
chroma.scale('YlGnBu')
chroma.scale('Spectral')
chroma.scale('RdYlBu')

// Accéder aux couleurs directement
chroma.brewer.OrRd
// ['#fff7ec', '#fee8c8', '#fdd49e', '#fdbb84', '#fc8d59', '#ef6548', '#d7301f', '#b30000', '#7f0000']

// Liste des palettes disponibles
Object.keys(chroma.brewer)
// ['OrRd', 'PuBu', 'BuPu', 'Oranges', 'BuGn', 'YlOrBr', 'YlGn', 'Reds', 'RdPu', 'Greens',
//  'YlGnBu', 'Purples', 'GnBu', 'Greys', 'YlOrRd', 'PuRd', 'Blues', 'PuBuGn', 'Viridis',
//  'Spectral', 'RdYlGn', 'RdBu', 'PiYG', 'PRGn', 'RdYlBu', 'BrBG', 'RdGy', 'PuOr',
//  'Set2', 'Accent', 'Set1', 'Set3', 'Dark2', 'Paired', 'Pastel2', 'Pastel1']
```

### Créer un dégradé

```javascript
const gradient = chroma.scale(['#fafa6e', '#2A4858'])
    .mode('hsl')
    .colors(6)
// ['#fafa6e', '#9cdf7c', '#4abd8c', '#00968e', '#106e7c', '#2a4858']
```
