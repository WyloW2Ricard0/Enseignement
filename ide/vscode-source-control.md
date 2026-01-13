---
versions: 1.0.0
effectiveDate: 2025-12-16
author: RICHARD Wilfried

title: Contrôle de code source dans VS Code
intro: Guide pratique pour utiliser Git et le contrôle de version dans Visual Studio Code.
type: guide
topics:
  - vscode
  - git
  - contrôle de version
  - branches
  - github
image: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/langfr-250px-Visual_Studio_Code_1.35_icon.svg.png"
---

# Contrôle de code source dans VS Code

VS Code intègre la gestion Git pour le contrôle de version : vous pouvez effectuer toutes les opérations courantes (mise en scène, commit, création de branches, résolution de conflits) directement dans l’éditeur, sans passer par le terminal.

## Prérequis
- Installez Git (version 2.0.0 ou ultérieure) sur votre machine.
- Configurez votre nom et e-mail :
	```bash
	git config --global user.name "Votre Nom"
	git config --global user.email "votre.email@exemple.com"
	```

## Démarrer avec un dépôt
- Ouvrez un dossier existant
- initialisez un nouveau dépôt Git.
- Pour cloner un dépôt : utilisez la commande « Cloner un dépôt » dans l’interface ou le terminal.

## Fonctions principales dans VS Code
- Vue Contrôle de version : mettez en scène, validez, gérez les modifications.
- Éditeur de diff : comparez les versions de fichiers côte à côte.
- Graphique de branches : visualisez l’historique des commits et des branches.
- Indicateurs de modification dans la marge de l’éditeur.

## Flux de travail
1. Modifiez vos fichiers.
2. Examinez les changements dans la vue Contrôle de version.
3. Mettez en scène les fichiers (+).
4. Saisissez un message de commit et validez.
5. Synchronisez avec le dépôt distant (push/pull).

## Résolution de conflits
VS Code met en évidence les fichiers en conflit. Utilisez l’éditeur pour choisir les modifications à conserver ou l’éditeur de fusion à trois voies pour une vue détaillée.

## Branches et réserves
- Changez de branche rapidement.
- Utilisez les arbres de travail pour travailler sur plusieurs branches.
- Utilisez le stash pour sauvegarder temporairement des modifications non validées.

## Historique
- Visualisez l’historique des commits et la timeline d’un fichier.

## Intégration GitHub
- Gérez les pull requests et issues avec l’extension GitHub Pull Requests and Issues.

## Autres systèmes
- Installez des extensions pour Azure DevOps, SVN, Mercurial, etc.

---
*Pour plus d’informations, consultez la documentation officielle de VS Code et de Git.*