---
# Variable
showMiniToc: true
permissions: true
effectiveDate: 2025-12-19
image: "https://tommisaltiola.gallerycdn.vsassets.io/extensions/tommisaltiola/autofold-md-frontmatter/1.0.5/1710533937767/Microsoft.VisualStudio.Services.Icons.Default"

# Content pour faciliter la recherche
title: Frontmatter YAML dans Markdown
intro: Comment utiliser le frontmatter YAML dans les fichiers Markdown pour ajouter des metadonnees structurees
type: Tutorial
topics:
  - Markdown
  - YAML
  - Documentation

# Information
author: RICHARD Wilfried
changelog:
  - 2025-12-19 : Creation du guide sur le frontmatter YAML
---

# Frontmatter YAML dans Markdown

Le frontmatter YAML est un bloc de metadonnees place en haut d'un fichier Markdown, utilise pour configurer l'affichage, la navigation et le filtrage des articles sur des sites comme GitHub Docs.

Tout fichier Markdown contenant un bloc frontmatter YAML (entre trois tirets ---) est traite comme special par Jekyll.

**Conseils pratiques :**

- Le frontmatter peut être vide (utile pour les flux CSS/RSS).
- ***Attention au codage UTF-8*** : evitez le BOM en debut de fichier, surtout sous Windows.
- Pour ne pas repeter les mêmes variables.
- Les ***fichiers index.md doivent contenir la propriete children***.
- Pour **echapper une apostrophe**, utiliser deux apostrophes ('') ou des guillemets doubles.

## Mon choix actuel

```yaml
---
# Variable
showMiniToc: true # auto et pas dans text
permissions: true # parametre d'accessibilite hors de GitHub
effectiveDate: 2025-12-19 # date de creation
image: "https://tommisaltiola.gallerycdn.vsassets.io/extensions/tommisaltiola/autofold-md-frontmatter/1.0.5/1710533937767/Microsoft.VisualStudio.Services.Icons.Default" # lien web ver une image libre de droit correspondant

# Content pour faciliter la recherche
title: Titre acrocheur
intro: intro pour mettre en exert
type: categorie1 # type de fichier en un mot
topics: # max 3 tags
  - tags1
  - tags2
  - tags3

# Information
author: RICHARD Wilfried # dernier autheur
featuredLinks: # lien interne ver d'autre page
  - prev: # chemain ver la leson precedante
  - next: # chemain ver la lecon suivante
  - mid: # chemain le fichier qui peut aider
  - exp: # chemain ver un fichier exemple complet
  - ofi: # lien ver le site officiel
changelog: # pour mettre au couran l'utilisateur de la page d'une modification
  - 2025-01-04 : cour explication de la modification effectuer
---
```

**Conseils pratiques :**
- Le frontmatter peut être vide (utile pour les flux CSS/RSS).
- ***Attention au codage UTF-8*** : évitez le BOM en début de fichier, surtout sous Windows.
- Pour ne pas répéter les mêmes variables.
- Les ***fichiers index.md doivent contenir la propriété children***.
- Pour **échapper une apostrophe**, utiliser deux apostrophes ('') ou des guillemets doubles.

## Proprietes standard

Entre ces lignes, vous pouvez definir des variables predefinies (layout, title, permalink, published, date, category, tags) ou vos propres variables personnalisees, accessibles dans le contenu avec les balises Liquid (ex : {{ page.food }}).

```yaml
---
versions: # indique les versions auxquelles une page s’applique.
    fpt: '*' # GitHub Free, GitHub Pro ou GitHub Team
    ghec: '*' # GitHub Enterprise Cloud
    ghes: '3.x' # GitHub Enterprise Server
redirect_from: # Listez les URL qui doivent rediriger vers cette page.
    - /ancienne/url
title: Titre de la page
shortTitle: Titre abrege pour la navigation
intro: Introduction affichee
permissions: Definir la declaration d’autorisation pour l’article.
product: Definir la reference du produit pour l’article.
layout: components/landing # Afficher la mise en page correctequi correspond au nom de la disposition. Pour une disposition nommee (optionel).
children: # Liste les liens relatifs appartenant au sujet produit/categorie/carte.
    - /chemin/vers/article-enfant
childGroups: # Rendre les enfants en groupes sur la page d’accueil.
    - name: Groupe 1
        children:
            - /chemin/vers/article-enfant
featuredLinks: # Liste des liens populaires est celle affichee sur la page d’atterrissage sous le titre "Popular".
    popular:
        - /chemin/vers/article-populaire
showMiniToc: false # pour masquer la mini table des matières
allowTitleToDifferFromFilename: true # Pour autoriser un titre different du nom de fichier
changelog: # afficher une liste des elements extraits du journal des modifications de GitHub sur les pages d’accueil des produits
    label: Actions # doit être present et correspondre aux labels utilises dans le journal des modifications GitHub
    prefix: # chaîne optionnelle qui commence chaque titre du journal des modifications qui doit être omis dans le flux docs.
defaultPlatform: windows # Outrepasser la selection initiale de la plateforme d’une page (optionel).
defaultTool: cli # Annuler la selection initiale de l’outil pour une page (optionel).
learningTracks: # collection d’articles qui vous aident à maîtriser un sujet particulier.
  - parcours1
includeGuides: # Afficher une liste d’articles, filtrable par et . applicable uniquement lorsqu’elle est utilisee avec .type|topics|layout: product-guides
  - /chemin/vers/guide
journeyTracks: # Definir les parcours pour les pages d’atterrissage des voyages (prend en charge les variables liquides). Applicable uniquement lorsqu’elle est utilisee avec .layout: journey-landing
  - id: 'debuter' # Identifiant unique pour le voyage.
    title: 'Demarrer avec GitHub Actions' # afficher le titre du voyage
    description: # Description du parcours (optionnel)
    guides: # Ensemble d’objets-guides qui composent ce voyage.
      - href: '/actions/quickstart' # Chemin vers l’article
      - alternativeNextStep: # Texte personnalise pour guider les utilisateurs vers des chemins alternatifs dans le parcours. (optionnel)
type: tutorial #  Indiquer le type d’article.
topics: # Indiquer les sujets abordes par l’article (https://github.com/github/docs/blob/main/data/allowed-topics.ts).
  - github
communityRedirect: # Definir un lien personnalise et un nom de lien pour le lien dans le pied de page.
  name: Communaute
  href: https://github.community
  Object:
effectiveDate: 2025-12-19
---
```

### redirect_from

Pour gerer les redirections d’URL :

- Utilisez la propriete `redirect_from` dans le frontmatter YAML pour rediriger d’anciennes URLs vers la nouvelle page

- Pour des redirections plus complexes (par version ou vers une autre page), modifiez le fichier `redirect-exceptions.txt` dans le dossier `src/redirects`.

- Pour rediriger vers un site externe, ajoutez une entree dans `external-sites.json` :

```json
"/github-status": "https://www.githubstatus.com/",
"/articles/github-security": "https://github.com/security"
```

### children (page index)

La propriete `children` dans le frontmatter d’un fichier index.md liste les liens relatifs vers les pages enfants (articles, sous-categories, etc.).

**Important :** Seuls les chemins listes dans `children` seront accessibles sur le site. Tout fichier ou dossier non reference ici retournera une erreur 404.

### childGroups (page d'accueil)

La page d’accueil (index.md principal) doit contenir une liste complète de `children` et la propriete `childGroups` dans le frontmatter.

`childGroups` permet de regrouper les enfants par thème ou categorie sur la page d’accueil.
Chaque groupe possède un nom (name), eventuellement une icône (icon), et une liste de chemins enfants (children) qui doivent aussi figurer dans la propriete `children`.

***Il faut toujours la propriete children*** même si on utilise childGroups.
Cela garantit que tous les liens sont reconnus et accessibles sur le site.
