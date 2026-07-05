---
# Variable
showMiniToc: true
permissions: true
effectiveDate: 2026-05-30
image: "https://learn.microsoft.com/en-us/training/achievements/power-bi-effective.svg"

# Content pour faciliter la recherche
title: Rapports efficaces de conception dans Power BI
intro: Utilisez des techniques de visualisation des données qui engagent les utilisateurs, mettent en lumière les principales conclusions et aident à orienter les décisions basées sur les données.
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
    - ofi: https://learn.microsoft.com/fr-fr/training/modules/power-bi-visual-calculations/
changelog:
    - 2026-05-29 : Creation du cours
---

# Conception d’un rapport Power BI

L’objectif est de **définir correctement le périmètre d’un rapport** avant sa création : public, objectifs, type de rapport, exigences UI/UX.

## 1. Structure d’un rapport

Sur chaque page, les objets de rapport sont disposés, avec la visualisation d'un unique modeles sementique

![report-structure.png](https://learn.microsoft.com/en-us/training/modules/power-bi-effective-reports/media/1-1-report-structure.png)

Elle doit conduire l’esprit du lecteur du global vers le détaillé car *le savoir qui se dévoile seulement à celui qui cherche*.

1. Exécutifs
    - Besoin : vision synthétique, KPI, tendances.
    - Usage : rapide, mobile, décision stratégique.
    - Répond à : *“Comment allons‑nous ?”*
1. Analystes
    - Besoin : explorer, comprendre, diagnostiquer, [anomalie](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-anomaly-detection).
    - Usage : interactions avancées, filtres, drill-down.
    - Répond à : *“Pourquoi cela s’est‑il produit ?”*
1. Travailleurs de l’information
    - Besoin : données opérationnelles à jour.
    - Usage : actions quotidiennes, décisions immédiates.
    - Répond à : *“Que dois‑je faire maintenant ?”*
1. Public général
    - Besoin : comprendre un sujet non maîtrisé.
    - Usage : Narration, explications, guidage.
    - Répond à : *“Comment comprendre ce sujet ?”*

Les pages ne peut être ni sécurisée ni publiée indépendamment, seul le rapport porte la charge du dévoilement : séparer les pages en rapports distincts lorsque les **publics divergent**, lorsque les **règles de partage**, de sécurité ou de diffusion ne peuvent cohabiter.

## 2. Exigences de l’interface utilisateur (UI)

Alignement avec la charte graphique de couleurs contrastée pour une Cohérence visuelle sans oublier Texte alternatif pour visuels.

Chaque page est un plan, chaque visuel une manifestation, chaque élément une intention.
Le rapport n’est pas un assemblage : c’est une architecture mentale.

Soit avec height $=720$ px & Width $=1280$ px

1. **Placement** : Le savoir se révèle du coin supérieur directeur et descend en flux.
    - *règle des tiers* pour un poids uniforme
    - *suite de Fibonacci* pour la tension maîtrisée ; $\varphi=\frac{1+\sqrt{5}}{2}=1.618$
    - Profondeur : variations d’espace pour séparer les sections, sans excès.
    - Alignement : présentes sur le ruban Format
1. **Proximité** : *Ce qui est proche est lié. Ce qui est séparé est autre. Loi de Proximité (Gestalt)*
    - Marges de part et d'autre du bord long : Dessiner la plus grande suite de fibonacci ; $m_{w}=\frac{1}{2}|h-\frac{w}{\varphi}|=36$ px
    - Marges de part et d'autre du bord court : Cadre de meme ratio du canevas ; $m_{h}=\frac{w}{2}(1-\frac{w}{\varphi\cdot h})=63$ px
    - Espacement : distance contrôlée entre les objets pour éviter chevauchements et interférences (notamment des en‑têtes visuels) ; $e=\frac{m_w+m_h}{4}=25$ px
    - Padding interne : $p=e/2=12$ px
1. **Contraste** : *La différence éclaire*. Couleurs, tailles, formes : tout sert à désigner l’essentiel.
    - Palette douce = neutralité analytique.
    - Couleurs vives = exceptions, signaux.
    - Contraste obligatoire pour l’accessibilité (éviter jaune + labels blancs) .
1. **Répétition** : Le motif crée la doctrine.
    - Uniformité chromatique = cohérence perceptive.
    - Polices, tailles, poids, couleurs, espacements : un seul canon.
    - Activer un [thème](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes/) pour imposer la doctrine visuelle à l’ensemble du rapport .
    - Limiter les overrides (HEX manuels) pour préserver l’intégrité du thème.
    - Exporter le thème (JSON) pour propager la norme.

Vous pouvez utiliser un site externe comme [powerbi.tips](https://powerbi.tips/)

## 3. Exigences de l’expérience utilisateur (UX)

minimiser la charge cognitive et maximiser la profondeur exploratoire.

1. Interactivité
    - Drill-down / drill-up.
    - [Drillthrough](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-drillthrough).
    - Navigation entre pages.
    - Filtres, slicers, boutons.
1. Accès flexible aux données
    - Export Excel/CSV.
    - [Q&R](https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-q-and-a) (langage naturel).
    - [Alertes](https://learn.microsoft.com/fr-fr/power-bi/create-reports/service-set-data-alerts) (dans les dashboards).
    - Liens externes, actions.
    - [Infobulles](https://learn.microsoft.com/en-us/power-bi/guidance/report-page-tooltips)
1. Analyse & scénarios
    - Paramètres hypothétiques (What-if).
    - Mise en page [imprimable](https://learn.microsoft.com/en-us/power-bi/visuals/paginated-report-visual).
    - Comparaison de scénarios.
1. Collaboration & automatisation
    - [Capture la visibilité des objets de rapport](https://learn.microsoft.com/en-us/training/modules/power-bi-effective-user-experience/4-bookmarks)
    - [Abonnements email](https://learn.microsoft.com/fr-fr/power-bi/collaborate-share/end-user-subscribe).
    - [Commentaires intégrés](https://learn.microsoft.com/fr-fr/power-bi/explore-reports/end-user-comment).
    - [Partage et discussions](https://learn.microsoft.com/fr-fr/power-bi/collaborate-share/service-share-dashboards).

## 4. Pipeline de [configuration](https://learn.microsoft.com/en-us/training/modules/power-bi-effective-reports/4-report-objects)

1. [Instanciation](https://learn.microsoft.com/en-us/power-bi/consumer/end-user-visual-type/) (sélection du type)
1. Allocation des champs → wells (structure variable selon le visuel)
1. Application de filtres locaux
1. Paramétrage des agrégations / renommages / “Show items with no data”
1. Définition du tri
1. Stylisation (Format)
1. Surcouches [analytiques](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-analytics-pane) (min/max lines, forecast, anomaly detection)

## 5. Techniques de [filtrage](https://learn.microsoft.com/en-us/training/modules/power-bi-effective-reports/6-report-filters)

Le filtrage opère sur 5 couches hiérarchiques :

![structure-filters.png](https://learn.microsoft.com/en-us/training/modules/power-bi-effective-reports/media/7-1-report-structure-filters.png)

- RLS + filtres = risque de BLANK total pour certains utilisateurs.
- Les filtres relatifs dépendent de l’horloge système.
- Les filtres de mesure peuvent éliminer des groupes entiers → attention aux interprétations.
- Utiliser des boutons pour masquer/afficher les filtres

Un slicer est un visuel dont la seule fonction est de propager un filtre vers les autres visuels.

- Utiliser les segments synchronisés entre pages
- Désactivation des filtres persistants
- déroulants interrogent le modèle uniquement à l’ouverture → accélération du rendu.
- Sélection simple = utile pour scénarios exclusifs (ex : Réel / Budget / Forecast).
- Limiter le nombre de slicers
- Préférer les slicers hiérarchiques

Transformer chaque visuel en contrôleur de contexte vers tous les visuels de la page.
Multi‑sélection additive via Ctrl.

## 6. Taxonomie des visuels

1. Classe catégorielle : comparer des mesures entre modalités **discrètes**. *Tri par valeur (desc) sauf ordre métier imposé.*
    - Barre/Colonne groupée : axe = dimension, hauteur = mesure.
    - Ribbon chart : suivi de **rangs** dans le temps (hybride catégoriel/temporel).
1. Classe temporelle : séries chronologiques, dynamique dans le temps.
    - Courbe (Line chart) : axe X = temps **continu**, tri chronologique strict. *Idéal si pas de trous de série.*
    - Colonne temporelle : préférable si valeurs **manquante** (visualise les « gaps »).
    - Aire / Line & Column : même logique, pour mettre l’accent sur **volume cumulé** ou double métrique.
    - Analytique intégré : bandes de **prévision**, lignes min/max, anomalies.
1. Classe proportionnelle : part d’un total, distribution relative. *éviter la surcharge de légende pour fortes cardinalités.*
    - Barre/Colonne 100 % empilée : **comparaison de structure** entre groupes.
    - Treemap : hiérarchie de parts, surface ∝ valeur.
    - Funnel : décroissance séquentielle (pipeline).
    - Pie/Doughnut : à réserver à faible cardinalité, valeurs toutes positives.
1. Classe numérique (indicateurs) : mise en avant de KPI **scalaires**.
    - Carte simple (Card) : valeur unique, lecture immédiate.
    - Carte multi‑lignes : petit ensemble de KPI homogènes.
    - Gauge / KPI : valeur vs cible, tendance.
1. Classe géospatiale : ancrage spatial des mesures.
    - Map / Filled map : coordonnées ou catégories géographiques (pays, région, ville).
    - Bubble map : taille/couleur ∝ mesure.
    - Considérations : géocodage fiable, projection cohérente, éviter surcharge de points.
1. Classe grille (tableau) : lecture **détaillée**, inspection tabulaire avec mise en forme conditionnelle.
    - Table : granularité fine, tri multi‑colonnes, export.
    - Matrix : grille croisée (lignes/colonnes hiérarchiques), sous‑totaux, drill‑down.
    - Usage : complément analytique, pas visuel principal pour synthèse.
