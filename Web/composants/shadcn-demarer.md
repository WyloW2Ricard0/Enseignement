---

---

# shadcn/ui - Guide pour démarrer

## Qu'est-ce que shadcn/ui ?

shadcn/ui est une **collection de composants UI réutilisables** construits avec **Radix UI** et **Tailwind CSS**. Contrairement aux bibliothèques de composants traditionnelles, shadcn/ui vous donne accès au **code source complet** des composants pour une personnalisation totale.

Utilise Radix UI pour l'accessibilité et le comportement des composants, garantissant une excellente accessibilité WCAG 2.1.

### Avantages de shadcn/ui

✅ **Contrôle total** : Vous possédez le code source
✅ **Personnalisation facile** : Modifiez directement le code
✅ **Accessibilité garantie** : Basé sur Radix UI
✅ **Légèreté** : N'installez que ce dont vous avez besoin
✅ **Pas de maj forcées** : Contrôlez quand mettre à jour
✅ **Design moderne** : Esthétique épurée et professionnelle
✅ **TypeScript** : Support TypeScript complet
✅ **Communauté** : Composants créés par la communauté

### Cas d'usage idéaux pour shadcn/ui

- 🎨 **Applications avec design personnalisé**
- 🚀 **Projets Vite/Next.js modernes**
- 💼 **Dashboards et applications d'entreprise**
- 📱 **Applications responsive-first**
- 🎯 **Prototypes et MVPs rapides**
- 🏗️ **Projets où vous contrôlez le code**

## Caractéristiques principales

### Code source propriétaire

shadcn/ui n'est pas une dépendance - c'est une collection de composants que vous **copiez dans votre projet**. Vous contrôlez totalement le code.

```bash
npx shadcn-ui@latest add button
npx shadcn-ui@latest add card
npx shadcn-ui@latest add form
```

### Stylé avec Tailwind CSS

Tous les composants utilisent Tailwind CSS, ce qui signifie :

- Personnalisation facile via classes Tailwind
- Pas de CSS-in-JS
- Bundle size réduit

```jsx
import { Button } from "@/components/ui/button"

export default function App() {
  return (
    <Button className="bg-blue-600 hover:bg-blue-700">
      Cliquez-moi
    </Button>
  )
}
```

### Personnalisation du thème

Modifiez les couleurs et le style en un seul fichier `globals.css`.

```css
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 0 0% 3.6%;
    --card: 0 0% 100%;
    --card-foreground: 0 0% 3.6%;
    --primary: 0 0% 9%;
    --primary-foreground: 0 0% 98%;
    --secondary: 0 0% 96.1%;
    --secondary-foreground: 0 0% 9%;
  }

  .dark {
    --background: 0 0% 3.6%;
    --foreground: 0 0% 98%;
    --card: 0 0% 3.6%;
    --card-foreground: 0 0% 98%;
  }
}
```

### Installation composant par composant

N'installez que les composants dont vous avez besoin, gardez votre projet léger.

## Installation

### Prérequis

- React 18+
- Tailwind CSS 3.0+
- Moderne avec un build tool (Vite, Next.js, etc.)

### Configuration initiale

```bash
# Créer une app Vite
npm create vite@latest mon-app -- --template react
cd mon-app
npm install

# Ajouter Tailwind CSS
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Ajouter shadcn/ui
npx shadcn-ui@latest init
```

### Répondre aux questions de configuration

```
✔ Which style would you like to use? › Default
✔ Which color would you like as your base color? › Slate
✔ Would you like to use CSS variables for theming? › yes
```

## Conclusion

shadcn/ui est parfait si vous :

- Voulez une **flexibilité maximale** sur vos composants
- Préférez **contrôler le code source**
- Utilisez déjà **Tailwind CSS**
- Construisez des applications **modernes avec Vite ou Next.js**
- Appréciez une **excellente accessibilité** sans compromis

C'est une excellente alternative aux bibliothèques de composants traditionnelles, offrant plus de contrôle et de personnalisation tout en gardant une excellente accessibilité et une belle esthétique.

### Ressources utiles

- [Documentation officielle shadcn/ui](https://ui.shadcn.com)
- [Composants disponibles](https://ui.shadcn.com/docs/components/accordion)
- [Exemples et templates](https://ui.shadcn.com/examples)
- [Radix UI Documentation](https://www.radix-ui.com) - Fondation des composants
- [Tailwind CSS](https://tailwindcss.com) - Framework CSS utilisé
- [shadcn/ui Discord](https://discord.gg/pqvq3dn4Gx)
