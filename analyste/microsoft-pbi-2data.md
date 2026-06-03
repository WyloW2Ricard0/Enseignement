---
# Variable
showMiniToc: true
permissions: true
effectiveDate: 2026-05-28
image: "https://learn.microsoft.com/en-us/training/achievements/get-data.svg"

# Content pour faciliter la recherche
title: Obtenir des données dans Power BI
intro: Vous allez découvrir comment récupérer des données à partir de diverses sources de données &  améliorer les performances lors de la récupération de données.
type: Cours
topics:
    - data
    - Microsoft PBI

# Information
author: RICHARD Wilfried
featuredLinks:
    - prev:
    - next:
    - mid:
    - exp:
    - ofi: https://learn.microsoft.com/fr-fr/training/modules/get-data/
changelog:
    - 2026-05-29 : Creation du cours
---

# Donnée dans PBI

L’environnement analytique repose sur l’intégration de référentiels hétérogènes distribués entre systèmes relationnels, fichiers plats, documents semi‑structurés et modèles multidimensionnels.

## 1. Introduction

Dans cette exemple nous avons quatre type de données :

1. Transactionnelles : opérations commerciales stockées dans *SQL Server* ; identifiants clients, articles vendus, employés associés aux ventes, métadonnées opérationnelles.
1. Attributs RH : stockées dans Excel maintenus par le département RH ; date d’embauche, fonction, responsable hiérarchique.
1. Logistiques :  Issues de l’application d’expédition sont stokées dans *Azure Cosmos DB* sous forme de documents JSON.
1. Projections financières : stockée dans *Azure Analysis Services*.

[Power Query](https://learn.microsoft.com/fr-fr/power-query/query-folding-basics) constitue le mécanisme de *préparation* analytique requiert l’ingestion, de nettoyage et de normalisation, avant la construction du modèle sémantique dans Power BI.

La publication dans le service permet la réutilisation du modèle et la génération de rapports dérivés.

## 2. Framework de modèle PBI

Les infrastructures de modélisation Power BI reposent sur la technologie tabulaire issue de SSAS/AAS, optimisée pour l’analyse multidimensionnelle et l’exécution de requêtes analytiques.

Power BI permet de développer un modèle local dans Desktop ou de s’appuyer sur des infrastructures distribuées offrant des performances élevées ou un accès quasi temps réel.

1. `Modèle de données` : Le modèle Power BI constitue une ressource analytique interrogeable via DAX ou MDX. Il s’agit d’un modèle sémantique tabulaire structuré en tables, relations, hiérarchies et mesures.
1. `Jeu de données` : Sont les `Modèles de données` une fois publié dans `Espace de travail`, artefact consommé par les rapports et tableaux de bord. Certains jeux de données peuvent représenter des connexions à des modèles externes, mais ce module se concentre sur les modèles développés dans Desktop.
1. `Requête analytique` : Sont les requêtes envoyer au `Jeu de données`, exécute en trois phases séquentielles :
    1. **Filtrer** : restriction du périmètre (filtres, segments, RLS).
    1. **Grouper** : segmentation visible du résultat (dimensions).
    1. **Résumer** : agrégation numérique (SUM, COUNT, MIN, MAX, mesures DAX).
1. `Modèle tabulaire` : Le modèle Power BI est tabulaire : tables, colonnes, relations, hiérarchies, mesures.
1. `Schéma en étoile` : modélisation [optimale](https://learn.microsoft.com/fr-fr/power-bi/guidance/star-schema) où les dimensions filtrent et groupent ; les faits sont agrégés.
    * **Dimensions** : entités métier (produits, clients, temps).
    * **Faits** : événements ou observations (commandes, stocks, taux).
1. `Framework de modèle` : Les paramètres du [mode de stockage](microsoft-pbi-2data.md#2-mode-de-stockage) de table déterminent l’infrastructure du modèle

Le choix du framework **conditionne** la latence, la volumétrie admissible, la gouvernance, la sécurité et les capacités analytiques.

La configuration du mode s’effectue au niveau de la table dans la *vue Modèle*, via le volet Propriétés.
La connexion requiert la spécification du serveur, de la base et du `mode de stockage` :

* `Importer` (par défaut) : créer une **copie locale du modèles sémantiques** à partir de votre source de données, compenser par une actualisation planifiée.
  * *Avantages* : offrent les meilleures **performances** (in‑memory, compression VertiPaq) & supportent l’ensemble des fonctionnalités et source
  * *Limitations* : Duplication des données & **Limite de 1 Go actualiser 8/jour** en capacité partagée.
* `DirectQuery` : Supprime toute mise en cache et [délègue](https://learn.microsoft.com/fr-fr/power-bi/connect-data/desktop-directquery-about) l’évaluation des requêtes à la source transactionnelle.
  * *Avantages* : La latence dépend alors exclusivement du moteur source.
  * *Limitations* : pas de pivot/unpivot
* `Double` (Composite) : Le moteur choisit dynamiquement la **stratégie optimale** selon le contexte d’exécution.
  * *Avantages* : arbitrage entre cache et requêtes directes.
  * *Limitations* : Relations limitées (cross‑source ou M:M)

Pour plus d’informations sur les jeux de données en temps réel, parcourez le module [Surveiller les données en temps réel avec Power BI](https://learn.microsoft.com/fr-fr/power-bi/connect-data/service-real-time-streaming).
Pour optimiser le stockage :

* réduire le nombre de tables,
* éviter les transformations non pliables,
* utiliser des tables d’agrégation,
* utiliser le mode **Double** pour les dimensions,
* filtrer les données à la source.

## 3. Obtenir des données

### 3.1. Fichiers

`fichiers plats` constituent des conteneurs **tabulaires** dépourvus de hiérarchie, caractérisés par une structure uniforme par ligne ; CSV, TXT, classeurs Excel.

L’éditeur Power Query permet de ce connecter et effectuer les opérations de nettoyage avant chargement.
Toute modification structurelle du fichier (suppression, renommage de colonnes, changement d’emplacement) invalide le modèle.
Power BI Desktop prend en charge l’ingestion de ces formats via *Obtenir des données*.

La connexion à un fichier implique la sélection du type de source, l’ouverture du fichier et l’affichage du Navigateur, qui expose les tables disponibles.
L’utilisateur choisit les entités à importer et opte pour *Charger* ou *Transformer les données*.
L’importation d’un fichier local crée un modèle sémantique **autonome non synchronisé**.

Utilisez une [passerelle](https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-install) Power BI.
Il permet un [transfert](https://learn.microsoft.com/en-us/training/modules/manage-datasets-power-bi/4-power-bi-gateway) sécurisé de données entre les systèmes sur site et les services cloud Microsoft sans déplacer les données vers le cloud.

### 3.2. Sources relationnelles

Le Navigateur expose les tables et vues disponibles.
L’utilisateur sélectionne les entités à charger ou à transformer.

L’importation peut également s’effectuer via une instruction SQL explicite dans *Option avancer*.

Les paramètres de connexion peuvent être modifiés ultérieurement pour répondre aux contraintes de sécurité (rotation des mots de passe).
Les mises à jour s’effectuent via les paramètres de la source de données ou via Power Query.

### 3.3. base NoSQL

Certaines organisations utilisent des bases *NoSQL*, dépourvues de schéma tabulaire.
Dans le scénario, les données logistiques sont stockées dans *Azure Cosmos DB* sous forme de documents JSON.

La connexion s’effectue via *Obtenir des données > Plus… > Azure Cosmos DB*.
L’utilisateur fournit l’URL du point de terminaison et les informations d’identification.
Power BI ingère les documents JSON et les expose dans Power Query pour transformation.

### 3.4. Azure Analysis Services

Plateforme PaaS tabulaire managée permettant la **consolidation sémantique** de sources hétérogènes.

Le modèle tabulaire opère comme couche sémantique intermédiaire entre les sources opérationnelles et les outils de visualisation.

La logique métier est déjà **encapsulée** dans le modèle, réduisant la nécessité de transformations supplémentaires dans Power BI.

Les divergences résident dans la présence de calculs pré‑matérialisés et dans l’usage de DAX ou MDX pour l’interrogation directe, en substitution à T‑SQL.

## 4. Créer des rapports dynamiques avec des paramètres

Les rapports dynamiques permettent la modification des données affichées en fonction de valeurs [paramétrées](https://learn.microsoft.com/fr-fr/power-bi/transform-model/desktop-what-if) pour **contrôler** la filtration ou la modification de la source de données.

### 4.1. Champs

Permet de sélectionner dynamiquement un champ dans un visuel, Utile pour créer des rapports interactifs et adaptatifs.

Dans Power Query, l’utilisateur crée un paramètre (type Texte, valeur libre), puis modifie la requête dans l’Éditeur avancé pour concaténer le paramètre dans l’instruction.
L’application du paramètre dans le rapport s’effectue via *Modifier les paramètres*, suivie de l’actualisation du modèle.

### 4.2 Plage numérique

Une table calculée contenant la plage ou une mesure représentant la valeur sélectionnée; scénarios hypothétiques (ex. taux de change)

Pour gérer plusieurs valeurs simultanément, l’utilisateur crée une table Excel contenant la liste des valeurs.

1. Cette table est importée dans Power BI, renommée et typée.
1. Une fonction Power Query est générée à partir de la requête paramétrée.
1. La table des valeurs appelle ensuite cette fonction via *Appeler une fonction personnalisée*, produisant une colonne contenant les résultats pour chaque valeur.
1. L’expansion de cette colonne expose les champs nécessaires au rapport.

## 5. Optimiser les performances

Des visuel ou filtre peut mettre plus de temps que d'autre.
90 % des problèmes de performance proviennent d’un modèle mal conçu ou de mesures inefficaces.

Les erreurs d’importation résultent de la diversité des sources, des messages d’erreur propres à chaque système et des contraintes matérielles ou réseau.

Le [Query Folding](https://learn.microsoft.com/fr-fr/power-query/query-folding-basics) dans l’éditeur Power Query vous aide à accroître les performances de vos rapports Power BI.
Dans ce processus appelé `pliage` de requête, il détermine quelles étapes peuvent être déchargées vers votre source de données afin d'optimiser l'exécution de votre requête.

Avec la fonction de [mise en cache](https://learn.microsoft.com/en-us/training/modules/manage-datasets-power-bi/9-query-caching) des requêtes.
Vous utilisez des ressources cloud sur vos capacités Fabric ou Premium dans le service Power BI pour charger votre rapport. La mise en cache des requêtes garantit une performance constante au lieu de surcharger les ressources sémantiques du modèle.
Comprendre le flux des données de la source vers sa destination peut être un défi.
La vue de la [linéation](https://learn.microsoft.com/en-us/training/modules/manage-datasets-power-bi/9a-lineage) des données de Power BI vous aide à répondre à ces questions.

Plusieurs principes structurants améliorent la performance globale :

1. Séparer date et heure dans les colonnes combinées afin d’améliorer la compression et la performance du moteur `VertiPaq`.
1. [réduire](https://learn.microsoft.com/fr-fr/power-bi/guidance/import-modeling-data-reduction) le nombre de colonnes ou de lignes, simplifier les requêtes, ou segmenter les extractions en plusieurs requêtes fusionnées ensuite dans Power Query.
1. Les agrégations permettent de stocker des **tables résumées** en mode Import, tout en conservant les tables détaillées en DirectQuery.
1. Traiter les données dans la source native : la [délégation](https://learn.microsoft.com/fr-fr/power-bi/guidance/directquery-model-guidance) maximise l’efficacité et réduit la charge locale.
1. Utiliser des requêtes SQL natives en DirectQuery, en évitant les procédures stockées et les CTE, qui ne se plient pas.

Vous pouvez déterminer les goulots d’étranglement qui se produisent lors du chargement et de la transformation de vos données.
Pour accéder aux diagnostics de requête dans l’éditeur Power Query, accédez à *Outils* dans le ruban Accueil, sélectionnez *Démarrer les diagnostics*, veillez à sélectionner *Arrêter les diagnostics*.
La sélection de *Diagnostiquer l’étape* vous montre la durée nécessaire à l’exécution des étapes

Ou l’outil [Performance Analyzer](https://learn.microsoft.com/fr-fr/power-bi/create-reports/performance-analyzer) mesure ; trier par durée décroissante puis analyser les visuels les plus coûteux.

* **Requête DAX** : temps d’exécution du moteur,
* **Affichage du visuel** : rendu graphique, géocodage, images,
* **Autre** : préparation, dépendances, attente d’autres visuels.
