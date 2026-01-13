# VS Code - Version 1.108 (Décembre 2025)

**Date de sortie:** 8 janvier 2026

## Fonctionnalités principales utiles

### Agent et Chat

- **Agent Skills** : Nouvelles compétences spécialisées pour l'IA (Ctrl+Space pour les suggestions)
  - Stockez des instructions, scripts et ressources dans `.github/skills/` ou `.claude/skills/`
  - Chaque skill doit avoir un fichier `SKILL.md` définissant son comportement
  - Activez avec `chat.useAgentSkills`
  - [Découvrez-en plus](https://code.visualstudio.com/docs/copilot/customization/agent-skills)

- **Améliorations de la vue des sessions** : Meilleure organisation et accessibilité
  - Regroupement selon l'État et l'âge
  - Informations sur les fichiers modifiés et les PR associées
  - Archivage de plusieurs sessions simultanément
  - Support du clavier amélioré

- **Chat session picker** : Accès facile aux sessions précédentes
  - Appuyez sur `Ctrl+P` et tapez "agent" pour accéder aux sessions
  - Actions disponibles : archiver, renommer, supprimer
  - Accessible depuis le titre du Chat

- **Nouvelles règles Terminal** :
  - Commandes `git`, `npm`, `rg`, `sed` auto-approuvées par défaut
  - Option pour masquer les commandes de l'historique shell (`chat.tools.terminal.preventShellHistory`)
  - Possibilité de créer des règles de session ou workspace

### Terminal

- **IntelliSense amélioré** : Suggestions de commandes intelligentes
  - Appuyez sur `Ctrl+Space` pour afficher les suggestions (par défaut, non automatiques)
  - Support des complétions `npm`, `git`, fichiers exécutables (macOS/Linux)
  - Possibilité d'activer "quick suggestions" et "suggest on trigger characters"
  - Un hint aide à la découverte lors de l'ouverture d'un terminal

- **Performance** : Collage et throughput améliorés
  - Collage rapide sans throttle pour >50 caractères
  - Copilot peut exécuter de grandes commandes sans ralentissement
  - Correction des crashes possibles sur macOS
  - Problèmes de "layout thrashing" résolus

- **800 glyphes personnalisés** : Symboles de haute qualité sans configuration de police
  - Box Drawing (U+2500-U+257F)
  - Block Elements, Braille Patterns, Powerline symbols
  - Git Branch symbols et Progress indicators
  - Symboles Legacy Computing (U+1FB00-U+1FBFF)
  - Mise à l'échelle avec hauteur de ligne et espacement

- **Améliorations visuelles** :
  - Overlay de dimensions lors du redimensionnement (colonnes × lignes)
  - Amélioration des underlines courbes (ressemblent maintenant à l'éditeur)
  - Support VT amélioré (sortie synchronisée, XTVERSION)

- **Historique du shell** : Option pour masquer les commandes de l'historique
  - Paramètre : `chat.tools.terminal.preventShellHistory`
  - Par défaut activé pour bash, zsh, pwsh, fish

### Édition de code

- **Copier le chemin des miettes de pain** vers le clipboard
  - Commande : "Copy Breadcrumbs Path"
  - Partagez l'emplacement exact d'un symbole avec votre équipe
  - Configurable via `breadcrumbs.symbolPathSeparator`

- **Nouveaux snippets transformations** : `snakecase` et `kebabcase`
  - Syntaxe : `${TM_FILENAME/(.*)/${1:/snakecase}/}` ou `${1:/kebabcase}`
  - `MyFileName.txt` → `my_file_name.txt` (snakecase)
  - Ou `my-file-name.txt` (kebabcase)
  - **Où configurer** : Fichier → Préférences → Configurer les snippets utilisateur
  - **Ou** : `Ctrl+Shift+P` → "Snippets: Configure User Snippets"
  - Format JSON : snippets personnalisés dans `%APPDATA%\Code\User\snippets\` (Windows)
  - Paramètres liés : `editor.snippetSuggestions` (inline, atTop, bottom, none)

- **Symboles en espace de travail** : Support des caractères spéciaux
  - `Ctrl+T` (Go to Symbol in Workspace)
  - Les caractères `#` ne filtrent plus les résultats
  - Utile pour les extensions (ex: rust-analyzer avec `main#`)

- **Importation de profils** : Glisser-déposer simplifiée
  - Déposez un fichier `.code-profile` dans VS Code
  - Aperçu et import dans l'éditeur Profiles
  - Partage facilité avec l'équipe

- **Importation de profils via glisser-déposer** :
  - Précédent : Seul drag-drop de `.code-workspace`
  - Nouveau : Support complet des `.code-profile`

### Contrôle de source (Git)

- **Blame amélioré** : Identifiez les vrais changements fonctionnels
  - Paramètre : `git.blame.ignoreWhitespace`
  - Ignorez les changements de formatage pour voir la vraie modification
  - Paramètre : `git.blame.editorDecoration.disableHover` pour désactiver le tooltip

- **Worktrees** : Gestion complète dans la vue Repositories (Experimental)
  - Visualisez tous les worktrees du référentiel
  - Actions : ouvrir en nouvelle fenêtre, supprimer, ouvrir en fenêtre actuelle
  - Activez avec `scm.repositories.explorer` et `scm.repositories.selectionMode`

- **Commit messages** : Édition améliorée dans l'éditeur
  - Actions commit/cancel visibles en bas à droite
  - Plus facile à découvrir que dans la barre de titre
  - Utilisation du plein éditeur pour rédiger les messages

### Debug et Tests

- **Breakpoints organisés** : Arborescence par fichier
  - Paramètre : `debug.breakpointsView.presentation` = `tree`
  - Vue plus lisible pour les projets complexes
  - Groupement automatique par fichier source

- **Coverage navigation** : Explorez rapidement les zones non testées
  - Barre d'outils Test Coverage avec boutons de navigation
  - Sautez entre les régions sans couverture
  - Commande : "Test: Show Coverage Toolbar"

- **Test Coverage Toolbar** :
  - Affichage et masquage simplifié
  - Navigation directe vers code non couvert

### Accessibilité

- **Accessible View** : Streaming en temps réel
  - Les réponses du chat se mettent à jour dynamiquement
  - Plus besoin de fermer/réouvrir pour voir les nouveaux contenus
  - Compatible avec les lecteurs d'écran

- **Variable d'ID de langage** : Automatisation pour accessibilité
  - Nouvelle variable : `${activeEditorLanguageId}`
  - Utilisable dans `window.title`
  - Utile pour les outils comme Talon (commandes vocales)
  - Exemple : `"${activeEditorLanguageId} - ${activeEditorShort}"`

- **Sortie MCP exclue** : Réduction du bruit
  - Sortie du serveur MCP (Model Context Protocol) exclue par défaut
  - Facilite l'utilisation avec lecteurs d'écran

### Maintenance et Ingénierie

- **Nettoyage GitHub massif** : Décembre 2025 (housekeeping)
  - **5,951 issues** fermées toutes repositories confondues
  - **1,203 issues** triées (état "unknown")
  - Dépôt principal : 2,872 issues fermées + 1,697 triées
  - Dépôt copilot : 1,659 issues fermées (175 restantes pour migration)
  - Résultat : Projet plus gérable et fonctionnalités percutantes
  - Outils de triage améliorés et déduplication

- **TypeScript pour extensions** : Développement sans build (Expérimental)
  - Authoring direct de extensions en TypeScript
  - Pas de step de build requis
  - Aspects à tester encore : tests, publication, workflows
  - [Plus d'infos](https://github.com/microsoft/vscode/discussions)

- **API Extension** : Nouvelles propriétés QuickPick
  - Propriété `prompt` : texte instructif persistent sous la boîte d'input
  - Propriété `resourceUri` : dérive auto des propriétés (label, description, icon)
  - Utile pour les interfaces de sélection fichier/dossier
