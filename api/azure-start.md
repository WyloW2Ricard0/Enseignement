---
# Variable
showMiniToc: true
permissions: true
effectiveDate: 2026-01-13
image: "https://tommisaltiola.gallerycdn.vsassets.io/extensions/tommisaltiola/autofold-md-frontmatter/1.0.5/1710533937767/Microsoft.VisualStudio.Services.Icons.Default"

# Content pour faciliter la recherche
title: Démarrer avec Azure : Guide pour un Compte Personnel
intro: Guide pratique pour débuter sur Azure avec un compte personnel et la CLI
type: tutoriel
topics:
	- Azure
	- CLI
	- Cloud

# Information
author: RICHARD Wilfried
featuredLinks:
	- next: ../api/azure-ad-outlook.md
	- ofi: https://learn.microsoft.com/fr-fr/cli/azure/
changelog:
	- 2026-01-13 : Création du guide de démarrage Azure personnel
---
# Démarrer avec Azure : Guide pour un Compte Personnel

Ce guide vous accompagne pas à pas pour utiliser Azure avec un compte personnel, en privilégiant l’utilisation du terminal (PowerShell, Azure CLI, Bash).

## Créer un compte Azure personnel

1. Rendez-vous sur [https://azure.microsoft.com/fr-fr/free/](https://azure.microsoft.com/fr-fr/free/)
2. Cliquez sur **Commencer gratuitement** et suivez les instructions pour créer votre compte.

## Installer Azure CLI (PowerShell)

```powershell
# Vérifie si Azure CLI est déjà installé
if (Get-Command az -ErrorAction SilentlyContinue) {

	Write-Host "Azure CLI est déjà installé." -ForegroundColor Green

} else {

	# Télécharge le programme
	Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi

	# Lance l’installation silencieuse
	Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'

	# Supprime le fichier d’installation MSI pour nettoyer
	Remove-Item .\AzureCLI.msi
	Write-Host "Azure CLI a été installé avec succès." -ForegroundColor Green
}
```

## Commandes de base Azure CLI

### Se connecter à Azure

```bash
az login
```

Suivez le lien affiché et connectez-vous avec votre compte personnel.

### Se déconnecter

```bash
az logout
```

### Documentation et aide

```bash
az --help
az <commande> --help
```

### Abonnements

Pour connaître vos abonnements disponibles :

```bash
az account list --output table
```

Pour changer d’abonnement par défaut :

```bash
az account set --subscription "NomOuIDAbonnement"
```

### Créer un groupe de ressources

Un groupe de ressources Azure permet de regrouper et de gérer les ressources (VM, bases de données, services web, etc.) liées à une même application.

Placez toutes les ressources d'une même application dans le même groupe.
Il facilite l'organisation, la gestion, la supervision et la suppression groupée des ressources.

```powershell
# Lister les groupe disponible
az group list --output table

# Créer un groupe de ressources
az group create \
  --name MonGroupe \
  --location westeurope
```

- `--name` : nom du groupe de ressources (ex : MonGroupeApp)
  - Donnez un nom explicite à votre groupe (ex : app-prod-rg, app-dev-rg)
- `--location` : région Azure où seront créées les ressources (ex : westeurope)
- `--subscription` : permet de spécifier l’abonnement Azure cible (nom ou ID). Si vous ne le précisez pas, [l’abonnement par défaut sera utilisé](#abonnements).

👉 [Voir les groupes de ressources sur le portail Azure](https://portal.azure.com/#view/HubsExtension/BrowseResourceGroups)

👉 [Créer un groupe de ressources sur le portail Azure](https://portal.azure.com/#create/Microsoft.ResourceGroup)

Supprimez le groupe pour nettoyer toutes les ressources associées - [portail Azure](https://portal.azure.com/#view/HubsExtension/BrowseResourceGroups)

```bash
az group delete --name MonGroupe --yes --no-wait
```
