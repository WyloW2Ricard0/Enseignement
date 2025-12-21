# Conventional Commits : l’essentiel

## Pourquoi utiliser Conventional Commits ?

- Générer automatiquement le changelog
- Déterminer automatiquement l’incrémentation de version (SemVer)
- Communiquer clairement la nature des changements
- Faciliter la contribution et la relecture

## Exemples

**Définitions :**

- **type** : nature du changement
  - `feat:` ajouter la recherche
  - `fix:` corrige le bug d’affichage
  - `feat`: modifie la gestion des erreurs
  - `chore`: suppression du support Node 6\n\nBREAKING CHANGE: Node 6 n’est plus supporté.
  - `docs`: corrige l’orthographe du changelog
- **(scope)** : partie concernée du code (ex : auth, api…), optionnel
- **!** : indique un changement non rétrocompatible (breaking change)

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

---
Plus d’infos : https://www.conventionalcommits.org/fr/v1.0.0/