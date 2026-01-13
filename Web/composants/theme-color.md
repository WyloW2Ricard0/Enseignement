---
title: Roles de couleur Material Design
intro: Guide des 26 roles de couleur standard pour une interface accessible
---

# Roles de couleur Material Design

Il y a 26 roles de couleur standard organises en 6 groupes : **primary**, **secondary**, **tertiary**, **error**, **surface** et **outline**.

## Qu'est-ce que les roles de couleur ?

Les **roles de couleur** definissent où et comment appliquer les couleurs dans votre interface. Ils assurent :
- L'**accessibilite** (contraste minimum 3:1)
- La **coherence** visuelle
- La **flexibilite** entre thèmes clairs/sombres

## Concepts generaux

1. Roles d'accentuation pour elements au premier plan
    - **Primary**: Utilisez pour les elements les plus importants : FAB, boutons haute-emphase, etats actifs.
    - **Secondary**: Utilisez pour les elements moins importants : filtres, chips.
    - **Tertiary**: Utilisez pour les contrastes equilibres : champs d'entree, badges.
    - **Surface**: Couleur de fond et zones basse-emphase
    - Error
    - Warning
    - Info
    - Success
    - Divider
- **Container**: Couleur de remplissage des elements (boutons, cartes). Ne pas utiliser pour texte/icones
- **On**: Couleur du texte ou icones sur la couleur parente (ex : on primary = texte sur primary)
- **Variant**: Version moins emphasisee (ex : outline variant = outline moins visible); low, medium, high
- **Outline**: Utilisez pour les bordures et dividers.

## Bonnes pratiques

✅ **À faire** :
- Utiliser les paires de couleurs prevues pour maintenir l'accessibilite
- Appliquer les mêmes roles dans tous les window sizes
- Maintenir la coherence entre thèmes clair et sombre
- Utiliser `on surface` et `on surface variant` sur tous les types de surfaces

❌ **À eviter** :
- Combiner les couleurs de manière incorrecte
- Utiliser outline pour les dividers (utiliser outline variant)
- Utiliser outline pour les cartes complexes
- Forcer des couleurs fixed où le contraste est necessaire

## Resume des paires recommandees

| Composant | Roles | Utilisation |
|-----------|-------|------------|
| Bouton filled | primary + on primary | Bouton d'action primaire |
| Bouton tonal | secondary container + on secondary container | Bouton secondaire |
| Champ texte | tertiary container + outline | Champ de saisie |
| Card | surface container + on surface | Contenu niche |
| FAB | primary container + on primary container | Bouton flottant |
| Snackbar | inverse surface + inverse on surface + inverse primary | Message de notification |
| Divider | outline variant | Separateur |
| Navigation | surface container | Barre de navigation |
