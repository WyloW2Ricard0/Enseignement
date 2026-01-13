---
title: Journal des versions (Changelog)
intro: Page de présentation et d’accès aux journaux de versions du dépôt pour le cours pratique.
type: page
topics: [changelog, version, cours pratique]
---

# PROCESSUS DE MISE À JOUR DU CHANGELOG

## 1. PENDANT LE DÉVELOPPEMENT

- Ajoutez les changements dans [Unreleased]
- Groupez par catégorie (Added, Changed, etc.)
- Soyez descriptif mais concis

## 2. AVANT UNE RELEASE

- Créez une nouvelle section avec le numéro de version et la date
- Déplacez les entrées de [Unreleased] vers cette section
- Vérifiez le versioning sémantique (MAJOR.MINOR.PATCH)
- Mettez en évidence les breaking changes

## 3. APRÈS LA RELEASE

- Créez un tag Git : git tag -a v1.0.0 -m "Version 1.0.0"
- Poussez le tag : git push origin v1.0.0
- Créez une release GitHub avec les notes du CHANGELOG
- Laissez [Unreleased] vide pour les futurs changements

## 4. VÉRIFICATIONS

- [ ] Toutes les dates sont au format YYYY-MM-DD
- [ ] Les breaking changes sont marqués **BREAKING**
- [ ] Les issues/PRs sont liées (#numéro)
- [ ] Le versioning sémantique est respecté
- [ ] Le langage est clair et orienté utilisateur
- [ ] Pas de jargon technique inutile
- [ ] Les sections sont dans l'ordre standard

## FIN DU CHANGELOG

- [ ] J'ai ajouté tous les changements significatifs
- [ ] Les breaking changes sont clairement marqués
- [ ] La date est correcte (format YYYY-MM-DD)
- [ ] Le numéro de version suit le Semantic Versioning
- [ ] Les liens vers issues/PRs sont corrects
- [ ] Le langage est compréhensible par les utilisateurs finaux
- [ ] J'ai vérifié l'orthographe et la grammaire
- [ ] Les sections sont dans le bon ordre
