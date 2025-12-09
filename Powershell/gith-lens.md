# GitLens — Guide d'utilisation

GitLens est une extension VS Code puissante qui enrichit l'intégration Git native en affichant des informations contextuelles, l'historique, les auteurs, et bien plus directement dans l'éditeur.

## Installation

1. Ouvrir VS Code
2. Aller dans Extensions (`Ctrl+Shift+X`)
3. Rechercher **GitLens** (par GitKraken)
4. Cliquer sur **Install**

Ou installer via la ligne de commande :
```powershell
code --install-extension eamodio.gitlens
```

## Fonctionnalités principales

### 1. Annotations en ligne (Blame)

GitLens affiche automatiquement des annotations à la fin de chaque ligne montrant :
- L'auteur du dernier commit qui a modifié cette ligne
- La date du commit
- Le message du commit (abrégé)

**Activation/désactivation :**
- `Ctrl+Shift+P` → `GitLens: Toggle Line Blame`
- Ou cliquer sur l'icône GitLens dans la barre d'état

**Configuration :**
```json
// settings.json
{
  "gitlens.currentLine.enabled": true,
  "gitlens.currentLine.format": "${author}, ${agoOrDate} • ${message}"
}
```

### 2. File Annotations (Blame complet)

Affiche les informations d'auteur pour **toutes** les lignes d'un fichier.

**Commandes :**
- `Ctrl+Shift+P` → `GitLens: Toggle File Blame`
- Ou cliquer avec le bouton droit → `GitLens` → `Toggle File Blame`

**Types d'annotations :**
- **Blame** : auteur + date pour chaque ligne
- **Changes** : met en évidence les modifications locales non commitées
- **Heatmap** : visualisation colorée de l'ancienneté des lignes (rouge = récent, bleu = ancien)

### 3. Hovers (infobulles)

Survoler une ligne avec la souris affiche une infobulle détaillée contenant :
- Auteur et date du commit
- Message complet du commit
- Hash du commit
- Boutons d'action : voir le diff, ouvrir le commit, copier le SHA

**Survoler les annotations :**
- Survoler l'annotation en fin de ligne pour plus de détails
- Cliquer sur le SHA pour ouvrir la vue du commit

### 4. Vue "GitLens" dans la barre latérale

Ouvrir la vue GitLens depuis l'icône dans la barre d'activité (à gauche).

**Sections principales :**

#### Repositories
- Liste de tous les dépôts ouverts dans le workspace
- Branches, tags, remotes, stashes
- Cliquer sur une branche pour basculer dessus

#### File History
- Historique complet du fichier actif
- Cliquer sur un commit pour voir les changements
- Comparer deux commits

#### Line History
- Historique de la ligne courante (où se trouve le curseur)
- Utile pour tracer l'évolution d'une ligne de code spécifique

#### Search & Compare
- Rechercher des commits par auteur, message, SHA
- Comparer deux branches/commits/tags

#### Commits
- Historique de tous les commits du dépôt
- Groupés par branche ou par date

### 5. Barre d'état (Status Bar)

En bas de l'éditeur, GitLens affiche :
- Branche courante
- Nombre de commits en avance/retard par rapport au remote
- Modifications locales non commitées

**Cliquer dessus :**
- Ouvre un menu rapide avec actions Git courantes (pull, push, fetch, switch branch)

### 6. Commandes rapides

Ouvrir la palette de commandes (`Ctrl+Shift+P`) et taper `GitLens:` pour voir toutes les commandes disponibles.

**Commandes utiles :**
- `GitLens: Show Commit Graph` — graphe visuel de l'historique (comme `git log --graph`)
- `GitLens: Open File on Remote` — ouvre le fichier actuel sur GitHub/GitLab dans le navigateur
- `GitLens: Copy Remote File URL` — copie l'URL du fichier sur le remote
- `GitLens: Show Quick File History` — affiche l'historique du fichier actif
- `GitLens: Compare References...` — compare branches/commits
- `GitLens: Search Commits` — recherche dans les commits (message, auteur, SHA)

### 7. GitLens Inspect (panneau contextuel)

Cliquer avec le bouton droit sur une ligne → `GitLens` → `Open Changes` pour voir :
- Les modifications apportées par le dernier commit affectant cette ligne
- Diff side-by-side

### 8. Compare et Diff

**Comparer deux branches :**
1. `Ctrl+Shift+P` → `GitLens: Compare References...`
2. Sélectionner la première branche/commit
3. Sélectionner la deuxième
4. Voir la liste des fichiers modifiés et les diffs

**Comparer deux commits :**
- Dans la vue "Commits", clic droit sur un commit → `Compare with...` → sélectionner un autre commit

**Comparer Working Tree avec un commit :**
- Clic droit sur un commit → `Compare Working Tree with...`

### 9. GitLens Interactive Rebase Editor

GitLens améliore l'éditeur de rebase interactif (`git rebase -i`) avec une interface visuelle :
- Glisser-déposer pour réordonner les commits
- Boutons pour squash, fixup, drop, edit
- Prévisualisation des changements

**Utilisation :**
1. Lancer un rebase interactif : `git rebase -i HEAD~5`
2. VS Code ouvre l'éditeur GitLens
3. Modifier l'ordre/actions via l'interface
4. Sauvegarder et fermer pour appliquer

### 10. Stashes

Vue "Repositories" → section "Stashes" :
- Voir tous les stashes sauvegardés
- Cliquer sur un stash pour voir son contenu
- Apply, pop, ou drop un stash

**Créer un stash :**
- `Ctrl+Shift+P` → `Git: Stash` (commande Git native)
- Ou via GitLens → menu contextuel sur les changements

## Raccourcis clavier courants

| Raccourci | Action |
|-----------|--------|
| `Ctrl+Shift+P` → `GitLens:` | Ouvre la palette de commandes GitLens |
| `Alt+B` | Toggle File Blame |
| `Alt+H` | Show Quick File History |
| Clic droit sur ligne | Menu contextuel GitLens |

## Configuration avancée

Personnaliser GitLens via `File` → `Preferences` → `Settings` → rechercher `gitlens`.

**Paramètres utiles :**

```json
{
  // Activer/désactiver les annotations en ligne
  "gitlens.currentLine.enabled": true,
  
  // Format des annotations
  "gitlens.currentLine.format": "${author} • ${agoOrDate} • ${message}",
  
  // Afficher le Blame complet par défaut
  "gitlens.blame.highlight.enabled": true,
  
  // Heatmap
  "gitlens.heatmap.ageThreshold": "90",
  
  // Activer le graphe de commits
  "gitlens.graph.enabled": true,
  
  // Compact sidebar views
  "gitlens.views.repositories.compact": true,
  
  // Désactiver les hovers (si trop intrusif)
  "gitlens.hovers.enabled": false
}
```

## Cas d'usage pratiques

### Identifier qui a écrit une ligne problématique
1. Placer le curseur sur la ligne
2. Regarder l'annotation en fin de ligne ou survoler pour voir l'infobulle
3. Cliquer sur le SHA pour ouvrir le commit complet
4. Voir le contexte (autres fichiers modifiés, message complet)

### Comparer votre branche avec `main`
1. `Ctrl+Shift+P` → `GitLens: Compare References...`
2. Sélectionner `main` puis votre branche
3. Voir tous les fichiers modifiés et les diffs

### Rechercher tous les commits d'un auteur
1. Ouvrir la vue "Search & Compare"
2. Cliquer sur "Search Commits"
3. Entrer le nom de l'auteur
4. Voir la liste de tous ses commits

### Ouvrir un fichier sur GitHub
1. Ouvrir le fichier dans l'éditeur
2. `Ctrl+Shift+P` → `GitLens: Open File on Remote`
3. Le fichier s'ouvre dans votre navigateur sur GitHub/GitLab

### Voir l'évolution d'une fonction
1. Sélectionner la fonction (plusieurs lignes)
2. Clic droit → `GitLens` → `Show Line History Selection`
3. Voir tous les commits ayant modifié cette sélection

## Fonctionnalités premium (GitLens+)

GitLens offre des fonctionnalités gratuites étendues, mais certaines avancées nécessitent un compte GitLens+ (gratuit pour usage personnel, payant pour équipes) :
- **Worktrees** : gestion des worktrees Git
- **Visual File History** : graphe visuel de l'historique d'un fichier
- **Commit Graph** : graphe complet et interactif de tous les commits
- **GitKraken integration** : intégration avec GitKraken Desktop

**Inscription :**
- `Ctrl+Shift+P` → `GitLens: Sign In to GitLens+`
- Créer un compte gratuit avec GitHub/GitLab/Bitbucket

## Dépannage

### Les annotations ne s'affichent pas
- Vérifier que vous êtes dans un dépôt Git : `git status` dans le terminal
- Activer les annotations : `Ctrl+Shift+P` → `GitLens: Toggle Line Blame`
- Vérifier les paramètres : `gitlens.currentLine.enabled` doit être `true`

### GitLens est trop lent sur un gros dépôt
- Désactiver certaines fonctionnalités lourdes :
  ```json
  {
    "gitlens.codeLens.enabled": false,
    "gitlens.blame.file.decorations.enabled": false
  }
  ```
- Limiter l'historique : `gitlens.advanced.maxListItems`

### Les hovers sont trop intrusifs
- Désactiver : `"gitlens.hovers.enabled": false`
- Ou ajuster le délai : `"gitlens.hovers.delay": 1000`

## Ressources

- Documentation officielle : https://gitlens.amod.io/
- GitHub : https://github.com/gitkraken/vscode-gitlens
- Tutoriels vidéo : https://www.youtube.com/@GitKraken
- Support : https://help.gitkraken.com/gitlens/gitlens-home/

---

**Astuce finale :** GitLens est hautement personnalisable. Explorez les paramètres (`Ctrl+,` → rechercher `gitlens`) pour adapter l'extension à votre workflow.
