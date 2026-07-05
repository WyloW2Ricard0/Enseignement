---
# Variable
showMiniToc: true
permissions: true
effectiveDate: 2026-05-28
image: "https://learn.microsoft.com/en-us/training/achievements/introduction-end-analytics-use-microsoft-fabric.svg"

# Content pour faciliter la recherche
title: Présentation de l’analytique de bout en bout à l’aide de Microsoft Fabric
intro: Découvrez Microsoft Fabric, comment cela fonctionne et identifiez comment vous pouvez l’utiliser pour vos besoins d’analyse.
type: Cour
topics:
    - Analyste
    - Microsoft Fabric

# Information
author: RICHARD Wilfried
featuredLinks:
    - prev:
    - next:
    - mid:
    - exp:
    - ofi: https://learn.microsoft.com/fr-fr/training/modules/introduction-end-analytics-use-microsoft-fabric/
changelog:
    - 2026-05-28 : Creation du cours
---

# Microsoft Fabric

Découvrez Microsoft Fabric, comment cela fonctionne et identifiez comment vous pouvez l’utiliser pour vos besoins d’analyse.

L’émergence de la plateforme SaaS Microsoft Fabric visaient à réduire la fragmentation des gouvernaces pour l'unification des moteurs de calcul, *dans la continuité des architectures intégrées initiées par les systèmes décisionnels des années 1990 (ex. Teradata Unified Data Architecture)*.

## 1. Architecture conceptuelle

1. `Shortcuts` permettent d’accéder à des données externes sans duplication, *selon les principes de transparence d’emplacement introduits par les liens symboliques (Unix, 1978).*
1. `Workloads` regroupe des moteurs historiquement séparés (ETL, entrepôt, streaming, ML)
1. `OneLake` prolonge les travaux sur les `global namespaces`, *analogue à AFS (Andrew File System, 1989)* ; repose sur `ADLS Gen2` et prend en charge tout les formats.
1. Ecriture systématique au format `Delta-Parquet` assurant la compatibilité inter‑moteurs

## 2. Travail collaboratifs

Les équipes de données sont souvent confrontées à plusieurs défis en raison de la division des tâches et workflows de données.
La résolution des frictions collaboratives repose sur quatre mécanismes structurants :

1. **Stockage unique** : Connexion au objet directement au lakehouse via `Direct Lake`.
1. **Préparation réduite** : Les transformations sont faites qu'une foit en amont par les ingénieurs données, grâce à la centralisation des pipelines. *Les analystes ne bricolent plus des versions divergentes.*
1. **Sémantique partagé** : Tous les rôles utilisent la même définition métier des données. cree par Les ingénieurs d’analyse.
1. **Suppression séquentielles des rôles** : Tous les rôles lisent et écrivent dans OneLake, sans copie, sans déplacement.

## 3. Les charges de travail

1. `Data Factory` : Orchestration et ingestion ; *Workflow Management Coalition (1993)*.
1. `Data Engineering` : Pipelines, lakehouses, Delta-Parquet ; *ETL Informatica (1996)*.
1. `Data Science` : Notebooks, Spark, ML.
1. `Data Warehouse` : Modèle relationnel analytique ; *Star Schema (Kimball, 1996)*.
1. `Real-Time Intelligence` : Streaming et analyse temps réel ; *CEP (Complex Event Processing, 2003)*.
1. `Power BI` : Visualisation et modèles sémantiques.

## 4. IA intégrée**

1. `Copilot` : assistant IA génératif disponible dans toutes les charges de travail, *grace au Transformers (Vaswani, 2017)*.
2. `Agents de données` : Interfaces conversationnelles structurées.
3. `Fabric IQ` : Ontologies, graphes, modèles sémantiques.

## 5. Administration

1. `Espaces de travail` [constituent des conteneurs](https://learn.microsoft.com/fr-fr/fabric/fundamentals/workspaces) logiques des ressource, *héritiers des modèles de multi‑tenant introduits par Salesforce (1999)*.
1. `portail d’administration` **centralise** les autorisations, *reprenant les principes du policy‑based management (2005)*.
1. `catalogue OneLake` vous aide à analyser, surveiller et gérer la gouvernance des données partagées uniquement avec vous.

## 6. Activation

Les administrateurs peuvent activer Fabric dans le portail Admin de `Service PBI` > Paramètres du locataire

1. `Administrateur d’infrastructure` : gère les paramètres et les configurations de l’infrastructure.
1. `Administrateur Power Platform` : supervise les services Power Platform, notamment Fabric.
1. `Global administrator` : dispose de droits d’administrateur de structure implicites via des autorisations à l’échelle de l’organisation.

![onelake-architecture](https://learn.microsoft.com/fr-fr/training/wwl/introduction-end-analytics-use-microsoft-fabric/media/onelake-architecture.png)
