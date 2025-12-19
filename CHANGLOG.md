---
title: Journal des versions (Changelog)
excerpt: Page de présentation et d’accès aux journaux de versions du dépôt pour le cours pratique.
type: page
topics: [changelog, version, cours pratique]
---

# Journal des versions

## Notes pour les mainteneurs

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


## FIN DU CHANGELOG

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
