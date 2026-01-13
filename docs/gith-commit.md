---
# Variable
showMiniToc: true
permissions: true
effectiveDate: 2026-01-01
image: "https://example.com/git-commit.png"

# Content pour faciliter la recherche
title: Convention des commit
intro: Quel est le format d'un commit !
type: documentation
topics:
    - git
    - commit
    - convention

# Information
author: RICHARD Wilfried
featuredLinks:
    - prev:
    - next:
    - mid:
    - exp:
    - ofi:
changelog:
    - 2026-01-13 : Initialisation du frontmatter YAML enrichi
---

# Conventional Commits : l’essentiel

On considaire ici que le git et deja [initialiser](gith-start.md)

Un commit est un snapshot de votre projet a un moment donne — il enregistre l'etat des fichiers indexes avec un message explicite et des metadonnees (auteur, date, hash unique).


## Pourquoi utiliser Conventional Commits ?

- Générer automatiquement le changelog
- Déterminer automatiquement l’incrémentation de version (SemVer)
- Communiquer clairement la nature des changements
- Faciliter la contribution et la relecture

**Définitions :**

- **type** : nature du changement
    - `feat:` ajouter la recherche
    - `fix:` corrige le bug d’affichage
    - `chore`: suppression du support Node 6\n\nBREAKING CHANGE: Node 6 n’est plus supporté.
    - `docs`: corrige l’orthographe du changelog
- **(scope)** : partie concernée du code (ex : auth, api…), optionnel
- **!** : indique un changement non rétrocompatible (breaking change)


## Exemples de message

```md
<!--**Première ligne** : resume court (50 caractères max) en imperatif present-->
Résumé court du changement

<!--**Corps** (optionnel) : explique le *pourquoi* plutot que le *comment*, separe par une ligne vide-->
- feat(scope)!: Ajout d’une nouvelle fonctionnalité majeure ou modification importante.
- ...

<!--body : explication détaillée-->
BREAKING CHANGE: Décrivez ici la rupture de compatibilité ou l’impact majeur pour l’utilisateur.
```

Plus d’infos : https://www.conventionalcommits.org/fr/v1.0.0/


## Lire un commit dans le terminal

Il est donc important de bien preparer son commit.
Le moyen pour moi est d'extraire dans un fichier apart.

```sh
# Afficher la liste des commits (recent -> ancien)
git log --oneline

# Afficher le détail d’un commit spécifique dans le terminal
$HASH_COMMIT = ef21b07
git show $HASH_COMMIT

# Exporter le détail d’un commit dans un fichier (avec chemin)
$PATH="docs/commits"
git show $HASH_COMMIT > "$PATH/$HASH_COMMIT.md"

# Exporter les detail du dernier commit
git show HEAD > "$PATH/lasted.md"

# Exporter la différence entre le dernier commit (HEAD) et la situation actuelle
git diff HEAD > "$PATH/next.md"

# Inclure aussi les nouveaux fichiers (non suivis)
# Méthode 1 — simple: marquer les nouveaux fichiers comme "intent-to-add"
git add -N .
git diff HEAD > "$PATH/next.md"
# (optionnel) Annuler l'intention d'ajout
git reset
```

Si vous préférez conserver l’index intact et concaténer le contenu des nouveaux fichiers sans les toucher, vous pouvez utiliser PowerShell:

```powershell
$PATH = "docs/commits"
# Diff complet (fichiers suivis)
git diff HEAD > "$PATH/next.md"

# Ajouter, en fin de fichier, le diff des fichiers non suivis (nouveaux)
git ls-files --others --exclude-standard |
    ForEach-Object { git diff --no-index -- NUL $_ } |
    Out-File -Append -Encoding utf8 "$PATH/next.md"
```


## Enregistrer les Commit

```powershell
# Verifier l'etat du depot
git status
```

mettre a jour ta branche locale avec les changements du depot distant.

```powershell
$GIT_REMOTE_DEFAUT="origin"
$GIT_BRANCH_DEFAULT="main"

# Recuperer les modifications depuis le depot distant
git pull $GIT_REMOTE_DEFAUT $GIT_BRANCH_DEFAULT

# Ajouter les modifications
git add . # pour tout ajouter
git add $FILE_NAME

# Enregistrer les modifications
git commit

# Pui insere le message dans la nouvel fenetre

# Envoyer les modifications locales vers le depot distant
git push $GIT_REMOTE_DEFAUT $GIT_BRANCH_DEFAULT
```


## ⚠️ **Erreur frequente :**

- `fatal: not a git repository (or any of the parent directories)`: Le gite n'a pas été [initialiser](gith-start.md#connecter-un-depot-local-a-un-distant)
- Si le depot distant contient des modifications qui ne figurent pas dans votre branche locale.
    ```powershell
    git log  --oneline --graph -5 --decorate

    # voir les modifications sans les fusionner
    git fetch
    git diff
    ```
    vous devez effectuer un pull  pour integrer les modifications distantes
    ```powershell
    $REMOTE_DEFAULT="origin"
    $BRANCH_DEFAULT="main"

    git pull --rebase $REMOTE_DEFAULT $BRANCH_DEFAULT # Ecraser les modifications
    git merge # OU fusionner les modifications
    ```
- `error: The following untracked working tree files would be overwritten by merge:` Cela signifie que des fichiers non suivis (untracked) dans votre dossier de travail seraient ecrases par la fusion. Git refuse donc d'ecraser ces fichiers pour eviter toute perte de donnees.
    ```powershell
    $FILLE_PATH="path/file-name"

    # voir tous les fichiers non suivis qui posent problème
    git status

    # Deplacez les fichiers non suivis concernes
    Move-Item $FILLE_PATH $FILLE_PATH.bak

    # Relancez la commande de fusion
    git merge

    # Comparez et restaurez si besoin les fichiers deplaces
    ```
