GUIDE D'UTILISATION DE CE DOCUMENT :

Ce CHANGELOG suit la convention "Keep a Changelog" (https://keepachangelog.com/fr/1.0.0/)
et adhère au "Semantic Versioning" (https://semver.org/lang/fr/).

POURQUOI UN CHANGELOG ?
- Permet aux utilisateurs de suivre l'évolution du projet
- Documente toutes les modifications notables entre les versions
- Facilite la compréhension des changements et leur impact
- Sert de référence lors de la mise à jour
- Améliore la transparence et la confiance

STRUCTURE D'UNE VERSION :
## [X.Y.Z] - YYYY-MM-DD

### Added (Ajouté)
- Nouvelles fonctionnalités

### Changed (Modifié)
- Modifications de fonctionnalités existantes

### Deprecated (Déprécié)
- Fonctionnalités obsolètes (encore présentes mais à éviter)

### Removed (Supprimé)
- Fonctionnalités supprimées

### Fixed (Corrigé)
- Corrections de bugs

### Security (Sécurité)
- Correctifs de sécurité

VERSIONING SÉMANTIQUE (MAJOR.MINOR.PATCH) :
- MAJOR (1.0.0) : Changements incompatibles (breaking changes)
- MINOR (0.1.0) : Nouvelles fonctionnalités compatibles
- PATCH (0.0.1) : Corrections de bugs

BONNES PRATIQUES :
- Toujours dater les versions : ## [1.2.0] - 2025-12-09
- Grouper par type de changement (Added, Changed, etc.)
- Écrire pour les utilisateurs, pas pour les développeurs
- Lier aux issues/PRs : (#42)
- Ordre antichronologique : version la plus récente en haut
- Section "Unreleased" pour changements non encore publiés
- Utiliser l'impératif présent : "Ajoute X" plutôt que "Ajouté X"
- Être spécifique : éviter "Diverses corrections"
- Mentionner les breaking changes en MAJUSCULES : **BREAKING**

À ÉVITER :
- ❌ Oublier de dater les versions
- ❌ Mélanger plusieurs types dans une même section
- ❌ Copier-coller les messages de commit bruts
- ❌ Omettre les breaking changes
- ❌ Utiliser du jargon technique incompréhensible
- ❌ Ne pas mentionner les dépendances obsolètes

EXEMPLES DE FORMULATION :
- ✅ "Ajoute support de l'authentification OAuth 2.0"
- ❌ "OAuth marche maintenant"
- ✅ "**BREAKING**: Renomme la fonction `getUser()` en `fetchUser()`"
- ❌ "Change fonction"
- ✅ "Corrige le crash au démarrage sur Windows 11 (#156)"
- ❌ "Fix bug"

ADAPTATION À VOTRE PROJET :
1. Remplacez [Unreleased] par votre première version réelle
2. Ajoutez la date au format YYYY-MM-DD
3. Documentez tous les changements significatifs
4. Mettez à jour à chaque release
5. Gardez les anciennes versions pour l'historique
6. Ajoutez des liens vers les issues/PRs GitHub si applicable

LIENS AUTOMATIQUES (optionnel) :
En bas du fichier, ajoutez des liens vers les tags Git :
[Unreleased]: https://github.com/votre-user/votre-repo/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/votre-user/votre-repo/compare/v0.9.0...v1.0.0