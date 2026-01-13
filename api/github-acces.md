---
versions: 1.0.1
effectiveDate: 2025-12-22
author: RICHARD Wilfried

title: Accès et automatisation GitHub
intro: Guide synthétique pour sécuriser, automatiser et choisir le bon mode d’accès à l’API GitHub.
type: guide
topics:
  - github
  - api
  - automatisation
  - sécurité
image: "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"

---

# Accès GitHub : guide synthétique

## Sécurité & Bonnes pratiques
- Traitez les jetons comme des mots de passe : ne les partagez ni ne les publiez jamais.
- Limitez les permissions et l'accès aux dépôts au strict nécessaire.
- Définissez une date d'expiration.
- Supprimez rapidement les jetons inutilisés.
- Utilisez un gestionnaire de mots de passe ou le CLI pour stocker les jetons en sécurité.

### Références
- [Docs GitHub : Jetons d'accès personnels](https://docs.github.com/fr/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [Bonnes pratiques pour les identifiants API](https://docs.github.com/fr/authentication/keeping-your-account-and-data-secure/keeping-your-api-credentials-secure)

### Choisir le type d’accès

Les méthodes sont maintenant triées du plus minimal au plus avancé :

1. **Transfert d’agent SSH** (besoin temporaire, minimal) :
	- Permet d’utiliser la clé SSH de l’utilisateur local pour des déploiements manuels ou temporaires, sans stocker de clé sur le serveur.
	- Rapide, pas de gestion de clés, nécessite une connexion manuelle, peu adapté à l’automatisation complète
	- [Configurer le transfert d’agent SSH](https://docs.github.com/fr/authentication/connecting-to-github-with-ssh/managing-deploy-keys#set-up-ssh-agent-forwarding)

1. **Personal access token** (scripts/tests simples) :
	- Pour scripts/tests courts
	- Lié à un utilisateur : l’automatisation s’arrête si l’utilisateur perd l’accès
	- Privilégier les tokens « fine-grained »
	- Accès rapide à l’API par **clonage HTTPS**
	- [Générer un personal access token](https://docs.github.com/fr/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token)

1. **Clé de déploiement** (dépôt unique, CI/CD simple) :
	- Clé SSH attachée à un dépôt, permet à un serveur ou une CI/CD d’accéder à un dépôt spécifique (lecture seule ou écriture).
	- Pratique pour déployer sans exposer de token utilisateur.
	- [Configurer une clé de déploiement](https://docs.github.com/fr/authentication/connecting-to-github-with-ssh/managing-deploy-keys#set-up-deploy-keys)

1. **Utilisateur machine** (multi-dépôts, automatisation intermédiaire) :
	- Compte GitHub dédié à l’automatisation, avec une clé SSH propre : utile pour gérer plusieurs dépôts, mais à limiter pour la sécurité (risque si le compte est compromis).
	- [Configurer un utilisateur machine](https://docs.github.com/fr/authentication/connecting-to-github-with-ssh/managing-deploy-keys#set-up-machine-users)

1. **OAuth app** (intégration utilisateur, automatisation avancée) :
	- Agit uniquement pour le compte d’un utilisateur
	- Permissions larges, jetons longue durée
	- Moins sécurisé et moins flexible que GitHub App
	- Utilise le **clonage HTTPS avec token OAuth**
	- [Créer/configurer une OAuth App](https://docs.github.com/fr/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)

1. **GitHub Actions** (CI/CD, automatisation dépôt, avancé) :
	- Pour automatiser CI/CD, déploiement, gestion de projet dans un dépôt
	- Secrets intégrés pour interagir avec des services tiers
	- Utilise le **GITHUB_TOKEN intégré** (généré automatiquement pour chaque workflow)
	- [Configurer GitHub Actions](https://docs.github.com/fr/authentication/connecting-to-github-with-ssh/managing-deploy-keys#set-up-installation-access-tokens)

1. **GitHub App** (automatisation la plus avancée, multi-dépôts/orgas) :
	- Pour la plupart des intégrations et automatisations modernes
	- Permissions fines, sécurité renforcée, jetons courts, webhooks intégrés
	- Peut agir pour un utilisateur ou de façon autonome
	- Idéal pour automatiser plusieurs dépôts/organisations
	- Utilise principalement un **jeton d’accès d’installation** (CI/CD, bots, intégrations)
	- [Créer/configurer une GitHub App](https://docs.github.com/fr/authentication/connecting-to-github-with-ssh/managing-deploy-keys#set-up-installation-access-tokens)

## Utilisation personel

### Types

- **Fine-grained (granulaire)** : Recommandé. Restreint à certains dépôts, permissions précises, peut nécessiter l'approbation d'une organisation. [Créer](https://github.com/settings/personal-access-tokens/new)
- **Classique** : Accès plus large, moins sécurisé, requis pour certaines fonctions héritées. [Créer](https://github.com/settings/tokens/new)

### Utilisation

- À utiliser à la place d'un mot de passe pour l'API GitHub ou la ligne de commande.
- À stocker comme secret dans les CI/CD (ex : GitHub Actions, Codespaces).
- Privilégier le `GITHUB_TOKEN` intégré dans les Actions si possible.

### Création

1. Aller dans [Paramètres GitHub > Paramètres développeur > Jetons d'accès personnels](https://github.com/settings/tokens).
2. Choisir **Fine-grained** ou **Classique**.
3. Définir le nom, l'expiration et les permissions (granulaire : sélectionnez dépôts et permissions ; classique : sélectionnez les scopes).
4. Générer et copier le jeton (il ne sera affiché qu'une seule fois).

### Ligne de commande

- Utilisez le jeton comme mot de passe pour les opérations Git en HTTPS :
	```sh
	git clone https://github.com/UTILISATEUR/DEPOT.git
	Username: VOTRE-UTILISATEUR
	Password: VOTRE-JETON
	```
- Vous pouvez mémoriser le jeton avec un gestionnaire de mots de passe.
- Pour SSH, utilisez plutôt des clés SSH.
- Exemple de vérification des scopes
	```sh
	curl -H "Authorization: Bearer OAUTH-TOKEN" https://api.github.com/user -I
	# X-OAuth-Scopes: repo, user
	# X-Accepted-OAuth-Scopes: user
	```

### Automatisation & Modèles

- Il est possible de pré-remplir le formulaire de création de jeton avec des paramètres d'URL (nom, description, permissions, etc.).
- Voir [Docs GitHub : Modèles de jetons](https://docs.github.com/fr/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#using-url-parameters-to-prefill-token-details)

**Principaux scopes OAuth :**

Genere les [taken classique](https://github.com/settings/tokens) pour plus de facilité

| Sécurité  | Scope                         | Description/Usage principal |
| --------: | :---------------------------: | :- |
|           | repo                          | Contrôle total des dépôts privés  |
|           | repo:statut                   | État d’engagement d’accès |
|           | repo_deployment               | État de déploiement de l’accès|
| public    | public_repo                   | Accéder aux dépôts publics |
|           | repo:invite                   | Accéder aux invitations au dépôt|
|           | security_events               | Lire et écrire les événements de sécurité|
|           | workflow                      | Mettre à jour les flux de travail d’actions GitHub|
|           | write:packages                | Téléverser les packages dans le registre de paquets GitHub|
| public    | read:packages                 | Téléchargez des paquets depuis le GitHub Package Registry |
|           | delete:packages               | Supprimer les paquets du registre de paquets GitHub|
|           | admin:org                     | Contrôle total des organisations et équipes, lecture et écriture des projets d’organisation|
|           | write:org                     | Lire et écrire l’adhésion à l’organisation et à l’équipe, lire et écrire les projets d’organisation|
|           | read:org                      | Lisez les membres des organisations et des équipes, lisez les projets des organisations,<br>peut révéler la structure interne, des membres privés ou des projets non publics.|
|           | manage_runners:org            | Gérer les runners d’organisation et les groupes de runners|
|           | admin:public_key              | Contrôle total des clés publiques utilisateur|
|           | write:public_key              | Écrire les clés publiques utilisateur|
|           | admin:repo_hook               | Contrôle total des crochets de dépôt|
|           | write:repo_hook               | Crochets de dépôt d’écriture|
|           | read:repo_hook                | Crochets de lecture du dépôt,<br>expose des URLs, des intégrations ou des secrets.|
|           | admin:org_hook                | Contrôle total des crochets d’organisation|
|           | gist                          | Créez des éléments|
|           | notifications                 | Notifications d’accès,<br>y compris celles liées à des dépôts privés ou à des discussions confidentielles.|
|           | user                          | Mettre à jour TOUTES les données utilisateur|
| public    | read:user                     | Lire TOUTES les données de profil utilisateur |
| public    | user:email                    | Accéder aux adresses e-mail des utilisateurs (lecture seule) |
| public    | user:follow                   | Suivre et ne pas suivre les utilisateurs |
|           | delete_repo                   | Supprimer les dépôts|
|           | write:discussion              | Lire et écrire les discussions d’équipe|
| public    | read:discussion               | Lisez les discussions d’équipe |
|           | admin:enterprise              | Contrôle total des entreprises|
|           | manage_runners:enterprise     | Gérer les runners d’entreprise et les groupes de runners|
|           | manage_billing:enterprise     | Lire et écrire les données de facturation d’entreprise|
|           | read:enterprise               | Lire les données de profil d’entreprise,<br>qui peuvent inclure des détails internes non publics. |
|           | scim:enterprise               |Provisionnement des utilisateurs et des groupes via SCIM|
|           | audit_log                     |Contrôle total du journal d’audit|
|           | read:audit_log                |Accès de lecture du journal d’audit,<br>qui contient des traces d’actions souvent sensibles.|
|           | codespace                     |Contrôle total des espaces de code|
|           | codespace:secrets             |Possibilité de créer, lire, mettre à jour et supprimer des secrets d’espace de code|
|           | copilote                      |Contrôle total des paramètres de GitHub Copilot et des assignations de places|
|           | manage_billing:copilot        |Voir et modifier les affectations des sièges Copilot Business|
|           | write:network_configurations  |Écrire des configurations de réseau de calcul hébergées par Write Org|
| public    | read:network_configurations   | Configurations de réseau de calcul hébergées par l’organisation |
|           | project                       |Contrôle total des projets|
| public    | read:project                  | Accès de lecture des projets |
|           | admin:gpg_key                 |Contrôle total des clés GPG des utilisateurs publics|
|           | write:gpg_key                 |Écrire des clés GPG utilisateur publiques|
| public    | read:gpg_key                  | Lire les clés GPG des utilisateurs publics |
|           | admin:ssh_signing_key         |Contrôle total des clés de signature SSH des utilisateurs publics|
|           | write:ssh_signing_key         |Écrire les clés de signature SSH des utilisateurs publics|
| public    | read:ssh_signing_key          | Lire les clés de signature SSH des utilisateurs publics |
