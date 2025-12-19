---
versions: 0.1.0
effectiveDate: 2025-12-20
author: RICHARD Wilfried

title: Prioriser les composants MUI
excerpt: Guide pour choisir et organiser les composants principaux de Material-UI pour une architecture uniforme.
type: guide
topics:
  - mui
  - react
  - composants
  - architecture
image: "https://mui.com/static/logo.png"
---

# Choisir le bonne interface

prioriser les composant pour une architecture plus uniforme

## Disposition

Le composant « layout », il définit la structure globale avant d’ajouter les éléments de détail.

1. **Conteneur :** Sert de cadre principal, limite la largeur et centre le contenu. Il structure la page.
1. **Stack :** Organise les éléments enfants en pile verticale ou horizontale, gère l’espacement entre eux.
1. **Grille :** Permet un positionnement précis et réactif des éléments sur plusieurs colonnes/lignes
1. **Boite :** Élément de base pour appliquer des groupes

## Surface

Ces le suport d'apparence, que l'on choisi.

optionel si vous avez simplement besoin d’un contenant générique, vous pourriez préférer utiliser les composants Boîte ou Conteneur.

1. **Paper :** Dans la conception des matériaux, les composants de surface et les styles d’ombre sont fortement influencés par leurs équivalents physiques réels.
1. **Card :** Les cartes sont des surfaces qui affichent le contenu et les actions sur un même sujet.
1. **Accordion :** permet aux utilisateurs d’afficher et de masquer des sections de contenu connexe sur une page.
1. **App Bar :** La barre d’applications supérieure affiche du contenu et des actions liés à l’écran actuel. Il sert à l’image de marque, aux titres d’écran, à la navigation et aux actions.

### Card

1. **CardActionArea :** Contenair de la carte
1. **CardActions :** boite pour action 
1. **CardContent :** boite pour text de card
1. **CardHeader :**
1. **CardMedia :** boite pour image