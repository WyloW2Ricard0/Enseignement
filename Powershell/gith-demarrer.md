---
versions: 1.0.0
effectiveDate: 2025-12-12
author: RICHARD Wilfried

title: Bien démarrer avec Git
excerpt: Guide pratique pour installer, configurer et utiliser Git efficacement dès le début.
type: guide
topics:
  - git
  - versioning
  - powershell
  - workflow
  - tutoriel
image: "https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png"
---
# Bien démarrer avec Git

Ce document présente l'essentiel pour commencer avec Git : installation, configuration, commandes de base, bonnes pratiques et dépannage rapide.

## Prérequis
- Git installé (Windows, macOS, Linux).
- Accès à un service distant si vous souhaitez pousser (`GitHub`, `GitLab`, `Bitbucket`, etc.).
- Pour Windows : utiliser PowerShell pour les exemples fournis.

## Variables d'environnement (exemple)

```powershell
$PROJET_NAME="Enseignement"
$PROJET_PATH="F:\Enseignement"

$GIT_REPO_URL="https://github.com/WyloW2Ricard0/Enseignement.git"
$GIT_REMOTE_DEFAULT="origin"
$GIT_BRANCH_DEFAULT="master"
```

## Installation (Windows)
Téléchargez l'installateur depuis https://git-scm.com/ ou installez via `winget` si disponible.

```powershell
# Vérification de l'installation
!git --version
```

## Configuration initiale
Définissez votre identité et quelques réglages utiles :

```powershell
# Lier vos commits à votre compte distant
!git config --global user.name $GIT_USER_NAME
!git config --global user.email $GIT_USER_EMAIL

# Editeur par défaut
!git config --global core.editor $GIT_EDITOR_VSCODE

# Gère OAuth, tokens et prompts sécurisés
!git config --global credential.helper manager-core

# Vérification de la configuration
!git config --global --list
```
Remarque : vous pouvez enlever `--global` pour changer que les paramètres local.

## Cloner un dépôt distant

### Qu'est-ce qu'un dépôt bare (.git) ?
Un dépôt **bare** (nu) est un dépôt Git sans répertoire de travail. Il contient uniquement l'historique Git (le contenu du dossier `.git`).

**Différences :**
- **Dépôt normal** : `Enseignement/` contient vos fichiers + `.git/` (historique caché)
- **Dépôt bare** : `Enseignement.git/` contient UNIQUEMENT l'historique Git

**Utilisations principales :**
- **Serveurs Git** : Les dépôts sur GitHub/GitLab sont des dépôts bare
- **Dépôt central** : Pour partager entre plusieurs développeurs
- **Backup** : Sauvegarde complète de l'historique sans fichiers de travail
- **Mirror** : Créer un miroir d'un dépôt distant

**Pourquoi "bare" ?**
- Pas de fichiers de travail (on ne peut pas modifier directement)
- Plus léger (pas de duplication des fichiers)
- Évite les conflits (personne ne travaille directement dedans)
- Fait pour recevoir des `push` (contrairement aux dépôts normaux)

```powershell
# Créer un dépôt bare (pour serveur/backup)
git clone --bare $GIT_REPO_URL Enseignement.git

# Cloner depuis un dépôt bare local
git clone $GIT_REPO_URL $PROJET_NAME

# Pousser vers un dépôt bare local
git remote add backup E:/Backup/Enseignement.git
git push backup master
```

## Créer un dépôt local (exemple minimal)

```powershell
# Initialisation d'un dépôt Git local
git init $PATH_PROJET

# Création d'un fichier README.md
echo "# " + $NOM_PROJET > README.md
git add README.md
git commit -m "Initial commit"
```

Si vous voyez `fatal: detected dubious ownership in repository`

```powershell
# chemin du projet à ajouter aux répertoires sûrs
git config --global safe.directory $PATH_PROJET
# Suprimer une règle de répertoire sûr
git config --global --unset safe.directory $PATH_PROJET
```

Pour connecter un dépôt Git local à un dépôt distant et le mettre à jour avec le contenu du dépôt distant :

```powershell
# Ajouter le dépôt distant
git remote add $GIT_REMOTE_DEFAULT $GIT_REPO_URL

# Récupérer les branches et l’historique du dépôt distant
git fetch $GIT_REMOTE_DEFAULT

# Créer et basculer sur la branche principale du dépôt distant (ex : master ou main)
git checkout -b $GIT_BRANCH_DEFAULT
```

## Remote (dépôt distant)

Un **remote** est une version du dépôt hébergée sur un serveur (ex. GitHub, GitLab) accessible via le réseau.
Il permet de synchroniser les modifications entre plusieurs utilisateurs ou machines.

**Quand utiliser une remote :**

- Partager le code avec d'autres développeurs
- Sauvegarder votre travail sur un serveur externe
- Collaborer sur un même dépôt depuis plusieurs machines
- Synchroniser les branches entre équipiers
- Le nom par défaut habituel est *origin*, mais on peut ajouter plusieurs remotes (ex. *upstream* pour un fork).

```powershell
# Ajouter un dépôt distant
git remote add $GIT_REMOTE_DEFAULT $GIT_REPO_URL

# Modifier un dépôt distant
git remote set-url $GIT_REMOTE_DEFAULT $GIT_REPO_URL

# Vérifier le dépôt distant
git remote -v
```

## Enregistrer dans les Commit

```powershell
# Vérifier l'état du dépôt
git status
```

mettre à jour ta branche locale avec les changements du dépôt distant.
```powershell
# Récupérer les modifications depuis le dépôt distant
git pull $REMOTE_DEFAUT $GIT_BRANCH_DEFAULT
```

On ajoute des modifications grâce à l'**index** (zone de mise en scène).
L'index capture une "photo" des fichiers que vous préparez à enregistrer avant le commit.

Un commit est un snapshot de votre projet à un moment donné — il enregistre l'état des fichiers indexés avec un message explicite et des métadonnées (auteur, date, hash unique).

Commits petits et fréquents avec messages clairs.
- **Première ligne** : résumé court (50 caractères max) en impératif présent
- **Corps** (optionnel) : explique le *pourquoi* plutôt que le *comment*, séparé par une ligne vide
- **Références** : mentionnez les issues ou tickets si pertinent

```powershell
# Ajouter les modifications
git add .

# Enregistrer les modifications
git commit

# Envoyer les modifications locales vers le dépôt distant
git push $GIT_REMOTE_DEFAUT $GIT_BRANCH_DEFAULT
```

## Push refusé
Si le dépôt distant contient des modifications qui ne figurent pas dans votre branche locale.

### Dépôt sans .git
```powershell
# Étape 1 : Initialiser Git dans le dépôt local
git init
# Étape 2 : Ajouter le dépôt distant
git remote add origin $GIT_REPO_URL
# Étape 3 : Récupérer les informations du dépôt distant
git fetch origin
# Étape 4 : Créer et basculer sur la branche master
git checkout -b master origin/master
# Étape 5 : Ajouter vos modifications locales
git add .
# Étape 6 : Commiter les modifications
git commit -m "Synchronisation avec le dépôt distant"
# Étape 7 : Pousser vers le dépôt distant
git push origin master
```

### Git différent
```powershell
!git log  --oneline --graph -5 --decorate
# voir les modifications sans les fusionner
!git fetch
!git diff
```
vous devez effectuer un pull avec rebase pour intégrer les modifications distantes
```powershell
# Ecraser les modifications locales avec celles du dépôt distant
git pull --rebase origin master
# OU fusionner les modifications
!git merge
# Pousser les modifications locales vers le dépôt distant
git push origin master
# Annuler le dernier commit (local)
!git reset --soft HEAD~1
```

## Branches (travail isolé)
Une **branche** est une ligne de développement indépendante permettant de travailler en parallèle sans affecter la branche principale (*main* ou *master*). 
Chaque branche pointe vers un commit spécifique et peut évoluer indépendamment.

**Quand créer une branche :**
- Développer une nouvelle fonctionnalité
- Corriger un bug sans impacter le code stable
- Expérimenter sans risque
- Travailler en équipe sur des tâches différentes

```powershell
# Voir toutes les branches locales et distantes
git branch -a
!git switch $BRANCHE_NOUVELLE
!git switch -c $BRANCHE_NOUVELLE $REMOTE_DEFAUT/$BRANCHE_PRINCIPALE
!git branch $BRANCHE_NOUVELLE ef21b07
git restore README.md
```
