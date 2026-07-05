---
---

# Démarrage rapide avec l’API REST GitHub

## Utiliser Octokit.js (JavaScript)

utiliser Octokit.js pour interagir avec l’API REST de GitHub dans vos scripts JavaScript.

1. Installez la librairie :
   ```sh
   npm install octokit
   ```
2. Importez et configurez avec votre jeton d’accès :
   ```js
   import { Octokit } from "octokit";
   const octokit = new Octokit({ auth: 'YOUR-TOKEN' });
   ```
3. Faites une requête :
   ```js
   await octokit.request("GET /repos/{owner}/{repo}/issues", {
     owner: "octocat",
     repo: "Spoon-Knife",
   });
   ```

## Exemple de workflow GitHub Actions

```yaml
on:
  workflow_dispatch:
jobs:
  use_api_via_script:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repo content
        uses: actions/checkout@v5
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '16.17.0'
          cache: npm
      - name: Install dependencies
        run: npm install octokit
      - name: Run script
        run: |
          node .github/actions-scripts/use-the-api.mjs
        env:
          TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Exemple de script Node.js

```js
import { Octokit } from "octokit";
const octokit = new Octokit({ auth: process.env.TOKEN });
try {
  const result = await octokit.request("GET /repos/{owner}/{repo}/issues", {
    owner: "octocat",
    repo: "Spoon-Knife",
  });
  const titleAndAuthor = result.data.map(issue => ({ title: issue.title, authorID: issue.user.id }));
  console.log(titleAndAuthor);
} catch (error) {
  console.log(`Error! Status: ${error.status}. Message: ${error.response.data.message}`);
}