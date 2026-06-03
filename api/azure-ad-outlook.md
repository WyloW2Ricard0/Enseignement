---
# Variable
showMiniToc: true
permissions: true
effectiveDate: 2026-01-13
image: "https://tommisaltiola.gallerycdn.vsassets.io/extensions/tommisaltiola/autofold-md-frontmatter/1.0.5/1710533937767/Microsoft.VisualStudio.Services.Icons.Default"

# Content pour faciliter la recherche
title: Accéder à Outlook via Azure AD
intro: Tutoriel pour connecter une application à Outlook/Microsoft 365 avec Azure AD et Microsoft Graph
type: tutoriel
topics:
  - Azure
  - Outlook
  - Microsoft Graph

# Information
author: RICHARD Wilfried
featuredLinks:
  - prev: api/azure-start.md
  - ofi: https://learn.microsoft.com/fr-fr/graph/api/resources/mail-api-overview?view=graph-rest-1.0
changelog:
  - 2026-01-13 : Création du guide Outlook via Azure AD
---
# Accéder à Outlook via Azure AD

Azure permet d’intégrer Outlook (Microsoft 365) à vos applications, par exemple pour envoyer des emails ou accéder à des calendriers.

## Qu'est-ce qu'Azure AD ?

**Azure Active Directory (Azure AD)** est le service d’annuaire et de gestion des identités de Microsoft dans le cloud. Azure AD est indispensable pour toute gestion d’accès, d’authentification et d’automatisation dans Azure.

Installer les modules nécessaires

```powershell
# Vérifier si le module AzureAD est installé
if (-not (Get-Module -ListAvailable -Name AzureAD)) {
  Install-Module -Name AzureAD
}
Connect-AzureAD
```

## Enregistrement d’une application

### Créer une application Azure AD

```powershell
$app = New-AzureADApplication \
  -DisplayName "NomDeMonApp"
$sp = New-AzureADServicePrincipal \
  -AppId $app.AppId
```

👉 [Accéder au portail Azure - Enregistrement d’application](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)

#### Types de comptes pris en charge

Qui peut utiliser cette application ou accéder à cette API ?

- **Locataire unique (single-tenant)**

  - Exemple : Application interne à l’entreprise, accessible uniquement par les employés de votre organisation.
  - Choix : `Comptes dans cet annuaire d'organisation uniquement`
  - CLI : `az ad app create --display-name "MonApp" --sign-in-audience AzureADMyOrg`

- **Multilocataire (multi-tenant)**

  - Exemple : Application SaaS destinée à plusieurs entreprises clientes, chaque client ayant son propre tenant Azure AD.
  - Choix : `Comptes dans un annuaire d'organisation`
  - CLI : `az ad app create --display-name "MonApp" --sign-in-audience AzureADMultipleOrgs`

- **Multilocataire + comptes Microsoft personnels**

  - Exemple : Application grand public qui accepte à la fois les comptes professionnels (Azure AD) et les comptes personnels Microsoft (Outlook.com, Xbox, Skype, etc.).
  - Choix : `Comptes dans un annuaire d'organisation et comptes Microsoft personnels`
  - CLI : `az ad app create --display-name "MonApp" --sign-in-audience AzureADandPersonalMicrosoftAccount`

- **Comptes Microsoft personnels uniquement**

  - Exemple : Application destinée uniquement aux utilisateurs Outlook.com, Xbox, Skype, etc. (pas d’accès pour les comptes professionnels/scolaires).
  - Choix : `Comptes Microsoft personnels uniquement`
  - CLI : `az ad app create --display-name "MonApp" --sign-in-audience PersonalMicrosoftAccount`

#### URI de redirection (facultatif)

Après que l’utilisateur s’est connecté et a autorisé l’application, Azure AD “renverra” la réponse d’authentification à l’URI de redirection, ce qui permet à votre application de récupérer le code ou le token pour poursuivre le processus (connexion, accès API, etc.).

- Exemple d’URI : https://example.com/auth ou http://localhost:3000/auth
- Permet de choisir le type d’application (web, mobile, desktop, SPA) pour adapter la configuration de l’authentification.
- **CLI** : `az ad app create --display-name "MonApp" --reply-urls "https://example.com/auth"`

>[!NOTE] pour **modifier le type** de comptes pris en charge d’une application existante, il ne faut pas utiliser az ad app create mais ***az ad app update***.

### Associer une application à un groupe de ressources

L’application/service principal est une identité qui peut recevoir des droits sur n’importe quelle ressource ou groupe de ressources via des rôles (RBAC), il faut :

```bash
az role assignment create \
  --assignee $app.AppId \
  --role "Contributor" \
  --resource-group MonGroupe
```

- `--assignee` : l’ID d’application (AppId) ou l’ObjectId du service principal.
- `--role` : le rôle à attribuer (ex : Contributor, Reader…).
- `--resource-group` : le nom du groupe de ressources cible.

👉 [Créer un group de ressource](azure-start.md#créer-un-groupe-de-ressources)

### Ajouter des autorisations Microsoft Graph (Outlook)

```powershell
# Exemple pour ajouter l'autorisation Mail.Read
Add-AzureADServicePrincipalOAuth2PermissionGrant \
  -ObjectId $sp.ObjectId \
  -Scope "Mail.Read" \
  -ClientId $app.AppId
```

### Générer un secret client

Après avoir créé votre application avec Azure CLI ou PowerShell, vous pouvez retrouver les identifiants nécessaires ainsi :

Crée un nouvel identifiant de mot de passe (également appelé secret client) pour l'application spécifiée.

```powershell
$clientSecret = New-AzureADApplicationPasswordCredential \
  -ObjectId $app.ObjectId
```

Une fois le secret client généré, il vous faut également récupérer l’identifiant du tenant Azure AD pour l’authentification :

```powershell
$tenant = Get-AzureADTenantDetail
```

👉 [Utilisez l’outil “Graph Explorer”](https://developer.microsoft.com/fr-fr/graph/graph-explorer) ; Connectez-vous, puis cliquez sur “Access token” pour voir et copier le token.

Note :

- `$app.AppId`donne le ClientId
- `$app.ObjectId` donne l’identifiant unique de l’**application** Azure AD que vous venez de créer.
- `$sp.ObjectId` donne l’identifiant unique du **service principal** associé à cette application dans Azure AD.
- `$tenantId` donne l’identifiant unique (tenantId) de **votre annuaire** Azure AD (votre organisation).

Vous pouvez maintenant utiliser directement ces variables dans vos scripts d’authentification MSAL.PS ou autres.

```bash
Install-Module -Name MSAL.PS
```

```bash
$scope = "https://graph.microsoft.com/.default"
$token = Get-MsalToken _
  -TenantId $tenant.ObjectId \
  -ClientId $app.AppId \
  -ClientSecret $clientSecret.value \
  -Scope $scope
```

### Utiliser Microsoft Graph pour accéder à Outlook

Pour envoyer un email, utilisez l’API Microsoft Graph avec les identifiants générés.

```powershell
# Exemple complet : envoyer un email avec Microsoft Graph
$email = @{
  Message = @{
    Subject = "Test depuis Microsoft Graph"
    Body = @{
      ContentType = "Text"
      Content = "Bonjour, ceci est un email envoyé via Microsoft Graph API et PowerShell."
    }
    ToRecipients = @(
      @{ EmailAddress = @{ Address = "destinataire@example.com" } }
    )
  }
  SaveToSentItems = $true
}

Invoke-RestMethod \
  -Uri "https://graph.microsoft.com/v1.0/me/sendMail" \
  -Headers @{Authorization = "Bearer $token.AccessToken"} \
  -Method POST \
  -Body ($email | ConvertTo-Json -Depth 10) \
  -ContentType "application/json"
```
