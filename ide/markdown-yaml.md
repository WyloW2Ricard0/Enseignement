---
versions: 1.0.0
effectiveDate: 2025-12-19
author: RICHARD Wilfried

title: Frontmatter YAML dans Markdown
excerpt: comment utiliser le frontmatter YAML dans les fichiers Markdown pour ajouter des métadonnées
type: tutorial
topics:
  - markdown
  - yaml
  - documentation
  - métadonnées
image: "https://tommisaltiola.gallerycdn.vsassets.io/extensions/tommisaltiola/autofold-md-frontmatter/1.0.5/1710533937767/Microsoft.VisualStudio.Services.Icons.Default"
---

# Frontmatter YAML dans Markdown

Le frontmatter YAML est un bloc de métadonnées placé en haut d'un fichier Markdown, utilisé pour configurer l'affichage, la navigation et le filtrage des articles sur des sites comme GitHub Docs.

Tout fichier Markdown contenant un bloc frontmatter YAML (entre trois tirets ---) est traité comme spécial par Jekyll.

Exemple minimal :
```yaml
---
layout: post
title: Mon premier blog
---
```

**Conseils pratiques :**
- Le frontmatter peut être vide (utile pour les flux CSS/RSS).
- ***Attention au codage UTF-8*** : évitez le BOM en début de fichier, surtout sous Windows.
- Pour ne pas répéter les mêmes variables.
- Les ***fichiers index.md doivent contenir la propriété children***.
- Pour **échapper une apostrophe**, utiliser deux apostrophes ('') ou des guillemets doubles.

## Principales propriétés du frontmatter

Entre ces lignes, vous pouvez définir des variables prédéfinies (layout, title, permalink, published, date, category, tags) ou vos propres variables personnalisées, accessibles dans le contenu avec les balises Liquid (ex : {{ page.food }}).

```yaml
---
versions: # indique les versions auxquelles une page s’applique.
    fpt: '*' # GitHub Free, GitHub Pro ou GitHub Team
    ghec: '*' # GitHub Enterprise Cloud
    ghes: '3.x' # GitHub Enterprise Server
redirect_from: # Listez les URL qui doivent rediriger vers cette page.
    - /ancienne/url
title: Titre de la page
shortTitle: Titre abrégé pour la navigation
intro: Introduction affichée
permissions: Définir la déclaration d’autorisation pour l’article.
product: Définir la référence du produit pour l’article.
layout: components/landing # Afficher la mise en page correctequi correspond au nom de la disposition. Pour une disposition nommée (optionel).
children: # Liste les liens relatifs appartenant au sujet produit/catégorie/carte.
    - /chemin/vers/article-enfant
childGroups: # Rendre les enfants en groupes sur la page d’accueil.
    - name: Groupe 1
        children:
            - /chemin/vers/article-enfant
featuredLinks: # Liste des liens populaires est celle affichée sur la page d’atterrissage sous le titre "Popular".
    popular:
        - /chemin/vers/article-populaire
showMiniToc: false # pour masquer la mini table des matières
allowTitleToDifferFromFilename: true # Pour autoriser un titre différent du nom de fichier
changelog: # afficher une liste des éléments extraits du journal des modifications de GitHub sur les pages d’accueil des produits
    label: Actions # doit être présent et correspondre aux labels utilisés dans le journal des modifications GitHub
    prefix: # chaîne optionnelle qui commence chaque titre du journal des modifications qui doit être omis dans le flux docs.
defaultPlatform: windows # Outrepasser la sélection initiale de la plateforme d’une page (optionel).
defaultTool: cli # Annuler la sélection initiale de l’outil pour une page (optionel).
learningTracks: # collection d’articles qui vous aident à maîtriser un sujet particulier.
  - parcours1
includeGuides: # Afficher une liste d’articles, filtrable par et . applicable uniquement lorsqu’elle est utilisée avec .type|topics|layout: product-guides
  - /chemin/vers/guide
journeyTracks: # Définir les parcours pour les pages d’atterrissage des voyages (prend en charge les variables liquides). Applicable uniquement lorsqu’elle est utilisée avec .layout: journey-landing
  - id: 'debuter' # Identifiant unique pour le voyage.
    title: 'Démarrer avec GitHub Actions' # afficher le titre du voyage
    description: # Description du parcours (optionnel)
    guides: # Ensemble d’objets-guides qui composent ce voyage.
      - href: '/actions/quickstart' # Chemin vers l’article
      - alternativeNextStep: # Texte personnalisé pour guider les utilisateurs vers des chemins alternatifs dans le parcours. (optionnel)
type: tutorial #  Indiquer le type d’article.
topics: # Indiquer les sujets abordés par l’article (https://github.com/github/docs/blob/main/data/allowed-topics.ts).
  - github
communityRedirect: # Définir un lien personnalisé et un nom de lien pour le lien dans le pied de page.
  name: Communauté
  href: https://github.community
  Object: 
effectiveDate: 2025-12-19
---
```

### redirect_from

Pour gérer les redirections d’URL :

- Utilisez la propriété `redirect_from` dans le frontmatter YAML pour rediriger d’anciennes URLs vers la nouvelle page

- Pour des redirections plus complexes (par version ou vers une autre page), modifiez le fichier `redirect-exceptions.txt` dans le dossier `src/redirects`.

- Pour rediriger vers un site externe, ajoutez une entrée dans `external-sites.json` :
```json
"/github-status": "https://www.githubstatus.com/",
"/articles/github-security": "https://github.com/security"
```

### children (page index)

La propriété `children` dans le frontmatter d’un fichier index.md liste les liens relatifs vers les pages enfants (articles, sous-catégories, etc.).

**Important :** Seuls les chemins listés dans `children` seront accessibles sur le site. Tout fichier ou dossier non référencé ici retournera une erreur 404.

### childGroups (page d'accueil)

La page d’accueil (index.md principal) doit contenir une liste complète de `children` et la propriété `childGroups` dans le frontmatter.

`childGroups` permet de regrouper les enfants par thème ou catégorie sur la page d’accueil.
Chaque groupe possède un nom (name), éventuellement une icône (icon), et une liste de chemins enfants (children) qui doivent aussi figurer dans la propriété `children`.

***Il faut toujours la propriété children*** même si on utilise childGroups.
Cela garantit que tous les liens sont reconnus et accessibles sur le site.
