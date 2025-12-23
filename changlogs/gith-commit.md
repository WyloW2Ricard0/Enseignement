---
versions: 1.1.0
effectiveDate: 2025-12-22
author: RICHARD Wilfried

title: Convention des commit
excerpt: Quel est le format d'un commit !
topics:
    - git
    - commit
    - convention
    - changelog
image: https://example.com/git-commit.png
---

# Conventional Commits : l’essentiel

## Pourquoi utiliser Conventional Commits ?

- Générer automatiquement le changelog
- Déterminer automatiquement l’incrémentation de version (SemVer)
- Communiquer clairement la nature des changements
- Faciliter la contribution et la relecture

**Définitions :**

- **type** : nature du changement
    - `feat:` ajouter la recherche
    - `fix:` corrige le bug d’affichage
    - `fix`: modifie la gestion des erreurs
    - `chore`: suppression du support Node 6\n\nBREAKING CHANGE: Node 6 n’est plus supporté.
    - `docs`: corrige l’orthographe du changelog
- **(scope)** : partie concernée du code (ex : auth, api…), optionnel
- **!** : indique un changement non rétrocompatible (breaking change)

## Exemples

```md
<!--type scope-->
feat(scope)!: Résumé court du changement

<!--description : résumé court du changement-->
feat(scope)!: Ajout d’une nouvelle fonctionnalité majeure ou modification importante.

<!--body : explication détaillée, optionnelle-->
BREAKING CHANGE: Décrivez ici la rupture de compatibilité ou l’impact majeur pour l’utilisateur.
```

## Lire un commit dans le terminal

Il est donc important de bien preparer son commit. Le moyen pour moi est d'extraitr dans un fichier apart.

```sh
# Afficher la liste des commits (recent -> ancien)
git log --oneline

# Afficher le détail d’un commit spécifique dans le terminal
$HASH_COMMIT = ef21b07
git show $HASH_COMMIT
 
# Exporter le détail d’un commit dans un fichier (avec chemin)
git show $HASH_COMMIT > docs/commits/$HASH_COMMIT.md

# Exporter les detail du dernier commit
git show HEAD > changlogs/commits/lasted.md

# Exporter la différence entre le dernier commit (HEAD) et la situation actuelle
git diff > changlogs/commits/unreleased.md
```

---
Plus d’infos : https://www.conventionalcommits.org/fr/v1.0.0/