---
versions: 1.0.0
effectiveDate: 2025-12-19
author: RICHARD Wilfried

title: Accès et automatisation GitHub
excerpt: Guide synthétique pour sécuriser, automatiser et choisir le bon mode d’accès à l’API GitHub.
type: guide
topics:
  - github
  - api
  - automatisation
  - sécurité
image: "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"

---

# Accès et automatisation GitHub : guide synthétique

## Sécurité & Bonnes pratiques
- Traitez les jetons comme des mots de passe : ne les partagez ni ne les publiez jamais.
- Limitez les permissions et l'accès aux dépôts au strict nécessaire.
- Définissez une date d'expiration.
- Supprimez rapidement les jetons inutilisés.
- Utilisez un gestionnaire de mots de passe ou le CLI pour stocker les jetons en sécurité.

## Choisir le type d’accès

Les méthodes sont maintenant triées du plus minimal au plus avancé :

1. **Accès utilisateur authentifié (API GitHub sans clé)** :
	- Accès à https://api.github.com sans clé, simplement en étant connecté à son compte GitHub (session utilisateur, OAuth ou cookie).
	- Limité en quotas et permissions : accès aux données publiques ou à votre compte selon les autorisations.
	- Pratique pour des requêtes ponctuelles ou l’exploration de l’API sans automatisation avancée.
	- [Documentation officielle](https://docs.github.com/fr/rest/overview/authenticating-to-the-rest-api?apiVersion=2022-11-28#using-the-api-without-authentication)

1. **Transfert d’agent SSH** (besoin temporaire, minimal) :
	- Permet d’utiliser la clé SSH de l’utilisateur local pour des déploiements manuels ou temporaires, sans stocker de clé sur le serveur.
	- Rapide, pas de gestion de clés, nécessite une connexion manuelle, peu adapté à l’automatisation complète
	- [Configurer le transfert d’agent SSH](https://docs.github.com/fr/authentication/connecting-to-github-with-ssh/managing-deploy-keys#set-up-ssh-agent-forwarding)

1. **Personal access token** (scripts/tests simples) :
	- Pour scripts/tests courts
	- Lié à un utilisateur : l’automatisation s’arrête si l’utilisateur perd l’accès
	- Privilégier les tokens « fine-grained »
	- Accès rapide à l’API par **clonage HTTPS**
	- [Générer un personal access token](https://docs.github.com/fr/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

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

## Jetons d'accès personnels GitHub : L'essentiel

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

### Utilisation en ligne de commande
- Utilisez le jeton comme mot de passe pour les opérations Git en HTTPS :
  ```sh
  git clone https://github.com/UTILISATEUR/DEPOT.git
  Username: VOTRE-UTILISATEUR
  Password: VOTRE-JETON
  ```
- Vous pouvez mémoriser le jeton avec un gestionnaire de mots de passe.
- Pour SSH, utilisez plutôt des clés SSH.

### Automatisation & Modèles
- Il est possible de pré-remplir le formulaire de création de jeton avec des paramètres d'URL (nom, description, permissions, etc.).
- Voir [Docs GitHub : Modèles de jetons](https://docs.github.com/fr/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#using-url-parameters-to-prefill-token-details)

### Références
- [Docs GitHub : Jetons d'accès personnels](https://docs.github.com/fr/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [Bonnes pratiques pour les identifiants API](https://docs.github.com/fr/authentication/keeping-your-account-and-data-secure/keeping-your-api-credentials-secure)
