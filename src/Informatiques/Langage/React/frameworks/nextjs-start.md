# Comment créer une page de dev avec Next.js (minimal)

## Structure de base

### README.md

### package.json minimal

```json
{
  "name": "theme",
  "version": "1.0.0",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "next": "latest",
    "react": "latest",
    "react-dom": "latest",
    "@mui/material": "latest",
  }
}
```

### app\page.js

```js
import { Container, Typography, Box } from '@mui/material'

export default function Home() {
  return (
    <Container>
      <Box sx={{ py: 4 }}>
        <Typography variant="h1">Bienvenue</Typography>
      </Box>
    </Container>
  )
}
```

### app\layout.js

```js
'use client'

import {
  CssBaseline,
  ThemeProvider, createTheme } from '@mui/material'

const theme = createTheme()

export default function RootLayout({ children }) {
  return (
    <html lang="fr">
      <body>
        <ThemeProvider theme={theme}>
          <CssBaseline />
          {children}
        </ThemeProvider>
      </body>
    </html>
  )
}
```

### Apercu

```shell
npm install
npm run dev
```

C'est tout ! La page est accessible sur http://localhost:3000
