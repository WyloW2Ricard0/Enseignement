---
versions: 0.1.0
effectiveDate: 
author: RICHARD Wilfried
title: Glossaire Git

excerpt: Définitions des principaux concepts Git (stash, worktree, etc.) pour la gestion de versions.
type: reference
topics:
  - git
  - glossaire
  - versioning
  - workflow
image: "https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png"
---

**Stash (Git)** : Fonctionnalité de Git permettant de mettre temporairement de côté (sauvegarder) des modifications en cours dans l’arbre de travail, sans les valider (commit). Cela permet de revenir à un état propre, puis de réappliquer ces modifications plus tard. Utile pour changer rapidement de branche ou tester autre chose sans perdre son travail en cours.

**Git worktree** : Fonctionnalité de Git permettant de créer plusieurs copies de travail (worktrees) d’un même dépôt, chacune pouvant être sur une branche différente. Pratique pour travailler sur plusieurs branches en parallèle, tester des correctifs ou développer des fonctionnalités sans avoir à cloner plusieurs fois le dépôt.