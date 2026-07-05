---
# Variable
showMiniToc: true
permissions: true
effectiveDate: 2026-01-13
image: "https://www.w3.org/Icons/w3c_home"

# Content pour faciliter la recherche
title: Recommandations W3C (WCAG)
intro: Résumé des principes et exigences d’accessibilité du W3C (WCAG 2.1)
type: standard
topics:
    - accessibilite
    - w3c
    - wcag

# Information
author: RICHARD Wilfried
featuredLinks:
    - prev:
    - next:
    - mid:
    - exp:
    - ofi: https://www.w3.org/WAI/standards-guidelines/wcag/
changelog:
    - 2026-01-13 : Ajout du frontmatter YAML standardisé
---


# Recommandations W3C

## Vue d'ensemble

Les Web Content Accessibility Guidelines (WCAG) 2.1 couvrent un large éventail de recommandations pour rendre le contenu web plus accessible. Ces directives visent à rendre le contenu accessible à un plus large éventail de personnes en situation de handicap, notamment :

- Cécité et malvoyance
- Surdité et perte auditive
- Mobilité limitée
- Troubles de la parole
- Photosensibilité
- Combinaisons de ces handicaps
- Apprentissage et limitations cognitives

## Les 4 Principes Fondamentaux

1. **Perceptible** : L'information et les composants doivent être présentables de manière perceptible
2. **Utilisable** : Les composants d'interface doivent être utilisables
3. **Compréhensible** : L'information et l'utilisation doivent être compréhensibles
4. **Robuste** : Le contenu doit être compatible avec les technologies d'assistance actuelles et futures

## Les 3 Niveaux de Conformité

- **Niveau A** : Niveau minimum de conformité
- **Niveau AA** : Niveau intermédiaire (recommandé)
- **Niveau AAA** : Niveau maximal de conformité

### Exigences de Ratio de Contraste

le nivau n'indique pas explicetement le ratio

1. Texte Normal : **Niveau AAA**; ratio minimum de **7:1**
1. Texte Large (en gras) : **Niveau AAA** ; ratio minimum de **9:2**
1. Composants UI : **Niveau AA** (pas de AAA definie); ratio minimum de **3:1**

#### Calcul du Ratio de Contraste

$$\text{ratio} = \frac{L_l + 0.05}{L_d + 0.05}$$

- $L_l$ = luminance relative de la couleur la plus claire (entre 0 et 1)
- $L_d$ = luminance relative de la couleur la plus foncée (entre 0 et 1)


Calculer la luminance relative :

$$L = 0.2126 \times R_{linear} + 0.7152 \times G_{linear} + 0.0722 \times B_{linear}$$

Les coefficients proviennent de la norme **ITU-R BT.709** (télévision HD) et sont basés sur la **sensibilité de l'œil humain** aux différentes longueurs d'onde ; $0.2126 + 0.7152 + 0.0722 = 1.0000$ (normalisation)

## Domaines Clés d'Accessibilité

### 1. Perceptible

1. Alternatives Textuelles
    - Fournir des alternatives textuelles pour tout contenu non textuel
    - Descriptions pour les images, graphiques, vidéos
1. Médias Temporels
    - Sous-titres pour les vidéos préenregistrées
    - Descriptions audio pour les vidéos
    - Transcriptions pour les contenus audio
    - Prise en charge du langage des signes
1. Adaptabilité
    - Information et relations marquées correctement
    - Séquence de lecture logique
    - Instructions sans dépendre uniquement de la couleur
    - Orientation de l'écran (portrait/paysage) supportée
1. Distinguabilité
    - Contraste suffisant entre le texte et l'arrière-plan (4.5:1 minimum pour AA)
    - Capacité à redimensionner le texte sans perte de contenu
    - Pas de vidéos avec flashs qui pourraient causer des crises

### 2. Utilisable

1. Accessibilité au Clavier
    - Toutes les fonctionnalités accessibles au clavier
    - Pas de pièges au clavier
1. Temps Suffisant
    - Donner assez de temps aux utilisateurs pour lire et utiliser le contenu
    - Pas de contenu qui flashe à une fréquence dangereuse
1. Convulsions et Réactions Physiques
    - Éviter le contenu qui flashe plus de 3 fois par seconde
1. Navigabilité
    - Objectif du lien clair
    - Titres et étiquettes explicites
    - Structure logique de la page
1. Modalités d'Entrée
    - Gestes alternatifs pour les commandes tactiles
    - Étiquettes visibles pour les champs
    - Taille suffisante des cibles tactiles

### 3. Compréhensible

1. Lisibilité
    - Langue de la page spécifiée
    - Mots inhabituels et acronymes définis
    - Mécanismes pour identifier les prononciations ambiguës
1. Prévisibilité
    - Navigation cohérente
    - Identification cohérente des composants
1. Assistance à la Saisie
    - Messages d'erreur clairs
    - Suggestions de correction
    - Prévention des erreurs

### 4. Robustesse

- Code HTML valide
- Noms, rôles et valeurs pour tous les composants
- Support maximal des technologies d'assistance

## Ressources Complémentaires

- [How to Meet WCAG 2.1](https://www.w3.org/WAI/WCAG22/quickref/) : Guide pratique personnalisable
- [Understanding WCAG 2.1](https://www.w3.org/WAI/WCAG22/Understanding/) : Guide complet de compréhension et d'implémentation
- [Techniques for WCAG 2.1](https://www.w3.org/WAI/WCAG22/Techniques/) : Collection de techniques et de cas d'échec
