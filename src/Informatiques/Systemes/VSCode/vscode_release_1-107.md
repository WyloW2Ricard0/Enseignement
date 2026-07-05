---
versions: 1.0.0
effectiveDate: 2025-12-15
author: RICHARD Wilfried

title: VS Code 1.107 – Nouveautés
intro: Résumé des nouveautés, améliorations et corrections de la version 1.107 de Visual Studio Code.
type: changelog
topics:
  - vscode
  - nouveautés
  - changelog
  - release
image: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/langfr-250px-Visual_Studio_Code_1.35_icon.svg.png"
---

# VS Code 1.107.1 – Nouveautés utiles

Retrouvez le détail complet des nouveautés et corrections sur le site officiel : [Notes de version VS Code 1.107](https://code.visualstudio.com/updates/v1_107)

## Agents et Chat

- Sessions d’**agents améliorées** : vue côte-à-côte, état mémorisé, marquage des sessions nécessitant une action, ***archivage simplifié***.
- **Orchestration multi-agents** : Copilot et agents personnalisés ***peuvent collaborer et s’exécuter en parallèle*** (local, cloud, arrière-plan).  Utilisez l’option pour déléguer une tâche à un autre agent (bouton  *"Continue in"*), chacun dans son propre contexte (local, cloud, ou arrière-plan). Pour travailler sur plusieurs branches ou contextes sans conflit (*Git worktree*).
- **Partage d’agents** personnalisés dans une organisation GitHub (*expérimental*).
- **Utilisation de sous-agents personnalisés** pour déléguer des tâches complexes.
- ***Support des « skills » Claude*** (*expérimental*).

## Chat et expérience utilisateur

- Chat intégré à la gestion des agents, ***navigation facilitée*** entre sessions.
- **Amélioration de l’UX** : sections repliables, affichage des statuts de commandes terminal, raccourcis clavier pour le terminal et les agents personnalisés.
- **Affichage des diffs** lors de l’édition de ***fichiers sensibles***.
- ***Recherche textuelle possible dans les fichiers ignorés*** (.gitignore, node_modules…).
- **Outil fetch plus robuste** (récupère aussi le contenu dynamique des pages web).

## Modèles et extensions
- **Éditeur centralisé** pour gérer tous les modèles de langage (Copilot, BYOK, tiers…).
- Possibilité de masquer/afficher les modèles dans le sélecteur.
- **Unification des suggestions** Copilot dans l’extension Copilot Chat (l’extension Copilot classique sera dépréciée en janvier 2026).

## Développement, code et terminal
- Suggestions de ***renommage intelligentes pour TypeScript***.
- ***Nouveau modèle de suggestions*** de modifications.
- Affichage des ***suggestions hors du viewport***.
- Ajout du **support des stashes** dans la vue Contrôle de source : vous pouvez désormais voir, appliquer, supprimer et gérer les stashes Git directement depuis l’interface Source Control, sans passer par la ligne de commande.
- ***Terminal Suggest activé par défaut*** (complétions et suggestions contextuelles en ligne de commande).

## Authentification et sécurité
- Support natif du broker Microsoft sur macOS Intel et Linux x64 (en plus de Windows et macOS ARM).
- Suppression de l’authentification Microsoft « classique ».
- Contrôle fin sur l’auto-approbation des outils agents (sécurité entreprise).

## MCP et entreprise
- Support du dernier standard MCP (2025-11-25).
- Serveur MCP GitHub intégré à Copilot Chat (préversion).
- Application automatique des politiques GitHub Enterprise dans Codespaces.

## Corrections notables
- Nombreux correctifs sur le terminal, la gestion des fenêtres, le contrôle de source, Python, etc.

---
Pour plus de détails, consultez les notes de version complètes sur le site officiel de VS Code.
Screenshot showing the 'Continue in' button in an untitled prompt file.
