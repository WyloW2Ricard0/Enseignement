---
versions: 1.0.0
effectiveDate: 2025-12-11
author: RICHARD Wilfried

title: Introduction à la gestion de version et Git
excerpt: Comprendre les bases des systèmes de gestion de version (VCS) et l’intérêt de Git.
type: introduction
topics:
  - git
  - versioning
  - vcs
  - introduction
image: "https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png"
---

# Gith

## Objectif

La gestion de version (VCS) enregistre l'évolution des fichiers afin de pouvoir revenir à n'importe quelle version, suivre qui a fait quelles modifications, et récupérer un état stable en cas d'erreur ou de perte de fichiers.

## Pourquoi l'utiliser

Permet de restaurer des versions antérieures, visualiser l'historique des changements, identifier l'auteur d'un changement problématique, et faciliter la collaboration sans risque de perte irréversible.

## Types de VCS :

### Locaux

Sauvegardes manuelles ou outils simples (ex. RCS). Faciles à mettre en place mais fragiles — risque d'oubli ou d'écrasement, et stockage centralisé local susceptible de perte.

### Centralisés (CVCS)
Un serveur central (ex. CVS, Subversion) contient l'historique ; les clients récupèrent les fichiers depuis ce serveur. Avantage : administration et permissions centralisées. Inconvénient majeur : point unique de panne et risque de perte si le serveur est corrompu sans sauvegarde.

### Distribués (DVCS)
Chaque client clone entièrement le dépôt (ex. Git, Mercurial). Avantage : résilience — toute copie peut restaurer le dépôt central, et chaque extraction sert de sauvegarde complète.

## Glossaire

### Branch

## Conclusion

il combine historique complet, meilleure collaboration et tolérance aux pannes.

### Ressources

- Lisez la documentation officielle : https://git-scm.com/doc
- Environnement graphique : GitHub Desktop, Sourcetree, GitKraken, ou intégration IDE (VS Code).