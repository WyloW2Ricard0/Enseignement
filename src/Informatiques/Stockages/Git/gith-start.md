---
effectiveDate: 2026-01-01
author: RICHARD Wilfried

title: Bien demarrer avec Git
intro: Guide pratique pour installer, configurer et utiliser Git efficacement dès le debut.
topics:
  - git
  - versioning
  - powershell
  - workflow
image: "https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png"
---
# Bien demarrer avec Git

Ce document presente l'essentiel pour commencer avec Git : installation, configuration, commandes de base, bonnes pratiques et depannage rapide.

## Prerequis
- Git installe (Windows, macOS, Linux).
- Accès a un service distant si vous souhaitez pousser (`GitHub`, `GitLab`, `Bitbucket`, etc.).
- Pour Windows : utiliser PowerShell pour les exemples fournis.

## Installation (Windows)

Telechargez l'installateur depuis https://git-scm.com/ ou installez via `winget` si disponible.

```powershell
# Verification de l'installation
!git --version
```

## Configuration initiale

Definissez votre identite et quelques reglages utiles :

```powershell
$GIT_USER_NAME="WyloW2Ricar0"
$GIT_USER_EMAIL="wrichard@live.fr"
$GIT_EDITOR_VSCODE=""

# Lier vos commits a votre compte distant
git config --global user.name $GIT_USER_NAME
git config --global user.email $GIT_USER_EMAIL

# Editeur par defaut
git config --global core.editor $GIT_EDITOR_VSCODE

# Gère OAuth, tokens et prompts securises
git config --global credential.helper manager-core

# Verification de la configuration
git config --global --list
```

Remarque : vous pouvez enlever `--global` pour ne changer que les paramètres locaux.

## Cloner un depot distant

### Qu'est-ce qu'un depot bare (.git) ?

Un depot **bare** (nu) est un depot Git sans repertoire de travail. Il contient uniquement l'historique Git (le contenu du dossier `.git`).

**Differences :**

- **Depot normal** : `Enseignement/` contient vos fichiers + `.git/` (historique cache)
- **Depot bare** : `Enseignement.git/` contient UNIQUEMENT l'historique Git

**Utilisations principales :**

- **Serveurs Git** : Les depots sur GitHub/GitLab sont des depots bare
- **Depot central** : Pour partager entre plusieurs developpeurs
- **Backup** : Sauvegarde complète de l'historique sans fichiers de travail
- **Mirror** : Creer un miroir d'un depot distant

**Pourquoi "bare" ?**

- Pas de fichiers de travail (Télécharge UNIQUEMENT le .git/)
- Plus leger (pas de duplication des fichiers)
- evite les conflits (personne ne travaille directement dedans)
- Fait pour recevoir des `push` (contrairement aux depots normaux)

```powershell
$GIT_REPO_URL="https://github.com/WyloW2Ricard0/Enseignement.git"
$PROJET_NAME="Enseignement"

# Cloner depuis un depot bare en local (dossier separé)
git clone $GIT_REPO_URL $PROJET_NAME
```

## Creer un depot local (exemple minimal)

```powershell
$PROJET_PATH="F:Enseignement"
$PROJET_NAME="Enseignement"

# Initialisation d'un depot Git local
git init $PROJET_PATH

# Creation d'un fichier README.md
echo "# " + $NOM_PROJET > README.md
git add README.md
git commit -m "Initial commit"
```

Si vous voyez `fatal: detected dubious ownership in repository`

```powershell
# chemin du projet a ajouter aux repertoires sûrs
git config --global safe.directory $PATH_PROJET

# Suprimer une règle de repertoire sûr
git config --global --unset safe.directory $PATH_PROJET
```

**Connecter un depot local a un distant**
le nom du wokspace doit necessairement avoir le meme nom que le repo pour ne pas ajouter de fichier inutil dan le comite

```powershell
$GIT_REPO_URL="https://github.com/WyloW2Ricard0/Enseignement.git"
$GIT_REMOTE_DEFAULT="origin"

# Initialiser le git
git init

# Ajouter le depot distant
git remote add $GIT_REMOTE_DEFAULT $GIT_REPO_URL

# Recuperer l'historique du depot distant (ne pas fusionner)
git fetch $GIT_REMOTE_DEFAULT
```

```powershell
# Basculer sur la branche principale du depot distant
$GIT_BRANCH_DEFAULT="main"
git switch -c $GIT_BRANCH_DEFAULT $GIT_REMOTE_DEFAULT/$GIT_BRANCH_DEFAULT

# Extraire les fichiers du dépot bare
#git reset --hard $GIT_REMOTE_DEFAULT/$GIT_BRANCH_DEFAULT

#git pull $GIT_REMOTE_DEFAULT $GIT_BRANCH_DEFAULT
```

## Remote (depot distant)

Un **remote** est une version du depot hebergee sur un serveur (ex. GitHub, GitLab) accessible via le reseau.
Il permet de synchroniser les modifications entre plusieurs utilisateurs ou machines.

**Quand utiliser une remote :**

- Partager le code avec d'autres developpeurs
- Sauvegarder votre travail sur un serveur externe
- Collaborer sur un même depot depuis plusieurs machines
- Synchroniser les branches entre equipiers
- Le nom par defaut habituel est *origin*, mais on peut ajouter plusieurs remotes (ex. *upstream* pour un fork).

```powershell
$GIT_REPO_URL="https://github.com/WyloW2Ricard0/Enseignement.git"
$GIT_REMOTE_DEFAULT="origin"

# Ajouter un depot distant
git remote add $GIT_REMOTE_DEFAULT $GIT_REPO_URL

# Modifier un depot distant
git remote set-url $GIT_REMOTE_DEFAULT $GIT_REPO_URL

# Verifier le depot distant
git remote -v
```

## Branches (travail isole)

Une **branche** est une ligne de developpement independante permettant de travailler en parallèle sans affecter la branche principale (*main* ou *master*).
Chaque branche pointe vers un commit specifique et peut evoluer independamment.

**Quand creer une branche :**

- Developper une nouvelle fonctionnalite
- Corriger un bug sans impacter le code stable
- Experimenter sans risque
- Travailler en equipe sur des tâches differentes

### Changer de branch

```shell
# Voir toutes les branches locales et distantes
git branch -a
# Entre le nom soiter
$BRANCHE_NAME='main'
# Changer de branch
git switch $BRANCHE_NAME
```

### Suprimer une branche

(Attention on ne peut cier la branche sur lequel on est)

```shell
# Voir toutes les branches locales et distantes
git branch -a
# Entre le nom soiter
$REMOTE_NAME='origin'
$BRANCHE_NAME='main'
# Changer de branch
git branch -d remotes/$REMOTE_NAME/$BRANCHE_NAME
```

```sh
!git switch -c $BRANCHE_NOUVELLE $REMOTE_DEFAUT/$BRANCHE_PRINCIPALE
!git branch $BRANCHE_NOUVELLE ef21b07
git restore README.md
```

---
*[Apprendre a enregitre ces commit ici](gith-commit.md)*
