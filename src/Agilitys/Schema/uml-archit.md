---
# Variable
showMiniToc: false
permissions: false
effectiveDate: 2026-07-09
---

# Architecture

```mermaid
architecture-beta

service Client(cloud)[Client]
service Site_Web(server)[Site_Web]
service Map(cloud)[Map]

group Pizzeria(cloud)[Pizzeria]
service Caisse(server)[Caisse] in Pizzeria
service Pizza_Data(database)[Pizza_Data] in Pizzeria

Client:R -- L:Site_Web
Site_Web:B -- T:Caisse
Site_Web:R -- L:Map
Caisse:R -- L:Pizza_Data
```
