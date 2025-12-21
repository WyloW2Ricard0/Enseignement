
# Guide pratique pour un bon changelog

Un **changelog** est un fichier listant, par version, les changements notables d’un projet destiné aux humains, pas aux machines.

Il aide les utilisateurs et contributeurs à suivre l’évolution du projet.

Il se base sur les commits mais ne les liste pas tous : il sélectionne et reformule les changements importants pour chaque version publiée.

Pour plus d’informations, voir : https://keepachangelog.com/fr/1.0.0/

## Types de changements

Grouper par type de changement

- **Added** : nouvelle fonctionnalité
- **Changed** : modification d’une fonctionnalité existante
- **Deprecated** : fonctionnalité bientôt supprimée
- **Removed** : fonctionnalité supprimée
- **Fixed** : correction de bug
- **Security** : correction de faille

### Conseils type

- Garder une section "Unreleased" en haut pour les changements non publiés.
- Lister clairement les dépréciations, suppressions et changements non rétrocompatibles.
- Préférer le format de date ISO (ex : 2025-12-21).
- Indiquer la date de chaque version (format ISO : AAAA-MM-JJ).

### Mauvaises pratiques à éviter

- Utiliser le log Git brut comme changelog.
- Oublier de signaler les dépréciations ou suppressions.
- Utiliser des formats de date ambigus.

## Gestion sémantique de version (SemVer)

Pour clarifier la compatibilité, faciliter la gestion des dépendances et communiquer clairement les changements aux utilisateurs.

Plus d’infos : https://semver.org/lang/fr/

### Règles essentielles

Format : **MAJEUR.MINEUR.CORRECTIF** (ex : 2.1.3)

- Incrémentez **MAJEUR** pour les changements non rétrocompatibles (1.0.0 → 1.0.1)
- Incrémentez **MINEUR** pour les ajouts de fonctionnalités rétrocompatibles (1.0.1 → 1.1.0)
- Incrémentez **CORRECTIF** pour les corrections de bugs rétrocompatibles (1.1.0 → 2.0.0)

### Conseils version

- La version 0.y.z est réservée au développement initial (API instable)
- Ne jamais modifier une version déjà publiée
- Documenter l’API publique et ses changements

## Exemple de changelog

```md
# [1.2.0] - 2025-12-21

**Auteur :** Jean Dupont

## Added
- feat: ajouter la recherche avancée (Refs: a1b2c3d)
- feat(auth)!: ajout du support de l’authentification 2FA (Refs: d4e5f6g)

## Changed
- chore!: suppression du support Node 10 (Refs: h7i8j9k)
- feat(api)!: modifie la gestion des erreurs (BREAKING CHANGE) (Refs: l0m1n2o)
- docs(readme): améliore la documentation d’installation (Refs: p3q4r5s)

## Fixed
- fix(api): correction du bug d’affichage sur mobile (Refs: t6u7v8w, Issue: [#110](https://github.com/WyloW2Ricard0/Enseignement/issues/110))

## Deprecated
- L’ancienne API d’authentification est dépréciée (Refs: x9y0z1a)

## Removed
- Suppression du support de Node 10 (Refs: b2c3d4e)

## Security
- Correction d’une faille XSS sur le formulaire de contact (Refs: f5g6h7i, PR: [#220](https://github.com/WyloW2Ricard0/Enseignement/pull/220))
```
