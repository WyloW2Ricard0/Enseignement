# TECHNIQUE — ANALYTIQUE AVANCÉE

Réduire la donnée brute en structures interprétables (tendances, clusters, anomalies, distributions).

Il faut isoler les plus performent et les moins performent pour exercer vos analyse.

## 1. Distribution

Analyse par segmentation des dimentions

Le module [Grouping & Binning](https://learn.microsoft.com/en-us/training/modules/perform-analytics-power-bi/4-group-data) permet de reprendre le contrôle sur cette segmentation en imposant des catégories artificielles ou des intervalles réguliers ; stabiliser la structure, révéler des patterns, réduire la cardinalité, préparer l’analyse avancée.

La fonctionnalité [Analyser](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-insights-find-where-different) exécute une analyse pour une catégorie spécifique.
Elle génère des explications statistiques et des variations significatives paraport au total.
Elle sert à comprendre pourquoi une valeur augmente, diminue ou diverge de la distribution attendue.

## 2. dispersion

Identification des zones de densité

Le [clustering](https://learn.microsoft.com/en-us/training/modules/perform-analytics-power-bi/5-clustering-techniques) est un algorithme de segmentation non supervisée qui regroupe des points présentant des attributs similaires et les isole du reste des données. Power BI exécute cette analyse directement sur le modèle sémantique, détectant les proximités et séparant les sous‑ensembles cohérents appelés clusters.

## 3. Tendance

L’analyse de séries temporelles consiste à modéliser l’évolution d’une variable dans le temps, détecter les tendances, identifier les événements perturbateurs, et produire des prévisions opérationnelles. Elle constitue la base analytique la plus fiable pour anticiper les activités futures.

* Line chart : trajectoire, tendance, rupture.
* Area chart : densité temporelle, volume cumulé.
* Scatter chart : évolution multi‑dimensionnelle.
* Gantt : planification séquentielle.
* Stock charts : volatilité, mouvements boursiers.

Le visuel [Play Axis](https://learn.microsoft.com/en-us/training/modules/perform-analytics-power-bi/6-time-series-analysis) agit comme un trancheur dynamique animé

## 5. Extrêmes

Une valeur aberrante est un point de rupture statistique : un élément qui diverge significativement du comportement moyen ou attendu.
Elle signale une possible anomalie opérationnelle, un événement isolé ou un changement structurel dans les données.

L’objectif est d’identifier où, quand et pourquoi un point s’écarte du cluster principal.

Le diagramme de dispersion est le visuel optimal pour détecter les outliers.
Il projette deux mesures sur un plan X/Y et révèle ; Clusters naturels, Points isolés, Relations non linéaires.

Analyse des causes racines et prendre (ou pas) des décisions correctives.

Création d’une mesure pour isole les points dépassant un seuil dynamiquement les données sans recalcul statique.

## 6. Fonction Systémique

1. paramètre What‑If est un contrôleur numérique injecté dans le modèle sémantique, permettant de simuler des scénarios, moduler des mesures et projeter des résultats futurs.
Il agit comme une variable d’entrée manipulable par l’utilisateur, reliée à une mesure dérivée qui réagit instantanément.
Objectif : tester des hypothèses, projeter des impacts, modéliser des variations.
1. [Influenceurs Clés](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-influencers?tabs=powerbi-desktop) calcule les facteurs explicatifs d’une mesure cible (ex : revenu, probabilité de gain) pour isoler les sous‑populations contributives.
1. [Arbre de Décomposition](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-decomposition-tree) : Exploration Multi‑Dimensionnelle libre dans n’importe quel ordre.
