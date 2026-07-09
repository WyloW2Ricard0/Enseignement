
# Visual Studio Code 1.127

[Date de sortie](https://code.visualstudio.com/updates/v1_127) : 1 juillet 2026

Cette version propose des agents capables de créer et tester des applications web dans le navigateur, une navigation par site plus sûre, et de nouvelles façons de maintenir les sessions d’agents chargées organisées.

## Agents

### Fenêtre des agents (Aperçu)

La fenêtre des agents sert à ***suivre*** les sessions d’agents entre projets et machines.
Elle évite de perdre le ***suivi*** quand plusieurs agents travaillent en parallèle.

1. Ouvrir la fenêtre Agents.
1. Créer un groupe.
1. Glisser une session dans ce groupe.
1. Épingler les sessions importantes.
1. Marquer les sessions terminées.

### Bannières d’entrée de chat

Une bannière apparaît au-dessus du chat quand une *pull request* a des échecs CI ou des commentaires.
Elle permet ***d’agir*** sans quitter la conversation.

- `/fix-ci` Affiche le nombre échouées avec des actions rapides :
  - **Fix Checks** lance une correction d’agent
  - **Reveal Checks** ouvre les échecs dans la vue Changements.
- `/act-on-feedback` Affiche le nombre de commentaires avec les actions :
  - **Adresser les commentaires** les remet à l’agent,
  - **Révéler les commentaires** les ouvre dans l’éditeur.

### Retour dans l’éditeur

Un retour peut être ***ajouté*** depuis la marge de l’éditeur.
L’agent reçoit un commentaire ***lié*** à une ligne précise.

1. Ouvrir le fichier modifié par l’agent.
1. Survoler la ligne à commenter.
1. Cliquer sur Add Feedback.
1. Écrire le retour.
1. Envoyer le commentaire à l’agent.

### Titres et descriptions de pull request

Create Pull Request utilise le ***contexte*** de session pour générer le titre et la description.
La pull request décrit ***mieux*** le travail réel.

1. Ouvrir la session d’agent.
1. Vérifier les changements.
1. Cliquer sur Create Pull Request.
1. Relire le titre généré.
1. Relire la description.
1. Publier la pull request.

## Sessions multi-chat

Une session peut ***contenir*** plusieurs chats.
On peut tester plusieurs pistes sans créer plusieurs sessions.

1. Ouvrir une session.
1. Cliquer sur + New Chat.
1. Utiliser chaque chat pour une piste.
1. Fermer un chat pour le masquer.
1. Le rouvrir depuis Conversations.
1. Utiliser Delete Chat pour le supprimer.

### Progrès et changements dans tous les chats

Le progrès et les modifications sont agrégés sur tous les chats.
On voit l’***état complet*** de la session.

1. Ouvrir une session multi-chat.
1. Regarder les onglets.
1. Lire la progression.
1. Vérifier Changes.
1. Ouvrir les changements combinés.

### Fork d’une conversation

Un *fork* crée un *chat pair* dans la même session.
On peut essayer une autre solution ***sans perdre l’historique***.

1. Choisir une conversation.
1. Utiliser l’action de fork.
1. Continuer dans le nouveau chat.
1. Garder l’ancien comme référence.
1. Comparer les deux pistes.

## Organisation des sessions

### Pilules dans l’en-tête

L’en-tête utilise des ***pilules*** pour l’espace de travail et les changements.
Les informations importantes sont plus faciles à ***lire***.

1. Ouvrir une session.
1. Lire Workspace.
1. Lire Changes.
1. Cliquer sur Changes pour ouvrir le diff.

### Focus sur l’entrée du chat

Quand une session s’ouvre, le ***focus*** va dans l’entrée du chat.
On peut ***écrire*** directement.

1. Sélectionner une session.
1. L’ouvrir.
1. Taper le message.

### Barre latérale réactive — Expérimental

La barre des sessions peut se ***masquer auto*** quand la fenêtre est étroite.
L’espace de travail reste ***lisible***.

Cadre : `sessions.layout.autoCollapseSessionsSidebar`

1. Ouvrir les paramètres.
1. Chercher sessions.layout.autoCollapseSessionsSidebar.
1. Activer le réglage.
1. Réduire la fenêtre.
1. Vérifier que la barre se masque.

### Dépannage avec /troubleshoot

`/troubleshoot` ***analyse*** les journaux de session.
Il aide à ***comprendre*** les réponses lentes ou les instructions ignorées.

1. Ouvrir la session.
1. Taper /troubleshoot.
1. Ajouter #session.
1. Sélectionner la session.
1. Décrire le problème.
1. Lire le diagnostic.

### Crédits de sous-agents

Le survol d’un sous-agent affiche les crédits IA utilisés.
Le coût du travail délégué devient visible.

1. Ouvrir une réponse avec un sous-agent.
1. Survoler la section.
1. Lire les crédits IA.

## Chat

### Sandboxing des commandes terminal

Les commandes d’agent peuvent s’exécuter en sandbox sur macOS et Linux.
Le réseau est bloqué et les fichiers sont protégés.

1. Lancer une tâche avec un agent.
1. Laisser l’agent proposer une commande.
1. Vérifier si elle reste en sandbox.
1. Approuver seulement si une élévation est demandée.

### Dépréciation du fournisseur Ollama intégré

Le fournisseur Ollama intégré est déprécié.
L’extension ***officielle*** Ollama est recommandée.
L’extension peut ***suivre*** plus vite les modèles Ollama.

1. Ouvrir les extensions.
1. Chercher Ollama.
1. Installer l’extension officielle.
1. Désactiver l’ancien fournisseur intégré.
1. Tester un modèle local.

### Caméra, emplacement, appareils

Le navigateur intégré prend en charge les ***permissions*** par site.
Chaque site reçoit seulement les droits ***nécessaires***.

1. Ouvrir un site dans le navigateur intégré.
1. Attendre la demande de permission.
1. Choisir Allow ou Block.
1. Ouvrir Site Permissions.
1. Modifier les droits du site.

### Outils d’agent disponibles

Les outils navigateur pour agents sont activés par défaut.
L’agent peut tester une application web sans outil externe.

Cadre : `workbench.browser.enableChatTools`

1. Demander à l’agent de créer une application web.
1. Lui demander de l’ouvrir dans le navigateur.
1. Lui demander de tester l’interface.
1. Lui demander de lire les erreurs.
1. Lui demander de corriger.
1. Relancer le test.

## Enterprise

Les administrateurs peuvent livrer des paramètres GitHub Copilot gérés avec un fichier JSON local.
Cela permet d’appliquer des règles Copilot sans MDM.

Ce fichier n’est respecté que lorsque les paramètres MDM ou les paramètres d’entreprise basés sur les comptes ne sont pas présents.

macOS : /Library/Application Support/GitHubCopilot/managed-settings.json
Linux : /etc/github-copilot/managed-settings.json
Fenêtres : %ProgramFiles%\GitHubCopilot\managed-settings.json
Le fichier contient un objet JSON utilisant le même schéma qu’un administrateur crée via GitHub.com, par exemple :

```json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  },
  "enabledPlugins": {
    "plugin@marketplace": false
  }
}
```

## Fonctionnalités et paramètres obsolètes

Aucun élément listé dans cette section
