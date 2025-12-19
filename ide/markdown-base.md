---
versions: 1.0.0
effectiveDate: 2025-12-17
author: RICHARD Wilfried

title: Markdown : bases et exemples
excerpt: Exemples concrets pour apprendre la syntaxe de base de Markdown et son rendu HTML.
type: tutoriel
topics:
    - markdown
    - html
    - exemples
    - syntaxe
image: "https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg"
---

# Markdown: Basics

## Getting the Gist of Markdown's Formatting Syntax

Cette page offre un bref aperçu de l'utilisation de Markdown.

Markdown devrait être très facile à comprendre simplement en regardant quelques exemples de son utilisation.

Les exemples sur cette page sont écrits dans un style avant/après, montrant un exemple de syntaxe et le
résultat HTML produit par Markdown.

### Paragraphs,Headers, Blockquotes

Un **paragraphe** est simplement une ou plusieurs lignes consécutives de texte, ***séparées par une ou plusieurs lignes vides*** ~rien d'autre que des espaces ou des tabulations).

Les **en-têtes** de style *atx* pour `<h1>` et `<h2>` sont créés en ***placez 1 à 6 dièses (`#`)*** au début de la ligne ~le nombre de dièses correspond au niveau.

Les **citations** sont indiquées à l'aide de crochets angulaires `>` de style e-mail.

Markdown:
```md
# A First Level Header

## A Second Level Header

Now is the time for all good men to come to
the aid of their country. This is just a
regular paragraph.

The quick brown fox jumped over the lazy
dog's back.

### Header 3

> This is a blockquote.
> 
> This is the second paragraph in the blockquote.
>
> ## This is an H2 in a blockquote
```


Output:
```html
<h1>A First Level Header</h1>

<h2>A Second Level Header</h2>

<p>Now is the time for all good men to come to
the aid of their country. This is just a
regular paragraph.</p>

<p>The quick brown fox jumped over the lazy
dog's back.</p>

<h3>Header 3</h3>

<blockquote>
    <p>This is a blockquote.</p>
    
    <p>This is the second paragraph in the blockquote.</p>
    
    <h2>This is an H2 in a blockquote</h2>
</blockquote>
```

### Phrase Emphasis ###

Des **astérisques** pour indiquer les passages à mettre en évidence.

Markdown:
```md
Some of these words *are emphasized*.

Use two asterisks for **strong emphasis**.
```

Output:
```html
<p>Some of these words <em>are emphasized</em>.

<p>Use two asterisks for <strong>strong emphasis</strong>.
``` 

## Lists ##

Les listes **non ordonnées** (à puces) utilisent des tirets (`-`) comme marqueurs de liste.

Markdown:
```md
-   Candy.
-   Gum.
-   Booze.
```

Output:
```html
<ul>
<li>Candy.</li>
<li>Gum.</li>
<li>Booze.</li>
</ul>
```

Les listes **ordonnées** (numérotées) utilisent des chiffres normaux suivis de points comme marqueurs de liste :

```md
1.  Red
2.  Green
3.  Blue
```

Output:
```html
<ol>
<li>Red</li>
<li>Green</li>
<li>Blue</li>
</ol>
```

Vous pouvez créer des éléments de **liste comportant plusieurs paragraphes**.
Si vous ***insérez des lignes vides entre les éléments***, vous obtiendrez des balises `<p>` pour le texte des éléments de la liste.  en indentant les paragraphes de `4 espaces` ou d'une tabulation :

```md
*   A list item.

    With multiple paragraphs.

*   Another item in the list.
```

Output:
```html
<ul>
<li><p>A list item.</p>
<p>With multiple paragraphs.</p></li>
<li><p>Another item in the list.</p></li>
</ul>
```

### Links ###

Pour **créer des liens** *reference* par leur nom. 

Vous utilisez des crochets pour délimiter le texte que vous souhaitez transformer en lien.

Les noms des liens peuvent contenir des lettres, des chiffres et des espaces, mais ne sont *pas* sensibles à la casse.

Vous définissez ailleurs dans votre document :


```md
I start my morning with a cup of coffee and
[The New York Times][NY Times].

[ny times]: http://www.nytimes.com/
```

Output:
```html
<p>I start my morning with a cup of coffee and
<a href="http://www.nytimes.com/">The New York Times</a>.</p>
```

### Images ###

La syntaxe des images est très similaire à celle des liens.

Reference-style:
```md
![alt text][id]

[id]: /path/to/img.jpg "Title"
```

Output:
```html
<img src="/path/to/img.jpg" alt="alt text" title="Title" />
```



### Code ###

Vous pouvez **créer une balise** de code en ***encadrant le texte par des guillemets inversés***.

Les esperluettes (`&`) et les crochets angulaires (`<` ou `) seront ***automatiquement convertis*** en entités HTML.

Cela facilite l'utilisation de Markdown pour écrire des exemples de code HTML :

```md
I strongly recommend against using any `<blink>` tags.

I wish SmartyPants used named entities like `&mdash;`
instead of decimal-encoded entities like `&#8212;`.
```

Output:
```html
<p>I strongly recommend against using any
<code>&lt;blink&gt;</code> tags.</p>

<p>I wish SmartyPants used named entities like
<code>&amp;mdash;</code> instead of decimal-encoded
entities like <code>&amp;#8212;</code>.</p>
```


Pour **spécifier un bloc entier** de code préformaté, indentez chaque ligne du bloc de `1 tabulation`. Tout comme pour les segments de code, les caractères `&`, `<` et
`>` seront automatiquement échappés.

```md
If you want your page to validate under XHTML 1.0 Strict,
you've got to put paragraph tags in your blockquotes:

<blockquote>
    <p>For example.</p>
</blockquote>
```

Output:
```html
<p>If you want your page to validate under XHTML 1.0 Strict,
you've got to put paragraph tags in your blockquotes:</p>

<pre><code>&lt;blockquote&gt;
    &lt;p&gt;For example.&lt;/p&gt;
&lt;/blockquote&gt;
</code></pre>
```
