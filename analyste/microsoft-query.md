---
# Variable
showMiniToc: true
permissions: true
effectiveDate: 2026-05-28
image: "https://learn.microsoft.com/en-us/training/achievements/clean-transform-and-load-data-in-power-bi.svg"

# Content pour faciliter la recherche
title: Nettoyer, transformer et charger des données dans Power BI
intro: comment simplifier un modèle complexe, changer de types de données, renommer des objets et créer un tableau croisé dynamique à partir de données.
type: Cours
topics:
    - data
    - Microsoft Query

# Information
author: RICHARD Wilfried
featuredLinks:
    - prev:
    - next:
    - mid:
    - exp:
    - ofi: https://learn.microsoft.com/fr-fr/training/modules/clean-data-power-bi/
changelog:
    - 2026-05-29 : Creation du cours
---

# Données dans Power Query

Les anomalies typiques incluent : valeurs numériques codant des catégories, erreurs, valeurs Null, duplications, concaténations non normalisées (adresses, identifiants), incohérences structurelles.

Ces défauts altèrent les mesures, biaisent les agrégations et compromettent la validité des rapports.

## 1. Mettre en forme les données initiales

L’Éditeur Power Query opère comme **couche** de transformation intermédiaire, indépendante de la source. Chaque action est enregistrée sous forme d’étape, *rejouée à chaque actualisation*.

Ouvrez l’Éditeur [Power Query](https://learn.microsoft.com/fr-fr/power-query/power-query-ui#the-query-ribbon) en cliquant sur le bouton *Transformer les données* dans l’onglet *Accueil* de Power BI Desktop.

## 1.1. Identification des en‑têtes et structures

Les données importées peuvent présenter des en‑têtes mal positionnés, des colonnes anonymes ou des lignes parasites. La première opération consiste à localiser les en‑têtes effectifs et à corriger leur position.

* *Promouvoir les en‑têtes* : La fonctionnalité *Utiliser la première ligne pour les en‑têtes* convertit la ligne supérieure en noms de colonnes.
* *Renommer les colonnes* : Les en‑têtes doivent être corrigés pour assurer cohérence, lisibilité et conformité aux conventions métier.
* *Supprimer les lignes du haut* : Les lignes vides ou non pertinentes doivent être éliminées pour stabiliser la structure tabulaire.

## 1.2. Réduction de la volumétrie

La suppression précoce des colonnes inutiles optimise la performance, simplifie le modèle et réduit les risques d’incohérence.

* *Supprimer les colonnes* sélectionnées,
* *Supprimer les autres colonnes* pour ne conserver que l’essentiel.

## 1.3. Transformations structurelles

* *Dépivoter* : Le dépivotage convertit des colonnes en lignes afin de normaliser des structures matricielles (ex. colonnes annuelles → attribut Year + valeur).
* *Pivoter* : Le pivotage agrège des valeurs selon une dimension unique, produisant une table structurée par regroupement (Count, Sum, Average, etc.).

## 2. Simplifier la structure des données

1. **Renommer les requêtes** : Les noms de tables doivent refléter les entités métier (PMEST). Les préfixes techniques (ex. *vProduct*, *FactProductTable*) doivent être éliminés.
1. **Remplacer des valeurs** : La fonctionnalité *Remplacer les valeurs* corrige les incohérences lexicales (ex. fautes d’orthographe, codes non standardisés).
1. **Remplacer les valeurs Null** : Les Null doivent être remplacés par des valeurs pertinentes (ex. 0 pour des montants), afin d’éviter les biais dans les agrégations.
1. **Supprimer les doublons** : La déduplication stabilise les dimensions et permet la création de tables de référence uniques.

## 3. Évaluer et modifier les types de données

Power BI détecte automatiquement les [types](https://learn.microsoft.com/fr-fr/power-bi/connect-data/desktop-data-types) sur les 1 000 premières lignes, mais cette détection peut être incorrecte, notamment dans les fichiers plats.
Un type erroné empêche :

* la création de relations,
* l’utilisation de fonctions temporelles,
* la génération de hiérarchies,
* l’exécution correcte des mesures.

La modification doit être effectuée dans Power Query, via :  *Transformer > Type de données*, l’icône de type dans l’en‑tête.
Chaque correction est enregistrée comme étape *Type modifié*.

## 4. Combiner plusieurs tables

La [combinaison](https://learn.microsoft.com/fr-fr/power-bi/connect-data/desktop-shape-and-combine-data/) permet de réduire la fragmentation et de créer des tables consolidées.

* **Ajouter des requêtes** : Concatène verticalement les lignes de plusieurs tables (union).
* **Fusionner des requêtes** : Joint horizontalement les colonnes selon une clé commune (join).

Permet de créer une table « source de vérité » à partir de plusieurs référentiels (ex. employés, fournisseurs, clients).

## 5. Profiler des données

L’Éditeur Power Query détermine les anomalies des données à l’aide de la fonctionnalité de profilage structurels :

1. *Distribution des valeur* : frequance sur les décomptes de données pour identifier les doublons et valeur unique.
1. *Profil de valeur* : identification des donnée null ou en erreur

Dans l’onglet Modèle, gérer, créer, modifier et supprimer des relations entre différentes tables à l’aide du bouton Gérer les relations, qui se trouve sur le ruban.
