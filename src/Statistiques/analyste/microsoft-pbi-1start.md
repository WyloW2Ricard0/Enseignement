---
# Variable
showMiniToc: true
permissions: true
effectiveDate: 2026-05-28
image: "https://learn.microsoft.com/en-us/training/achievements/get-started-power-bi.svg"

# Content pour faciliter la recherche
title: Commencer à créer avec Power BI
intro: Découvrez Power BI, les composants et le flux de Power BI, et comment créer des rapports interactifs et attrayants.
type: Cour
topics:
    - Analyste
    - Microsoft PBI

# Information
author: RICHARD Wilfried
featuredLinks:
    - prev:
    - next:
    - mid:
    - exp:
    - ofi: https://learn.microsoft.com/fr-fr/training/modules/get-started-with-power-bi/
changelog:
    - 2026-05-28 : Creation du cours
---

# Commencer avec Power BI

*Power BI s’inscrit dans la continuité des infrastructures décisionnelles apparues à la fin des années 1980 (Inmon, Kimball), lorsque les premiers entrepôts de données ont structuré l’accès analytique aux organisations.*

Il constitue un environnement low-code de modélisation, de transformation et de diffusion des artefacts analytiques sur un `canevas`, mais *"l’outil n’est rien sans la méthode"*.

## 1. Chaîne opératoire structurée

Intégrant un moteur tabulaire sur les modèles relationnels, *téléchargeable gratuitement par [Windows Store](https://apps.microsoft.com/detail/9ntxr16hnw1t?hl=fr-FR&gl=NL).

Cette séquence reprend la logique des pipelines ETL/ELT *formalisés dans les années 1990* pour ecrire les `Rapports`.

1. `Connexion aux données` : Multiplicité des sources, hétérogénéité structurelle.
2. `Préparation` (Power Query) : Héritage direct des langages de manipulation de données (SQL 1974, M moderne).
3. `Modélisation sémantique` : Relations, mesures DAX, hiérarchies pour créer un modèle tabulaire optimisé pour l’agrégation.
4. `Visualisation` : Interactivité, filtres, drill-down *"conformément aux principes de réduction cognitive de Tufte (1983)"*.
5. `Distribution` : Logique de gouvernance et de versioning. qui régis le contenu à inclure (limité à l’espace de travail actuel), puis votre public.

Au lieu de créer et gérer des états distincts pour chaque département, vous pouvez utiliser la [Sécurité au niveau des lignes](https://learn.microsoft.com/fr-fr/fabric/security/service-admin-row-level-security) (SNL) dans Power BI, garantissant que les utilisateurs ne voient que les données pertinentes pour leur rôle.

* La méthode [statique](https://learn.microsoft.com/fr-fr/training/modules/row-level-security-power-bi/2-static-method) dans la SNL utilise une valeur fixe dans le filtre DAX,
* la méthode [dynamique](https://learn.microsoft.com/fr-fr/training/modules/row-level-security-power-bi/3-dynamic-method) utilise une fonction DAX.
* Lorsque votre modèle de données comporte des tables DirectQuery et que leur source de données prend en charge la SSO, la [source de données](https://learn.microsoft.com/fr-fr/power-bi/connect-data/service-azure-sql-database-with-direct-connect#single-sign-on) peut appliquer des autorisations de données.

La [sécurité au niveau objet](https://learn.microsoft.com/fr-fr/analysis-services/tabular-models/object-level-security?view=sql-analysis-services-2025) (SNO) permet de limiter l’accès à des tables et colonnes spécifiques, ainsi qu’à leurs métadonnées.
En général, vous appliquez la SNO aux objets sécurisés qui stockent des données sensibles, comme les données personnelles des collaborateurs.

## 2. Service Power BI

[centraliser](https://learn.microsoft.com/en-us/training/modules/manage-workspaces-power-bi-service/), gouverner et distribuer les artefacts analytiques (rapports + modèle sémantique) via une plateforme SaaS.
Effet : versioning unique, rafraîchissement orchestré, contrôle d’accès, packaging en applications.

![power-bi-service.png](https://learn.microsoft.com/en-us/training/modules/manage-workspaces-power-bi-service/media/2-power-bi-service.png)

1. `Applications` : Elles constituent des `collection d’états` décisionnels stabilisés.
1. [Applications modèles](https://learn.microsoft.com/fr-fr/power-bi/explore-reports/end-user-apps) : Solutions templates *(2010)* avec un minimum d’effort. (Pour accéder ; Obtenir des applications > Applications modèles)

Power BI propose plusieurs exemples chargés dans `Mon espace de travail`. Vous pouvez accéder aux exemples de rapports dans la section `Learn` du volet de navigation.

### 2.1. Espaces de travail

Selon les logiques de segmentation **organisationnelle**. `Mon espace de travail` est idéal uniquement à des fins de tests
Il existe deux types d’espaces de [travail](https://learn.microsoft.com/en-us/training/modules/manage-workspaces-power-bi-service/3-understand-workspaces) :

* Mon espace de travail, qui est privé à chaque utilisateur,
* espaces de travail partagés, accessibles par plusieurs utilisateurs ayant des rôles assignés

Les [Role](https://learn.microsoft.com/fr-fr/power-bi/collaborate-share/service-roles-new-workspaces) déterminent le niveau d’accès et les autorisations dont dispose un utilisateur au sein d’un espace de travail.

Si souhaitez [ajouter](https://learn.microsoft.com/en-us/training/modules/manage-workspaces-power-bi-service/4-explore-publishing-process) un rapport à l’espace de travail.
Vous pouvez télécharger un rapport Power BI (fichier .pbik) directement dans l’espace de travail.
Si vous utilisez l’option cloud, le service Power BI peut automatiquement synchroniser ces modifications environ toutes les heures.

le partage au `item-level` vous permet de **partager** des rapports ou tableaux de bord **spécifiques** avec des individus ou groupes sélectionnés.

L’application d’`étiquettes` de sensibilité dans Power BI est une étape clé pour garantir que les données sensibles soient correctement classées et protégées tout au long de leur cycle de vie.
naviguez vers l'artefact, Utilisez le menu « Plus d’options » pour accéder  la liste déroulante sous la section « Étiquette de sensibilité »

[S’abonner](https://learn.microsoft.com/fr-fr/power-bi/collaborate-share/end-user-subscribe?tabs=creator) à un rapport ou tableau de bord permet aux utilisateurs de rester informés des données et des insights critiques sans avoir à vérifier manuellement les mises à jour.
De plus dans *Premium capacity*, les abonnements peuvent inclure une image d’aperçu, un lien vers le rapport ou le tableau de bord, et même des pièces jointes.
Dans Power BI Service, allez au rapport ou au tableau de bord et sélectionnez l’option S’abonner dans la barre de menu.

### 2.2. Modèle sémantique

Constitue la couche conceptuelle qui structure les données préparées via Power Query.
Il organise les artefact afin de produire un environnement analytique cohérent, performant et intuitif.
L’objectif est de fournir une représentation logique stable, optimisée pour les requêtes analytiques et adaptée aux exigences de reporting.

Une gestion efficace des modèles sémantiques est cruciale pour la performance organisationnelle.
Lorsque vos modèles sémantiques sont publiés, toute personne ayant besoin d’accéder au modèles sémantiques peut les trouver dans un emplacement central.

Automatiser les processus de [rafraîchissement](https://learn.microsoft.com/fr-fr/power-bi/connect-data/refresh-data#configure-scheduled-refresh) garantit aux utilisateurs des données toujours à jour, *"Une donnée non actualisée est une donnée fausse."*

* La fonction de [rafraîchissement programmé](https://learn.microsoft.com/en-us/training/modules/manage-datasets-power-bi/5-dataset-refresh), permet de définir la fréquence et les créneaux temporels pour actualiser un jeu de **données** particulier pour garantit aux utilisateurs des données toujours à jour.
* La fonction de [rafraîchissement incrémental](https://learn.microsoft.com/en-us/training/modules/manage-datasets-power-bi/6-incremental-refresh), vous permet de rafraîchir rapidement et aussi souvent que nécessaire, sans avoir à recharger les données historiques à chaque fois.
Le rafraîchissement incrémental ne doit être utilisé que sur les sources de données et les requêtes qui supportent le `pliage` des requêtes a l'aide des parametres manuel `RangeStart` & `RangeEnd`.

[Promouvoir](https://learn.microsoft.com/fr-fr/power-bi/collaborate-share/service-endorse-content) des modèles clés aide les utilisateurs à identifier les meilleures options pour reduire les efforts car un modèle sémantique peut être utilisé pour différentes raisons commerciales.
La `certification`, en revanche, signifie que le contenu respecte les normes de qualité de l’organisation et est considéré comme faisant autorité.

### 2.3 Audience

vous permettent d’adapter la visibilité et l’accès au contenu pour différents groupes d’utilisateurs défini manuelement au sein de votre organisation, en veillant à ce que les utilisateurs ne voient que les données pertinentes à leurs rôles ou responsabilités.

Au lieu de créer plusieurs applications ou espaces de travail pour différentes équipes, vous pouvez gérer tout le contenu au sein d’une seule application et contrôler la visibilité au niveau de l’audience.

1. **Créer un groupe** : Dans l’onglet *Audience*, lors de la création ou de la modification de l’application, sélectionnez Nouvelle audience et nommez le groupe.
1. **Personnalisez la visibilité** : Utilisez les icônes masquer/montrer à côté de chaque élément dans l’espace de travail pour déterminer quel contenu est visible pour le public.
1. **Assigner des groupes** : Dans le volet *Gérer* l’accès de l’audience, spécifiez les utilisateurs ou groupes qui doivent appartenir à l’audience.
1. **Publiez l’application** : Une fois les audiences et la visibilité de leur contenu configurées, publiez l’application.

Surveiller et suivre les indicateurs [d’utilisation](https://learn.microsoft.com/fr-fr/power-bi/collaborate-share/service-modern-usage-metrics) et les performances dans Power BI est essentiel pour comprendre comment vos rapports et tableaux de bord sont utilisés dans toute votre organisation.
En analysant les données d’utilisation, vous pouvez identifier quels rapports suscitent le plus d’engagement et lesquels peuvent nécessiter des mises à jour ou une promotion supplémentaire.

### 2.4 Tableau de bord

Cockpits industriels *(1950)* fixe, `Service PBI` permet de créer une unique page composée de `vignettes` pour acceder au PBI sous-jacent.
L’un des principaux avantages d’un [tableau de bord](https://learn.microsoft.com/fr-fr/power-bi/create-reports/service-dashboards) est la possibilité d’épingler un visuel provenant d’un modèle sémantique différent.

Lorsque vous apportez des modifications aux visuels de l’état, puis que vous les republiez dans le service Power BI, les modifications sont répercutées sur le tableau de bord.

Connectez-vous d’abord au service Power BI, puis accédez à un espace de travail avec des états. Ouvrez un état, puis cliquez sur l’icône Épingler le visuel dans l’en-tête visuel. Vous pouvez choisir d’épingler ce visuel à un tableau de bord nouveau ou existant. Après avoir épinglé vos visuels, vous pouvez les redimensionner et les déplacer en fonction de vos besoins.

Les [alertes](https://learn.microsoft.com/fr-fr/power-bi/create-reports/service-set-data-alerts) de données peuvent indiquer à vous-même ou à un utilisateur qu’un point de données spécifique est supérieur, inférieur ou égal à un seuil spécifique que vous pouvez définir ; carte & jauge.

## 3. Copilot pour Power BI

[Découvrez comment Activer Copilot pour Power BI.](https://learn.microsoft.com/fr-fr/fabric/fundamentals/copilot-enable-fabric)
Si vous ne voyez pas Copilot, vos administrateurs ne l’ont peut-être pas activé ou vous n’avez peut-être pas sélectionné de modèle sémantique.

Il opère exclusivement sur le `modèle sémantique` et ne modifie ni la `préparation` des données ni la `gouvernance`.

La qualité des données conditionne donc la validité des inférences générées par Copilot.

[Copilot](https://learn.microsoft.com/fr-fr/power-bi/create-reports/copilot-prompts-narratives) génère des pages d’état en exploitant la structure du modèle sémantique.

1. Mesure DAX : Copilot peut suggérer des mesures pertinentes en fonction des structures existantes.
Ces mesures ne deviennent persistantes qu’après intégration explicite dans le modèle.
1. génération de visuels et de pages,
1. Visuel Narration : génère un texte structuré référencé sur les visuels présents.
1. Résumé via le volet Copilot : Il peut produire un résumé global ou limité à la page active. Les résumés constituent une synthèse analytique destinée à stabiliser l’interprétation des visuels.
1. Invites personnalisées

Lorsque vous utilisez Copilot, vous devez considérer votre création comme votre première ébauche, qui nécessite votre examen avant de la finaliser.
