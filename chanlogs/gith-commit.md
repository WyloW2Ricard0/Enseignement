---
versions: 0.1.0
effectiveDate: 2025-12-21
author: RICHARD Wilfried

title: Convention des commit
excerpt: Quel est le format d'un commit !
type: guide
topics:
    - auth
    - sécurité
    - utilisateur
image: https://example.com/2fa.png
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
feat(auth)!: ajoute la validation 2FA

<!--description : résumé court du changement-->
Ajout d’une étape de validation à deux facteurs (2FA) lors de la connexion utilisateur.

<!--body : explication détaillée, optionnelle-->
BREAKING CHANGE: L’authentification nécessite désormais une validation 2FA.

<!--footer : informations additionnelles-->
Refs: #123
Reviewed-by: Alice
```

## Lire un commit dans le terminal

```sh
# Afficher la liste des commits
git log --oneline

# Afficher le détail d’un commit spécifique dans le terminal
$HASH_COMMIT = ef21b07
git show $HASH_COMMIT
```

---
Plus d’infos : https://www.conventionalcommits.org/fr/v1.0.0/