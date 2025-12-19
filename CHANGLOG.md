
# Changelog

<!-- 
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
-->

---

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

---

## [Unreleased]

<!--
Section pour les changements en cours de développement, non encore publiés.
Déplacez ces entrées dans une version numérotée lors de la prochaine release.
-->

### Added
- CODE_OF_CONDUCT.md : Code de conduite Contributor Covenant v2.1 avec guides d'application
- CONTRIBUTING.md : Guide de contribution pour les nouveaux contributeurs (template)
- .gitignore : Configuration exhaustive multi-langages avec commentaires pédagogiques détaillés
- standards/Licence-choisire.md : Guide complet de choix de licence avec méthodologie en 5 questions et diagrammes Mermaid interactifs
- standards/Repositorie.md : Standards de structuration de répertoires avec checklist complète et conventions de nommage
- standards/changlog-methode.md : Guide Keep a Changelog et Semantic Versioning avec exemples
- standards/Environement-gestion.md : Gestion des variables d'environnement et fichiers de configuration
- standards/Repositorie-mauvais.md : Anti-patterns à éviter avec exemples comparatifs
- standards/Repositorie-exo.md : Exercices pratiques de structuration de projets
- Powershell/gith-demarrer.ipynb : Notebook Jupyter interactif pour apprendre Git avec exemples Python/PowerShell
- Powershell/gith-intro.md : Introduction aux systèmes de contrôle de version (VCS)
- Powershell/gith-lens.md : Guide complet GitLens pour VS Code avec screenshots et cas d'usage
- Powershell/shell-demarer.md : Commandes PowerShell de base pour débutants
- datas/ : Nouveau dossier de configuration centralisée
  - variable.env.exemple : Template de variables d'environnement Git et projet
  - setup-git.py : Script Python d'automatisation de la configuration Git
  - README.md : Documentation du système de configuration
- langages/python-intro.md : Automatisation Git avec Python et GitPython
- langages/python-subprocess.md : Documentation du module subprocess pour exécuter des commandes Git

### Changed
- README.md : Refonte complète en template professionnel de 800+ lignes avec :
  - Commentaires HTML explicatifs pour chaque section
  - Badge de licence, dernière modification, taille du dépôt
  - Table des matières interactive avec 10 sections principales
  - Section "À propos" avec contexte, objectifs et technologies
  - Guide "Démarrage rapide" en 4 étapes avec vérification
  - Structure du projet en ASCII art avec icônes et descriptions
  - Documentation organisée par thème, difficulté et durée
  - 4 cas d'usage détaillés avec commandes PowerShell
  - Workflow de contribution en 8 étapes avec règles et priorités
  - Roadmap Q1-Q4 2026 avec fonctionnalités planifiées
  - Section contact avec multi-canaux (bugs, suggestions, questions)
  - Remerciements et notes additionnelles avec compatibilité
  - Checklist finale de 8 vérifications avant publication

### Removed
- Data/variable.py : Déplacé et restructuré dans datas/variable.env.exemple
- Gith/Demarrage.md : Contenu fusionné et amélioré dans Powershell/gith-demarrer.ipynb
- Gith/README.md : Contenu intégré dans Powershell/gith-intro.md
- Gith/progit.pdf : Supprimé (remplacé par liens vers documentation officielle)
- Powershell/Demarage.md : Vide, remplacé par gith-demarrer.ipynb
- Powershell/README.md : Vide, contenu dispersé dans fichiers spécifiques

---

## [0.1.0] - 2025-12-09

<!--
CONTEXTE DE CETTE VERSION :
Première version structurée du projet pédagogique "Enseignement".
Cette release marque la transition d'un dépôt basique vers un projet
professionnel avec documentation complète, standards et guides.

OBJECTIFS ATTEINTS :
- Standardisation de l'organisation du dépôt
- Documentation exhaustive pour contributeurs et apprenants
- Guides pédagogiques complets (Git, licences, structure)
- Automatisation de la configuration Git
- Templates réutilisables pour futurs projets
-->

### Added
- Initialisation du dépôt Git sur master
- README.md initial avec description basique du projet
- Structure de dossiers de base (Gith/, Powershell/, Data/)
- Fichiers de documentation préliminaires

### Changed
- Migration de la structure initiale vers organisation professionnelle
- Refactorisation complète de l'arborescence des dossiers

### Fixed
- Configuration Git initiale avec safe.directory pour éviter les erreurs de propriété
- Résolution des problèmes de credential helper (manager-core)

---

## Notes pour les mainteneurs

<!--
PROCESSUS DE MISE À JOUR DU CHANGELOG :

1. PENDANT LE DÉVELOPPEMENT :
   - Ajoutez les changements dans [Unreleased]
   - Groupez par catégorie (Added, Changed, etc.)
   - Soyez descriptif mais concis

2. AVANT UNE RELEASE :
   - Créez une nouvelle section avec le numéro de version et la date
   - Déplacez les entrées de [Unreleased] vers cette section
   - Vérifiez le versioning sémantique (MAJOR.MINOR.PATCH)
   - Mettez en évidence les breaking changes

3. APRÈS LA RELEASE :
   - Créez un tag Git : git tag -a v1.0.0 -m "Version 1.0.0"
   - Poussez le tag : git push origin v1.0.0
   - Créez une release GitHub avec les notes du CHANGELOG
   - Laissez [Unreleased] vide pour les futurs changements

4. VÉRIFICATIONS :
   - [ ] Toutes les dates sont au format YYYY-MM-DD
   - [ ] Les breaking changes sont marqués **BREAKING**
   - [ ] Les issues/PRs sont liées (#numéro)
   - [ ] Le versioning sémantique est respecté
   - [ ] Le langage est clair et orienté utilisateur
   - [ ] Pas de jargon technique inutile
   - [ ] Les sections sont dans l'ordre standard

5. EXEMPLES DE VERSIONING :
   - 0.1.0 → 0.1.1 : Correction de bug mineur
   - 0.1.0 → 0.2.0 : Nouvelle fonctionnalité compatible
   - 0.9.0 → 1.0.0 : Première version stable publique
   - 1.0.0 → 2.0.0 : Breaking change majeur

6. OUTILS UTILES :
   - Générateur de changelog automatique : github-changelog-generator
   - Validation : npx changelogen --verify
   - Comparaison de versions : git log v1.0.0...v2.0.0 --oneline
-->

---

## Ressources

- [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/) — Standard de ce document
- [Semantic Versioning](https://semver.org/lang/fr/) — Règles de numérotation
- [Conventional Commits](https://www.conventionalcommits.org/) — Format de messages de commit
- [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github) — Publication de versions

---

**Version de ce template :** 1.0  
**Dernière mise à jour :** 9 décembre 2025  
**Mainteneur :** WyloW2Ricard0  
**Licence de ce template :** CC0 (Domaine Public) — Adaptez librement sans attribution

<!--
FIN DU CHANGELOG

CHECKLIST FINALE AVANT COMMIT :
- [ ] J'ai ajouté tous les changements significatifs
- [ ] Les breaking changes sont clairement marqués
- [ ] La date est correcte (format YYYY-MM-DD)
- [ ] Le numéro de version suit le Semantic Versioning
- [ ] Les liens vers issues/PRs sont corrects
- [ ] Le langage est compréhensible par les utilisateurs finaux
- [ ] J'ai vérifié l'orthographe et la grammaire
- [ ] Les sections sont dans le bon ordre

COMMIT MESSAGE SUGGÉRÉ :
docs: mise à jour du CHANGELOG pour la version X.Y.Z

- Ajoute X nouvelles fonctionnalités
- Documente Y corrections de bugs
- Mentionne Z breaking changes
-->
