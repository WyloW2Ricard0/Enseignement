# Démarrage rapide — Git

Ce document présente l'essentiel pour commencer avec Git : installation, configuration, commandes de base, bonnes pratiques et dépannage rapide.

## Prérequis

- Avoir Git installé (Windows, macOS, Linux) et un accès à un service distant (GitHub, GitLab, Bitbucket, etc.) si vous voulez pousser vos dépôts.

## Installation (Windows)

- Vérification de l'installation : `git --version`
- Téléchargez depuis https://git-scm.com/.


## Configuration initiale

Exécutez ces commandes en PowerShell pour définir votre identité et quelques réglages utiles : `git config`.

- modifier les valeur par defaut : `. --global`
- Affichez la configuration avec : `. --list`
- Lier vos commits à votre compte distant : `. user.name GIT_COMMITTER_NAME` ou `. user.email GIT_COMMITTER_EMAIL`
- ère OAuth, tokens et prompts sécurisés : `. credential.helper manager-core`

## Créer un dépôt local

```powershell
mkdir mon-projet
cd mon-projet
git init
echo "# Mon projet" > README.md
git add .
git commit -m "Initial commit"
```

## Cloner un dépôt distant

```powershell
git clone https://exemple.com/mon-repo.git
```

## Cycle de travail courant
- Vérifier l'état : `git status`
- Ajouter : `git add <fichier>` ou `git add .`
- Committer : `git commit -m "Message clair"`
- Récupérer et fusionner remote : `git pull` (ou `git pull --rebase`)
- Envoyer : `git push origin <branche>`

## Branches (travail isolé)

```powershell
git checkout -b feature/ma-fonction
# travail...
git add .
git commit -m "Ajoute la fonctionnalité X"
git push -u origin feature/ma-fonction
```

Fusionner sur la branche principale :

```powershell
git checkout main
git merge feature/ma-fonction
git push origin main
```

## .gitignore
- Ajoutez un fichier `.gitignore` pour exclure fichiers temporaires, binaires, clés, etc. Exemples : `node_modules/`, `*.log`, `.env`.

## Historique et inspection
- Voir l'historique : `git log` ou `git log --oneline --graph --all --decorate`
- Voir les différences : `git diff`

## Revenir en arrière (avec prudence)
- Restaurer un fichier modifié : `git restore <fichier>`
- Annuler le dernier commit (local) : `git reset --soft HEAD~1` ou `git reset --hard HEAD~1` (perd les changements non sauvegardés)

## Résolution de conflits
- Lors d'un merge avec conflits, éditer les fichiers conflictuels, puis :

```powershell
git add <fichier-résolu>
git commit
```

## Bonnes pratiques
- Faites des commits petits et fréquents, avec un message clair.
- Travaillez par branches pour chaque fonctionnalité ou correctif.
- Faites `git pull` avant de pousser pour réduire les conflits.
- Ne mettez jamais d'informations sensibles (mots de passe, clés privées) dans le dépôt; utilisez `.gitignore`.

## Commandes utiles de dépannage
- Reprendre l'état d'un remote : `git fetch` puis `git reset --hard origin/main` (attention : écrase les changements locaux)
- Rebaser une branche : `git pull --rebase`

## Problèmes de propriété de dépôt

Si vous rencontrez l'erreur `fatal: detected dubious ownership in repository`, c'est que Git refuse d'opérer sur un dépôt dont vous n'êtes pas propriétaire (mesure de sécurité). Voici comment résoudre :

### Option 1 : Ajouter le répertoire à `safe.directory` (rapide)
Si vous faites confiance au dépôt, ajoutez-le à la liste blanche :

```powershell
git config --global safe.directory "C:/chemin/vers/depot"
# Ou avec plusieurs répertoires
git config --global safe.directory "*"
```

**Attention :** `safe.directory = *` désactive la vérification pour tous les dépôts — à utiliser uniquement en environnement de confiance.

### Option 2 : Corriger les permissions (plus sûr)
Changez le propriétaire du répertoire pour que ce soit vous :

```powershell
# Sur Windows, utiliser takeown (Prendre propriété)
takeown /F "C:\chemin\vers\depot" /R /D Y

# Puis vérifier avec icacls
icacls "C:\chemin\vers\depot"
```

### Option 3 : Cloner à nouveau
Si le dépôt vient d'une source externe (USB, partage réseau), le plus simple est de re-cloner :

```powershell
git clone https://exemple.com/mon-repo.git mon-repo-local
```

## Ressources & suites
- Configurez une clé SSH pour l'authentification si vous préférez SSH aux mots de passe.
- Lisez la documentation officielle : https://git-scm.com/doc
- Environnement graphique : GitHub Desktop, Sourcetree, GitKraken, ou intégration IDE (VS Code).

