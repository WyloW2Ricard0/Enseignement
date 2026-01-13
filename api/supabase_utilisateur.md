---
versions: 1.0.0
effectiveDate: 2025-12-19
author: RICHARD Wilfried

title: Authentification et gestion des utilisateurs Supabase
intro: Guide pour gérer l’authentification, les rôles et la sécurité des utilisateurs avec Supabase.
type: guide
topics:
  - supabase
  - authentification
  - api
  - sécurité
image: "https://supabase.com/docs/img/supabase-logo.svg"

---

# Authentification

Si un en-tête est inclus, l’API `switch` vers le rôle de l’utilisateur qui effectue la requête. Voir la section Gestion des utilisateurs pour plus de détails.

Si aucun en-tête n’est inclus, l’API supposera que vous faites une requête auprès d’un utilisateur anonyme.

Nous recommandons de définir vos clés comme Variables d’Environnement.
