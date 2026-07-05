---
# Variable
showMiniToc: true # auto et pas dans text
permissions: true # parametre d'accessibilité hors de GitHub
effectiveDate: 2025-01-07 # date de creation
image: https://www.pngitem.com/pimgs/m/360-3607163_storybook-js-logo-hd-png-download.png # image libre de droit

# Content pour faciliter la recherche
title: Storybook — Bloc Description & parameters.docs
intro: Guide pratique pour documenter un composant et ses stories via JSDoc, parameters.docs et MDX.
type: documentation
topics:
  - storybook
  - docs
  - jsdoc

# Information
author: RICHARD Wilfried
featuredLinks:
  - ofi: https://storybook.js.org/docs/writing-docs/doc-blocks
changelog:
  - 2025-01-07 : Ajout du front matter complet et clarification des options parameters.docs.
---

# Utiliser le bloc Description & parameters.docs

## ✅ Documentation directement dans Button.tsx (Recommandé)

Storybook extrait automatiquement la documentation depuis les **commentaires JSDoc** dans ton composant React/TypeScript !

### Résultat dans Storybook

- ✅ La description principale du composant formatées
- ✅ Description complète extraite du JSDoc de `ButtonProps`
- ✅ Chaque prop documentée avec description + valeur par défaut
- ✅ Exemples de code affichés (@example)
- ✅ Tableau des props généré automatiquement

### Structure de fichiers

```texte
Button/
├── Button.tsx          ← Documentation JSDoc ici
└── Button.stories.tsx  ← Stories simples
```

### Tags JSDoc supportés par Storybook

| Tag JSDoc | Usage | Exemple |
| --------- | ----- | ------- |
| `/** Description */` | Description du composant/prop | `/** Bouton réutilisable */` |
| `@default` | Valeur par défaut d'une prop | `@default 'primary'` |
| `@example` | Exemple de code | `@example <Button>Click</Button>` |
| `@deprecated` | Marquer comme obsolète | `@deprecated Utiliser NewButton` |
| `@see` | Lien vers autre doc | `@see ButtonGroup` |
| `@param` | Paramètre de fonction | `@param {string} text` |
| `@returns` | Type de retour | `@returns {JSX.Element}` |

### Exemple

**Button.tsx — Documentation complète avec JSDoc :**

```tsx
import { FC, ReactNode, MouseEvent } from 'react';

/**
 * # Composant Button réutilisable pour tous les CTA (Call-to-Action).
 * 
 * ## Caractéristiques
 * - Support des variantes (primary, secondary, tertiary, danger)
 * - États : normal, hover, active, disabled, loading
 * - Tailles : small, medium, large
 * 
 * ## Accessibilité
 * ✅ Contraste minimum 4.5:1
 * ✅ Zone cliquable 44x44px minimum
 * ✅ Support clavier complet
 * 
 * @example
 * ```tsx
 * <Button variant="primary" size="large" onClick={handleClick}>
 *   Envoyer
 * </Button>
 * ```
 */

export interface ButtonProps {
  /**
   * Variante visuelle du bouton
   * @default 'primary'
   */
  variant?: 'primary' | 'secondary' | 'tertiary' | 'danger';
}

/**
 * Composant Button
 */
export const Button: FC<ButtonProps> = ({}) => {};
```

**Button.stories.tsx — Stories simples (Storybook lit automatiquement Button.tsx) :**

- La description du composant depuis le JSDoc de ButtonProps
- Les descriptions de chaque prop
- Les valeurs par défaut (@default)
- Les exemples (@example)

```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta = {
  component: Button,
} satisfies Meta<typeof Button>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Primary: Story = {
  args: {
    children: 'Bouton primaire',
  },
};
```

## Exemple minimal — Documentation dans Button.tsx

**Button.tsx :**

```tsx
/**
 * Bouton réutilisable pour CTA
 */
export interface ButtonProps {
  /** Texte du bouton */
  children: ReactNode;
  
  /** Variante visuelle @default 'primary' */
  variant?: 'primary' | 'secondary';
  
  /** Callback au clic */
  onClick?: () => void;
}

export const Button: FC<ButtonProps> = ({ children, variant = 'primary', onClick }) => (
  <button className={`btn-${variant}`} onClick={onClick}>
    {children}
  </button>
);
```

**Button.stories.tsx :**

```tsx
import { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta = { component: Button } satisfies Meta<typeof Button>;
export default meta;

type Story = StoryObj<typeof meta>;

export const Primary: Story = {
  args: { children: 'Click me' },
};
```

## Story

- Utiliser des commentaires JSDoc pour descriptions naturelles et faciles à maintenir.
- Utiliser `parameters.docs.description.*` seulement si les commentaires ne sont pas possibles ou pour surcharger ponctuellement.

## Tous les paramètres `parameters.docs`

```ts
import { Meta, Description, Canvas, Controls } from '@storybook/addon-docs/blocks';

parameters: {
  docs: {
    subtitle: 'Ajouter un sous-titre au composant dans la documentation',
    description: { // Configurer les descriptions à différents niveaux
      component: 'Description du composant (surchage les commentaires JSDoc).',
      story: 'Description spécifique à cette histoire.',
    },
    source: { // Personnaliser l'affichage du code source
      code: '<Button disabled>Texte personnalisé</Button>', // Code à afficher
      language: 'jsx', // javascript, typescript, jsx, tsx, etc.
      type: 'code', // 'code' | 'auto' | 'dynamic' | 'story'
    },
    page: () => ( // Personnaliser la page de documentation entière (MDX ou React) :
      <>
        <Description of={SomeStories} />
        <Canvas of={SomeStories.Primary} />
        <Controls of={SomeStories.Primary} />
      </>
    ),
    controls: {
      expanded: true, // Agrandir/replier automatiquement le panneau des contrôle; false par défaut
      sort: 'alpha', // Trier les contrôles (Arg); 'alpha' | 'requiredFirst'
    },
  },
}
```

## Exemple complet — toutes les options

```ts
import type { Meta, StoryObj } from '@storybook/your-framework';

/**
 * Le composant Button affiche un bouton avec plusieurs variantes.
 * Il supporte différents états : normal, hover, disabled, active.
 */
export const Button = () => <button>Click me</button>;

const meta = {
  component: Button,
  parameters: {
    docs: {
      // Description
      description: {
        component: 'Composant Button réutilisable pour tous les CTA (Call-to-Action).',
      },
      // Sous-titre
      subtitle: 'Bouton interactif avec 4 variantes de style',
      // Source personnalisée
      source: {
        code: '<Button>Cliquez-moi</Button>',
        language: 'jsx',
      },
      // Contrôles
      controls: {
        expanded: true,
        sort: 'alpha',
      },
    },
  },
} satisfies Meta<typeof Button>;
export default meta;
```

Variante par défaut pour les actions principales.

```ts
type Story = StoryObj<typeof meta>;

export const Primary: Story = {
  parameters: {
    docs: {
      description: {
        story: 'Utilisez cette variante pour les CTA principaux.',
      },
      source: {
        code: '<Button variant="primary">Action</Button>',
        language: 'jsx',
      },
    },
  },
};
```
