---
# Variable
showMiniToc: true
permissions: true
effectiveDate: 2026-05-29
image: "https://learn.microsoft.com/en-us/training/achievements/dax-power-bi-write-formulas.svg"

# Content pour faciliter la recherche
title: Écrire des formules DAX pour des modèles sémantiques
intro: Créer des calculs, d’ajouter une logique et d’améliorer l’analyse des données dans vos états et vos modèles sémantiques.
type: Cours
topics:
    - data
    - Microsoft DAX

# Information
author: RICHARD Wilfried
featuredLinks:
    - prev:
    - next:
    - mid:
    - exp:
    - ofi: https://learn.microsoft.com/fr-fr/training/modules/dax-power-bi-write-formulas/
changelog:
    - 2026-05-29 : Creation du cours
---

# Formules DAX

DAX (*Data Analysis Expressions*) constitue le langage de calcul du moteur tabulaire Power BI.
Il permet la création de tables calculées, colonnes calculées et mesures, enrichissant le modèle sémantique par des opérations analytiques avancées.
DAX étend la logique métier, structure les agrégations, modifie le contexte d’évaluation et permet la construction d’indicateurs complexes.

## 1. Types de calculs DAX

### 1.1. Configurer des relations

Les [relations](https://learn.microsoft.com/fr-fr/power-bi/transform-model/desktop-relationships-understand) assurent la propagation des filtres entre tables.
Elles déterminent la cohérence analytique du modèle et conditionnent la validité des agrégations.

1. **Clés composites** : Chaque relation repose sur une colonne *De* et une colonne *À* via Power Query;
    * types de données identiques
    * valeurs correspondantes
    * unicité garantie pour le côté « un ».
1. **Direction** : Détermine la propagation des filtres ; sens unique de la table dimention au table des fait,
  Les relations bidirectionnelles sont justifiées dans les scénarios M:M nécessitant une table de pontage.
1. **Cardinalité** : granularités différentes ou absence d’unicité ; **1:1** doit etre remplacé par une fusion
1. **Relations inactives** : Les relations supplémentaires doivent être inactives et activées via `USERELATIONSHIP()` dans DAX.
1. **Tables de dates** : La fonctionnalité *Date/heure automatique* doit être désactivée ;
    * comporter une colonne de dates unique
    * être contiguë
    * être marquée comme table de dates.
1. Réduire la cardinalité
    * limiter les relations complexes,
    * supprimer les colonnes inutiles,
    * convertir les dates/heures en dates seules,
    * regrouper les valeurs (binning),
    * remplacer les identifiants GUID par des entiers,

Recommandation : créer des mesures et masquer les colonnes numériques.

### 1.2. Configurer des hiérarchies

Les hiérarchies structurent la navigation analytique (ex. Année → Trimestre → Mois).
Elles facilitent l’exploration sans nécessiter de connaissance technique.
Elles peuvent être masquées, documentées et organisées comme les colonnes.

### 1.3. Tables calculées

toujours importées dans le modèle (augmentation de la taille et du temps d’actualisation) ; `Due Table`,

* **tables de dates** (CALENDAR, CALENDARAUTO),
* **dimensions de rôle actif** : duplication pour gérer plusieurs relations entre les tables (filtre) ; `Ship Table = 'Table'`
* **analyse de scénarios** (paramètres → tables déconnectées).

Configurer des tables

* **Nom** : convivial, unique, aligné sur la terminologie métier.
* **Description** : documentation interne pour les auteurs de rapports.
* **Synonymes** : améliore Questions & Réponses et Copilot.
* **Masquage** : utile pour les tables techniques (ponts, tables de rôle, etc.).

### 1.4. Colonnes calculées

Expressions évaluées ligne par ligne utilisées pour enrichir les attributs ; stockées dans source,

Utiliser uniquement lorsque la colonne doit être utilisée pour filtrer, trier ou segmenter.

Chaque ligne est évaluée indépendamment.
Pour accéder à d’autres tables :

* `RELATED()` → côté *un*
* `RELATEDTABLE()` → côté *plusieurs*
* `LOOKUPVALUE()` → en absence de relation

Configurer des colonnes

1. Propriétés générales : nom, description, synonymes, masquage, d’affichage.
1. Type de données : Hérité de Power Query, Toute modification dans Desktop ajoute une étape M, Le type conditionne les relations, les hiérarchies et les calculs.
1. Format : Détermine l’affichage (devise, pourcentage, date, etc.).
1. Tri par colonne  : Permet de corriger les tris non naturels (ex. mois alphabétiques).
Exige une colonne numérique ou ordinale dédiée.
1. Catégorie de données : Permet de géocoder (latitude/longitude, ville, pays) ou d’afficher des URL (web ou image).
1. Résumer par : Définit l’agrégation par défaut (SUM, MIN, MAX, AVERAGE, COUNT, NONE).

### 1.5. Mesures

Expressions évaluées au moment de la requête essentielles pour les agrégations complexes ; **jamais stockées** & dépendent du contexte de filtre,

* **mesures explicites** : écrites en DAX,
* **mesures implicites** : agrégations automatiques des colonnes (∑).

## 2. Écrire des formules DAX

Toute [expression](https://learn.microsoft.com/en-us/dax/dax-function-reference) suit la structure : `<Nom> = <Formule DAX>`
Un excellent outil de mise en forme d’une autre source qui peut vous aider à mettre en forme vos calculs est [DAX Formatter](http://www.daxformatter.com/).

1. Références aux objets du modèle
    * `Table` (guillemets obligatoires si espace ou mot réservé).
    * `Table[Colonne]` : toujours utiliser le nom complet pour lever l’ambiguïté.
    * `[Mesure]` : ne jamais préfixer par le nom de table.
1. Variables DAX : Permettent d’[améliorer](https://learn.microsoft.com/fr-fr/dax/best-practices/dax-variables) la lisibilité & performances
1. Types de données DAX gère : des types scalaires & [BLANK](https://learn.microsoft.com/fr-fr/dax/blank-function-dax/) est distinct de zéro et doit être traité explicitement (ISBLANK).
1. Utiliser des fonctions DAX comprend : fonctions Excel (SUM, IF, LEFT, YEAR…) & * fonctions spécifiques au moteur tabulaire
1. Fonctions spécifiques à DAX : DISTINCTCOUNT() & DIVIDE()
1. Utiliser des opérateurs DAX**
    * Arithmétiques : `+`, `-`, `*`, `/`, `^`
    * Comparaison : `=`, `==`, `<`, `>`, `<=`, `>=`, `<>`
    * Concaténation : `&` pour assembler du texte.
    * Logiques : `&&`, `||`, `NOT`, `IN`

## 3. Modifier le contexte de filtre DAX

Le contexte de filtre constitue le mécanisme fondamental du moteur tabulaire.
Il détermine quelles lignes d’un modèle sont visibles lors de l’évaluation d’une mesure.
La maîtrise de ce concept permet de contrôler la granularité analytique, de produire des ratios, des comparatifs et des indicateurs avancés.

Le contexte de filtre correspond à l’ensemble des filtres actifs lors de l’évaluation d’une mesure.
Il provient de :

* filtres explicites (volet Filtres, segments, interactions),
* filtres implicites (regroupements dans les visuels),
* propagation via les relations du modèle.

Les `tables calculées` et `colonnes calculées` ne sont pas évaluées dans le contexte de filtre mais dans le **contexte de ligne**.

`CALCULATE(<expression>, <filter1>, …)` est la fonction centrale de modification du contexte de filtre.
Elle permet :

* d’ajouter des filtres,
* de remplacer des filtres existants,
* d’utiliser des modificateurs de filtre,
* de transférer le contexte de ligne vers le contexte de filtre.

Les filtres transmis peuvent être :

* **booléens** : `'Product'[Color] IN {"Red", "Blue"}` ou `'Product'[List Price] > 1000`
* **tables** : `FILTER('Product', condition)` ou `KEEPFILTERS()` lorsque possible
* **modificateurs** : Utilisé pour calculer des totaux globaux, des ratios, des pourcentages ; `REMOVEFILTERS`, `KEEPFILTERS`, `USERELATIONSHIP`, `CROSSFILTER`

En interne, Power BI convertit **tous** les filtres booléens en filtres de table.

Lorsqu’une mesure est utilisée dans une colonne calculée ou un itérateur, elle doit transférer le contexte de ligne vers le contexte de filtre.

## 4. Fonctions Time Intelligence

Les [fonctions](https://learn.microsoft.com/fr-fr/power-bi/transform-model/desktop-auto-date-time) *Time Intelligence* constituent l’ensemble des mécanismes DAX permettant de modifier le contexte de filtre temporel.

Le Time Intelligence désigne la modification du contexte de filtre appliqué aux dates afin de produire des calculs temporels.

Les fonctions Time Intelligence nécessitent une [table de dates marquée](https://learn.microsoft.com/fr-fr/power-bi/guidance/model-date-tables/).

1. LASTDATE / LASTNONBLANK : Renvoie la dernière date du contexte.
1. DATESYTD / DATESQTD / DATESMTD : Renvoient les dates depuis le début de l’année, du trimestre ou du mois.
1. TOTALYTD / TOTALQTD / TOTALMTD : Évaluent une expression sur l’intervalle cumulé.
1. DATESBETWEEN : Renvoie les dates entre deux bornes.
1. DATESINPERIOD : Renvoie un intervalle glissant (ex. 30 jours, 12 mois).
1. SAMEPERIODLASTYEAR : Décale d’un an en arrière.
1. DATEADD : Décale d’un nombre d’intervalles (mois, trimestres, années).
1. PARALLELPERIOD : Renvoie une période parallèle (ex. même trimestre année précédente).
1. `NEXTDAY`, `NEXTMONTH`, `NEXTQUARTER`, `NEXTYEAR`
1. `PREVIOUSDAY`, `PREVIOUSMONTH`, `PREVIOUSQUARTER`, `PREVIOUSYEAR`

Calculs temporels avancés

1. Variation annuelle (YoY)

```dax
Revenue YoY % =
VAR RevenuePriorYear =
    CALCULATE([Revenue], SAMEPERIODLASTYEAR('Date'[Date]))
RETURN
    DIVIDE([Revenue] - RevenuePriorYear, RevenuePriorYear)
```

1. Comptage des nouvelles occurrences

```dax
New Customers =
VAR CustomersLTD = //Clients distincts à date
  CALCULATE(
    DISTINCTCOUNT(Sales[CustomerKey]),
    DATESBETWEEN('Date'[Date], BLANK(), MAX('Date'[Date])),
    'Sales Order'[Channel] = "Internet"
  )
VAR CustomersPrior =
  CALCULATE(
    DISTINCTCOUNT(Sales[CustomerKey]),
    DATESBETWEEN('Date'[Date], BLANK(), MIN('Date'[Date]) - 1),
    'Sales Order'[Channel] = "Internet"
  )
RETURN
    CustomersLTD - CustomersPrior
```

## 5. Créer des calculs visuels

Les calculs visuels constituent une extension du langage DAX appliquée **directement au visuel**, et non au modèle sémantique.

Ils permettent de [produire](https://learn.microsoft.com/fr-fr/power-bi/transform-model/desktop-visual-calculations-overview) des calculs dynamiques, simplifiés, performants et contextualisés, sans modifier la structure du modèle ni ajouter de mesures persistantes.
Ils se distinguent des mesures par :

* **leur portée** : stockés dans le visuel, non dans le modèle,
* **leur dépendance** : ne peuvent référencer que les champs présents dans le visuel,
* **leur granularité** : évalués ligne par ligne (comme une colonne calculée),
* **leur performance** : opérant sur des données agrégées, ils réduisent la charge du moteur tabulaire.

### 5.1. Créer un calcul visuel

La création s’effectue via *Nouveau calcul* dans un visuel sélectionné.
L’interface comporte :

1. **Aperçu du visuel**
2. **Barre de formule**
3. **Matrice visuelle** (zone d’évaluation interne)

Il permet d'évalué ligne par ligne, sans agrégations explicites.

Les champs utilisés par les calculs visuels peuvent être masqués du visuel final tout en restant disponibles dans la matrice visuelle interne.

Power BI propose des [modèles préconfigurés](https://learn.microsoft.com/fr-fr/power-bi/transform-model/desktop-visual-calculations-overview#available-functions)

Des fonctions spécifiques aux calculs visuels (fonctions de fenêtre simplifiées), **à l’exclusion** des fonctions dépendant du modèle :

* `USERELATIONSHIP`,
* `RELATED`,
* `RELATEDTABLE`,
* fonctions nécessitant la navigation relationnelle.

### 5.2. Paramètres des calculs visuels

Les calculs visuels introduisent deux [paramètres](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-visual-elements-for-reports) structurants :

1. Paramètre `Axis` : Définit la direction d’évaluation dans la matrice visuelle.
    * **ROWS** : Parcours vertical (haut → bas)
    * **COLUMNS** : Parcours horizontal (gauche → droite)
    * **ROWS COLUMNS** : Lignes puis colonnes
    * **COLUMNS ROWS** : Colonnes puis lignes
1. Paramètre `Reset` : Définit quand réinitialiser l’agrégation.
    * **AUCUN** : Pas de réinitialisation
    * **HIGHESTPARENT** : Réinitialisation au changement du parent le plus haut
    * **LOWESTPARENT** : Réinitialisation au changement du parent le plus bas
    * **Valeur numérique** : Réinitialisation à un niveau hiérarchique spécifique

Axe : Year → Quarter → Month

* `RUNNINGSUM([Sales Amount], HIGHESTPARENT)` → redémarre chaque année
* `RUNNINGSUM([Sales Amount], LOWESTPARENT)` → redémarre chaque trimestre
* `RUNNINGSUM([Sales Amount])` → jamais réinitialisé

S’il n’y a qu’un seul niveau sur l’axe, vous pouvez utiliser PARTITIONBY.
