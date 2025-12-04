# Gith

## Objectif

La gestion de version (VCS) enregistre l'évolution des fichiers afin de pouvoir revenir à n'importe quelle version, suivre qui a fait quelles modifications, et récupérer un état stable en cas d'erreur ou de perte de fichiers.

## Pourquoi l'utiliser

Permet de restaurer des versions antérieures, visualiser l'historique des changements, identifier l'auteur d'un changement problématique, et faciliter la collaboration sans risque de perte irréversible.

## Glossaire

### Commit
Un commit est un snapshot de votre projet à un moment donné — il enregistre l'état des fichiers indexés avec un message explicite et des métadonnées (auteur, date, hash unique).

## Staging Area

L'index est la zone intermédiaire entre votre répertoire de travail (les fichiers que vous modifiez) et votre dépôt Git (l'historique enregistré).
L'index capture ainsi une "photo" des fichiers que vous préparez à enregistrer avant le commit — c'est pourquoi on l'appelle zone de mise en scène en anglais.

## Types de VCS :

### Locaux

Sauvegardes manuelles ou outils simples (ex. RCS). Faciles à mettre en place mais fragiles — risque d'oubli ou d'écrasement, et stockage centralisé local susceptible de perte.

### Centralisés (CVCS)
Un serveur central (ex. CVS, Subversion) contient l'historique ; les clients récupèrent les fichiers depuis ce serveur. Avantage : administration et permissions centralisées. Inconvénient majeur : point unique de panne et risque de perte si le serveur est corrompu sans sauvegarde.

### Distribués (DVCS)
Chaque client clone entièrement le dépôt (ex. Git, Mercurial). Avantage : résilience — toute copie peut restaurer le dépôt central, et chaque extraction sert de sauvegarde complète.

## Conclusion

il combine historique complet, meilleure collaboration et tolérance aux pannes.
