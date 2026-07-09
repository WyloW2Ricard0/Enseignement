---
# Variable
showMiniToc: false
permissions: false
effectiveDate: 2026-07-09
---

# Architecture Hexagonal

vise à permettre l’interopérabilité entre les outils de modélisation, s’inscrit dans l’approche *MDA*.

## 1

### 11

#### 111. LES GRANDS PRINCIPES DE GENIE LOGICIEL

L'approche objet permet de répondre aux préoccupations des analystes et des concepteurs en leur offrant une démarche homogène tout au long du cycle de éveloppement.
Quelles que soient les méthodes mises en oeuvre à chacune des étapes, l'objectif final à atteindre est de produire un logiciel qui corresponde à des besoins réels et qui soit facilement maintenable.
C'est à dire qu'il doit être:

- CORRECT En répondant exactement aux besoins des utilisateurs
- ROBUSTE En réagissant de façon prévisible à toutes les situations
- MAINTENABLE En acceptant les modifications de spécification (simplification ou enrichissement par rapport aux besoins initiaux) et en permettant facilement de localiser et corriger les anomalies
- REUTILISABLE En étant apte à être réutilisé dans un autre contexte afin de diminuer les coûts de production et d'améliorer la fiabilité
- PERFORMANT Vis à vis du temps et de l'espace mémoire

L'approche objet va permettre de respecter ces objectifs car elle offre un ensemble de concepts reconnus, permettant de garantir une production de logiciels de qualité:

#### 112. MOTIVATION DE L'APPROCHE OBJET

On constate que parmi les étapes du cycle de vie, celle correspondant à la spécification est la plus longue, environ 50 à 60% du temps développement.
De plus, de récents rapports font état que 40 à 70% du budget informatique des sociétés est consacré à la maintenance des logiciels.
A toutes les étapes du cycle de vie il est impératif de mettre en œuvre une démarche cohérente qui prenne en compte ces aspects importants.

Forte de cette motivation, l'approche objet est apparue progressivement afin de mettre entre les mains du programmeur une méthodologie3 cohérente lui permettant:

- de décomposer l'application en modules les plus autonomes possibles et compréhensibles individuellement.
Ceci favorise au maximum la réutilisation de parties de logiciel et diminue le temps passé en test
- de construire des modules dont la structure est masquée, pour que la conception ne soit plus basée sur des détails de bas niveau.
ceci facilite le portage des applications tout en tenant compte des évolutions des OS et de l'architecture du matériel
- de définir des modules présentant un niveau d'abstraction suffisamment grand pour modéliser au mieux les situations du monde réel.

#### 113. UN PEU D'HISTOIRE

La plus importante contribution à l'approche objet provient très certainement des langages de programmation tels que Simula et Smalltalk, qui ont introduit à la fin des années 70, le concept d'objet par réaction à l'approche impérative, utilisée à l'époque dans des langages comme Fortran, Cobol, Algol et bien d'autres.
Smalltalk qui a vu le jour dans les laboratoires de Rank Xerox (Paolo Alto), repose entièrement sur la notion d'objet et est intégré dans un environnement de développement interactif (menus déroulant, fenêtres,..).
Il hérite de Simula 67 qui était, comme son nom l'indique, un langage de simulation introduisant les concepts d'encapsulation et d'héritage, permettant pour la première fois la modélisation des situations du monde réel.
A partir des différentes versions de Smalltalk ont été définis un grand nombre de langages de programmation basés sur le concept d'objet (C++, Objective C, Object Pascal, Eiffel. et plus récemment Java).

A la fin des années 70 les méthodes de conception utilisées reposaient sur une approche structurée descendante.
Ces méthodes, conçues à partir des travaux de Djikstra, Yourdon, Constantine et bien d'autres, orientées traitements, étaient bien adaptées à la conception d'applications écrites avec les langages impératifs de l'époque.
La taille et la complexité des logiciels évoluant, ces méthodes devinrent insuffisantes.
C'est à la suite des travaux de Parnas, qui a introduit le concept de module, de Liskov et Guttag sur les types abstraits de donnée puis d'une équipe française dirigée par Galinier et Mathis sur les machines abstraites qu'a été formalisée, au début des années 80 la populaire méthode de Booch.
Cette méthode peut être considérée comme une approche très pédagogique de la conception orientée objet.
Elle a permis d'introduire la culture objet dans l'entreprise.
De nombreuses autres méthodes ont été mises au point à partir des travaux de Booch parmi lesquelles Mach2, Hood, OOD, Mac-Adam ...

Plus tard, à la fin des années 80, héritant des travaux de Shlaer et Mellor sur le modèle sémantique de donnée, est apparue l'analyse orientée objet permettant enfin d'utiliser le concept d'objet pendant la phase de spécification.

A partir des années 90 l'approche objet s'est révélée, être en informatique un concept fédérateur, non seulement pour les langages de programmation et les méthodes de conception et de spécification mais aussi pour: la conception d'interfaces utilisateur, les bases de données, les bases de connaissances.
Dans le milieu de la décennie on comptait une cinquantaine de méthodes recouvrant en totalité ou partiellement les phases d'analyse (spécification et conception) du cycle de vie du logiciel.
Trois méthodes ont eu un impact fort sur la communauté informatique:

1. La méthode de Grady Booch, dite Booch'93
2. La méthode de Jim Rumbaugh OMT-2 (Object Modeling Technique)
3. La méthode d'Ivar Jacobson OOSE (Object Oriented Software Engineering)

Les concepts et formalismes de ces trois méthodes ont été mis en commun dès 1995 pour former une méthode unifiée baptisée UML (Unified Modeling Language for Object-Oriented Development).
La version 1.0 de la méthode a été formalisée par un consortium d'entreprises parmi lesquelles DEC, HP, IBM, Microsoft, Oracle et d'autres.
La version 1.1 a été normalisée par l'OMG (Object Management Group) en 1997.
La version UML 2.0 est prévue pour 2002 Booch, Rumbaugh et Jacobson sont souvent considérés comme les "pères fondateurs" d'UML.
Parfois même, on les appèle les "3 Amigos".

DDD, Hexagonal, Onion, Clean, CQRS, ... Comment tout assembler
6 août 2022
Osman Selçok
DDD, Hexagonal, Onion, Clean, CQRS, ... Comment tout assembler

DDD, Hexagonal, Onion, Clean, CQRS, ... Comment tout assembler
DDD, Hexagonal, Onion, Clean, CQRS, ... Comment tout mettre en place ?

Vous pouvez lire la source originale de cet article préparé par @hgraca à partir de ce lien.

Note de la rédaction : Nous avons essayé de traduire en turc avec sa narration. Nous vous demandons de lire en conséquence au fur et à mesure que vous lisez l’article.

Cet article fait partie de Software Architecture Chronicles, une série de publications consacrées à l’architecture logicielle. J’y écris sur ce que j’ai appris sur l’architecture logicielle, comment je pense et comment j’utilise ces connaissances. Le contenu de ce billet peut être plus significatif si vous lisez les précédents articles de cette série.

Après avoir obtenu mon diplôme universitaire, j’ai poursuivi une carrière de professeur au lycée jusqu’à il y a quelques années, que j’ai décidé d’abandonner pour devenir développeur logiciel à plein temps.

À partir de ce moment, j’ai toujours eu l’impression que je devais retrouver le temps « perdu » et apprendre aussi vite que possible, autant que possible. Je suis donc devenu un peu accro à l’expérimentation, à la lecture et à l’écriture, avec un accent particulier sur la conception logicielle et l’architecture. C’est pourquoi j’écris ces articles pour m’aider à apprendre.

Dans mes écrits récents, j’ai écrit sur de nombreux concepts et principes que j’ai appris, ainsi qu’un peu sur la façon dont je les raisonne. Mais je les vois comme des pièces d’un grand puzzle.

Le post d’aujourd’hui porte sur la façon dont j’ai assemblé toutes ces pièces, et il semble que je doive lui donner un nom, que j’appelle Architecture Ouverte. De plus, tous ces concepts ont « passé les épreuves de la guerre » et sont utilisés dans le code de production sur des plateformes extrêmement exigeantes. L’une est une plateforme SaaS de commerce électronique avec des milliers de boutiques en ligne à travers le monde, et l’autre est une place de marché présente dans 20 pays avec un bus de messages traitant plus de 2 millions de messages par mois.

Blocs de base du système
Outils
Connecter outils et mécanismes de diffusion à Application Core
Ports
Adaptateurs primaires ou de disque
Adaptateurs secondaires ou pilotés
Renversement de contrôle
Organisation du noyau de l’application
Couche application
Couche de domaine
Services de domaine
Modèle de domaine
Composants
Composants séparateurs
Logique de déclenchement sur d’autres composants
Récupérer des données à partir d’autres composants
Stockage partagé des données entre composants
Stockage dédié des données par composant
Contrôle du flux

Blocs de base du système
Je commence par me souvenir des architectures EBI et Ports & Adapters. Les deux distinguent clairement quel code est interne dans l’application, ce qui est externe, et ce qui est utilisé pour connecter le code interne et externe.

De plus, l’architecture Ports and Adapters définit clairement les trois blocs fondamentaux de code dans un système :

Quel que soit le type d’interface utilisateur, ce qui rend possible l’exécution d’une interface utilisateur est la suivante :
La logique métier système ou le noyau applicatif utilisé par l’interface utilisateur pour faire avancer les choses ;
Un code d’infrastructure qui relie notre cœur d’application à des outils tels qu’une base de données, un moteur de recherche ou des API tierces.
000 - Ouvert Mimari.svg
Le noyau de l’application est ce qui nous intéresse vraiment. C’est le code qui fait fonctionner notre code ce qu’il doit faire, c’est notre application. Il peut utiliser plusieurs interfaces (application web progressive, mobile, CLI, API, ...) mais en réalité le code qui fait le travail est le même et se trouve dans le cœur de l’application, peu importe quelle interface le déclenche.

Comme vous pouvez l’imaginer, le flux typique de l’application passe du code dans l’interface utilisateur, du noyau de l’application au code de l’infrastructure, puis revient au noyau de l’application, et enfin à une réponse à l’interface utilisateur.

010 - Ouvert Mimari.svg
Outils
Loin du noyau de l’application, qui est le code le plus important de notre système, nous disposons des outils que notre application utilise, tels qu’un moteur de base de données, un moteur de recherche, un serveur Web ou une console CLI (bien que les deux derniers soient aussi de la livraison). mécanismes).

020 - Ouvert Mimari.svg
Bien qu’il puisse sembler étrange de mettre une console CLI dans le même « scoop » qu’un moteur de base de données, et qu’elles aient des objectifs différents, ce sont en réalité les outils utilisés par l’application. La principale différence est que, tandis que la console CLI et le serveur web servent à dire à notre application de faire quelque chose, elle dit au moteur de base de données de faire quelque chose par notre application. C’est une distinction très pertinente, car elle a de fortes implications sur la manière dont nous construisons le code qui relie ces outils au cœur de l’application.

Connecter outils et mécanismes de diffusion à Application Core
Les unités de code qui connectent les outils au cœur de l’application sont appelées adaptateurs (Ports and Adapters Architecture). Les adaptateurs sont ceux qui implémentent efficacement du code permettant à la logique métier de communiquer avec un outil spécifique, et inversement.

Les adaptateurs qui demandent à notre application de faire quelque chose sont appelés adaptateurs primaires ou adaptateurs de lecteur, tandis que ceux qui demandent à notre application de faire quelque chose sont appelés adaptateurs secondaires ou adaptateurs de lecteur.

Ports
Cependant, ces adaptateurs ne sont pas générés aléatoirement. Ils sont conçus pour s’adapter à un point d’entrée très spécifique dans le Cœur de l’Application, qui est un Port. Le port n’est rien d’autre qu’une spécification de la manière dont l’outil peut utiliser le noyau de l’application ou comment il est utilisé par le cœur d’application. Dans la plupart des langages, et dans sa forme la plus simple, cette spécification, Port, sera une Interface, mais elle peut en réalité consister en plusieurs Interfaces et DTO.

Il est important de noter que les ports (interfaces) appartiennent à l’intérieur de la logique métier tandis que les adaptateurs appartiennent à l’extérieur. Pour que ce modèle fonctionne comme il le faut, il est extrêmement important que les ports soient conçus pour répondre aux besoins du cœur d’application, plutôt que de simplement imiter les API des outils.

Adaptateurs principaux ou d’entraînement
Les adaptateurs primaires ou de pilotes s’enroulent autour d’un port et l’utilisent pour indiquer au cœur d’application quoi faire. Ils traduisent tout ce qui va du mécanisme de livraison en un appel de méthode dans le Cœur d’application.

030 - Ouvert Architecture.svg
En d’autres termes, nos adaptateurs de pilotage sont des contrôleurs ou commandes console injectées dans leurs constructeurs avec certains objets dont les classes implémentent l’interface (Port) requise par la commande contrôleur ou console.

Dans un exemple plus concret, un port pourrait être une interface de service ou une interface de dépôt dont un contrôleur a besoin. L’implémentation concrète du Service, du Dépôt ou de la Requête est ensuite injectée dans le Contrôleur et utilisée.

Sinon, il peut s’agir d’une interface Port, Command Bus ou Query Bus. Dans ce cas, une implémentation concrète du bus de commande ou de requête est injectée dans le contrôleur, qui génère ensuite une commande ou une requête et la transmet au bus correspondant.

Adaptateurs secondaires ou pilotés
Contrairement aux adaptateurs pilote, qui entourent un port, les adaptateurs pilotés implémentent un port, une interface, puis sont injectés dans le cœur de l’application là où le port est nécessaire (avec des indices de type).

040 - Ouvert Mimari.svg
Par exemple, supposons que nous ayons une application pure qui doit maintenir les données. Par conséquent, nous créons une interface de persistance qui répond à leurs besoins grâce à une méthode d’enregistrement d’un ensemble de données et une méthode de suppression d’une ligne dans un tableau par son ID. À partir de ce moment, lorsque notre application doit enregistrer ou supprimer des données, nous aurons besoin d’un objet qui implémente l’interface de persistance que nous avons définie dans son constructeur.

Nous créons maintenant un adaptateur personnalisé vers MySQL qui implémentera cette interface. Nous disposerons de méthodes pour sauvegarder un tableau, supprimer une ligne dans une table et l’injecter là où l’interface de persistance est requise.

Si à un moment donné nous décidons de changer de fournisseur de base de données, disons PostgreSQL ou MongoDB, il nous suffit de créer un nouvel adaptateur qui implémente l’interface de persistance et spécifique à PostgreSQL, et d’injecter le nouvel adaptateur au lieu de l’ancien.

Inversion de contrôle
Une caractéristique à noter concernant ce modèle est que les adaptateurs sont connectés à un outil spécifique et à un port spécifique (en implémentant une interface). Cependant, notre logique métier dépend uniquement du port (interface) conçu pour répondre aux exigences de la logique métier, il n’est donc pas lié à un adaptateur ou outil spécifique.

050 - Ouvert Mimari.svg
Cela signifie que la direction des dépendances est vers le centre, ce qui est un renversement du principe de contrôle au niveau architectural.

Cela dit, il est extrêmement important que les ports soient conçus pour répondre aux exigences du Cœur d’application et non simplement imiter les API d’outils.

Organisation du noyau d’application)
L’architecture Onion prend les couches DDD et les combine avec l’architecture des ports et adaptateurs. Ces couches sont destinées à introduire une disposition dans la logique métier, à l’intérieur de l'« hexagone » des ports et adaptateurs, et tout comme pour les ports et adaptateurs, la direction de la dépendance est orientée vers le centre.

Couche application
Les cas d’utilisation sont des processus qui peuvent être déclenchés dans notre Application Core par une ou plusieurs interfaces utilisateur de notre application. Par exemple, nous pouvons avoir l’interface utilisateur réelle utilisée par les utilisateurs courants dans un CMS, une autre interface autonome pour les administrateurs CMS, une autre interface CLI, et une API web. Ces interfaces (applications) peuvent déclencher des cas d’utilisation spécifiques à l’un d’eux ou réutilisés par plusieurs.

Les cas d’utilisation sont définis dans la couche application, qui est la première couche fournie par DDD et utilisée par l’architecture Onion.

060 - Ouvert Mimari.svg
Cette couche inclut les services d’application (et les interfaces) en tant que citoyens de première classe, mais inclut aussi les interfaces Ports et Adaptateurs (ports) qui incluent les interfaces ORM, les interfaces de moteurs de recherche, les interfaces de messagerie, etc. Dans le cas où nous utilisons le Command Bus et/ou le Query Bus, cette couche est la couche à laquelle appartiennent les Handlers respectifs pour les commandes et requêtes.

Les services d’application et/ou les gestionnaires de commandes contiennent la logique pour exposer un cas d’usage, un processus métier. En général, leur rôle est :

utiliser un pool pour trouver un ou plusieurs actifs ;
Dites à ces entités de faire un peu de logique de domaine ;
et utiliser le dépôt pour reprendre les ressources en enregistrant activement les modifications de données.
Les gestionnaires de commandes peuvent être utilisés de deux manières différentes :

Ils peuvent intégrer la logique réelle pour réaliser le cas d’usage ;
Ils peuvent être utilisés dans notre architecture comme de simples morceaux de câblage, ils prennent une commande et déclenchent simplement la logique qui existe dans un Service d’application.
L’approche à utiliser dépend du contexte, par exemple :

Avons-nous déjà des services d’application et ajoutons-nous maintenant un bus de commande ?
Le bus de commande permet-il de spécifier des classes/méthodes comme gestionnaires, ou doit-il étendre ou implémenter des classes ou interfaces existantes ?
Cette couche inclut également le déclenchement des événements d’application, qui représentent un résultat d’un cas d’utilisation. Ces événements déclenchent une logique qui est un effet secondaire d’un cas d’usage, comme l’envoi d’un e-mail, la notification d’une API tierce, l’envoi d’une notification push, ou même le lancement d’un autre cas d’usage appartenant à un autre composant de l’application.

Couche de domaine
Plus à l’intérieur, nous avons la couche de domaine. Les objets de cette couche contiennent des données uniques au domaine lui-même et à la logique de traitement de ces données, et sont indépendants des processus métier qui déclenchent cette logique, ils sont indépendants et totalement inconscients de la couche application.

070 - Ouvert Mimari.svg
Services de domaine
Comme je l’ai mentionné plus haut, le rôle d’un service d’application est :

utiliser un pool pour trouver un ou plusieurs actifs ;
Dites à ces entités de faire un peu de logique de domaine ;
et utiliser le dépôt pour reprendre les ressources en enregistrant activement les modifications de données.
Cependant, parfois, nous rencontrons une logique de champ qui implique différentes entités du même type ou non, et nous avons le sentiment que cette logique de champ n’appartient pas aux entités elles-mêmes, nous estimons que cette logique n’est pas leur responsabilité directe.

Notre première réaction pourrait donc être de placer cette logique en dehors des entités, dans un Service d’application. Cependant, cela signifie que la logique de domaine ne peut pas être réutilisée dans d’autres cas d’usage : la logique de domaine doit rester en dehors de la couche application !

La solution consiste à créer un service de domaine ayant pour rôle de récupérer un ensemble d’entités et d’exécuter une certaine logique métier sur celles-ci. Un service de domaine appartient à la couche de domaine et ne connaît donc rien des classes de la couche application, telles que les services d’application ou les dépôts. D’un autre côté, il peut utiliser d’autres services de domaine et, bien sûr, des objets de modèle de domaine.

Modèle de domaine
Au centre se trouve le Modèle de Domaine, qui contient des objets métier représentant quelque chose dans le domaine, sans être liés à quoi que ce soit en dehors. Des exemples de ces objets sont, tout d’abord, les Entités, ainsi que les Objets Valeur, les Énumérations et les objets utilisés dans le Modèle de Domaine.

Le Modèle de Domaine est aussi l’endroit où les Événements de Domaine « vivent ». Ces événements sont déclenchés lorsqu’un jeu de données particulier change, et ils entraînent ces changements avec eux. En d’autres termes, lorsqu’une entité change, un événement de domaine est déclenché, et ses propriétés modifiées portent de nouvelles valeurs. Ces événements sont parfaits pour une utilisation en Event Sourcing, par exemple.

Composants)
Jusqu’à présent, nous avons séparé le code par couches, mais il s’agit d’une séparation fine du code. La séparation grossière du code est au moins tout aussi importante, et il s’agit de séparer le code par sous-domaines et contextes bornés, suivant les idées de Robert C. Martin exprimées dans une architecture révolutionnaire. Cela est souvent appelé « Package by feature » ou « Package by component » plutôt que « Package by layer », et Simon Brown l’explique très bien dans son article de blog « Package by component and architecturally aligned testing » :

20150308-Package à couches
20150308 - Emballage selon les spécifications
20150308 - Package par composant
« Package par composant » et par composante En prenant le diagramme de Simon Brown sur le paquet, je le modifierais sans honte comme suit :

Ces sections de code croisent les couches décrites précédemment, qui sont les composantes de notre application. Des exemples de composants seraient l’authentification, l’autorisation, la facturation, l’utilisateur, l’avis ou le compte, mais ils sont toujours liés aux champs. Les contextes limités comme l’Autorisation et/ou l’Authentification doivent être considérés comme des outils externes où l’on crée un adaptateur et se cache derrière un sorte.

080 - Ouvert Mimari.svg
Découplage des composants
Tout comme les unités de code à grain fin (classes, interfaces, propriétés, mélanges, ...), les unités de code grossier (composantes) bénéficient d’un faible correspondance et d’une forte cohésion.

Pour séparer les classes, nous utilisons l’injection de dépendances en injectant des dépendances dans une classe au lieu de les instancier dans la classe, et l’inversion des dépendances en rendant la classe dépendante des abstractions (interfaces et/ou classes abstraites) au lieu de classes concrètes. Cela signifie que la classe dépendante ne dispose d’aucune information sur la classe concrète qu’elle utilisera, et que les classes dont elle dépend ne font aucune référence au nom de la classe pleinement qualifiée.

De même, avoir des composants entièrement séparés signifie qu’un composant ne possède pas d’informations directes sur un autre composant. En d’autres termes, il n’a aucune référence à une unité de code à grain fin provenant d’un autre composant, même pas des interfaces ! Cela signifie que l’injection de dépendances et l’inversion de dépendance ne suffisent pas à séparer les composants, il nous faudra des structures architecturales. Nous pourrions avoir besoin d’événements, d’un noyau commun, d’une cohérence éventuelle, ou même d’un service de découverte !

Logique de déclenchement dans d’autres composants
Quand l’un de nos composants (le composant B) doit faire quelque chose alors qu’autre chose se produit dans un autre composant (composant A), nous ne pouvons pas faire d’appel direct du composant A vers une classe/méthode dans le composant B car alors A est concaténé. B.

Cependant, on peut faire en sorte que A utilise un répartiteur d’événements pour envoyer un événement d’application qui sera livré à n’importe quel composant qui l’écoute, y compris B, et l’écouteur d’événements dans B déclenchera l’action désirée. Cela signifie que le composant A sera connecté à un émetteur d’événement, mais sera séparé de B.

Pourtant, si l’événement lui-même « vit » dans A, cela signifie que B est conscient de l’existence de A, qu’il correspond à A. Pour éliminer cette dépendance, nous pouvons créer une bibliothèque avec un ensemble de fonctions principales de l’application à partager entre elles. tous les composants, Shared Core. Cela signifie que les deux composants dépendront du Noyau Partagé, mais ils seront séparés l’un de l’autre. Le Shared Core contiendra des fonctionnalités telles que les événements d’application et de domaine, mais il peut aussi contenir des objets de spécification et tout autre élément qui a du sens à partager ; Gardez à l’esprit que tout changement apporté au Noyau Partagé doit être aussi strict que possible, car ils affecteront tous ses composants. application. De plus, si nous avons un système multilingue, disons un écosystème de microservices où il est écrit dans différentes langues, le Shared Core doit être indépendant de la langue afin qu’il puisse être compris par tous les composants, quel que soit le langage dans lequel il est écrit. Par exemple, au lieu que le Shared Core contienne une classe d’événement, vous pouvez utiliser la description de l’événement (c’est-à-dire nom, propriétés, méthodes, bien que ces éléments soient peut-être plus utiles dans un objet Specification) dans un langage agnostique comme JSON, afin que tous les composants/microservices puissent l’interpréter et même construire automatiquement leurs propres applications concrètes. Lisez-en plus à ce sujet dans mon article suivant : Plus que des couches concentriques.

Explicti_arch_layers
Bu yaklaşım hem monolitik uygulamalarda hem de mikro hizmet ekosistemleri gibi dağıtılmış uygulamalarda çalışır. Ancak, olaylar yalnızca eşzamansız olarak iletilebildiğinde, diğer bileşenlerde tetikleme mantığının hemen yapılması gereken bağlamlar için bu yaklaşım yeterli olmayacaktır! Bileşen A’nın, bileşen B’ye doğrudan bir HTTP çağrısı yapması gerekecektir. Bu durumda, bileşenlerin ayrıştırılması için, A’nın istenen eylemi tetiklemek için isteği nereye göndermesi gerektiğini soracağı veya alternatif olarak ilgili hizmete vekalet edebilen ve sonunda istek sahibine bir yanıt geri gönderebilen keşif hizmetine yapılan istek. Bu yaklaşım, bileşenleri keşif hizmetine bağlayacak, ancak birbirlerinden ayrılmalarını sağlayacaktır.

Diğer bileşenlerden veri alma (Getting data from other components)
Gördüğüm kadarıyla, bir bileşenin “sahip olmadığı” verileri değiştirmesine izin verilmiyor, ancak herhangi bir veriyi sorgulaması ve kullanması sorun değil.

Bileşenler arasında paylaşılan veri depolama (Data storage shared between components)
Bir bileşenin başka bir bileşene ait verileri kullanması gerektiğinde, diyelim ki bir faturalandırma bileşeninin hesaplar bileşenine ait müşteri adını kullanması gerektiğinde, faturalama bileşeni, bu veriler için veri deposunu sorgulayacak bir sorgu nesnesi içerecektir. Bu basitçe, faturalandırma bileşeninin herhangi bir veri kümesi hakkında bilgi sahibi olabileceği, ancak “sahip olmadığı” verileri sorgular aracılığıyla salt okunur olarak kullanması gerektiği anlamına gelir.

Le stockage des données est séparé par composant
Dans ce cas, le même schéma s’applique, mais nous avons plus de complexité au niveau du stockage des données. Le fait que les composants disposent de leur propre stockage de données signifie que chaque stockage contient :

C’est le seul jeu de données qu’il possède et qu’il est autorisé à modifier, ce qui en fait la seule source de vérité ;
Un jeu de données qu’il ne peut pas modifier seul, mais qui est une copie d’autres données composantes essentielles à la fonctionnalité des composants et doit être mis à jour à chaque changement dans le composant propriétaire.
Chaque composant créera une copie locale des données dont il a besoin auprès des autres composants pour être utilisées selon les besoins. Lorsque les données du composant possédé changent, ce composant propriétaire déclenche un événement de domaine qui transporte les données. Les composants qui conservent une copie de ces données écouteront cet événement de domaine et mettront à jour leurs copies locales en conséquence.

Flux de contrôle
Comme je l’ai dit plus haut, le flux de contrôle va bien sûr de l’utilisateur vers le Cœur d’application, puis vers les outils d’infrastructure, puis de nouveau vers le Cœur d’Application, et enfin de retour à l’utilisateur. Mais comment exactement les cours s’entrelacent-ils ? Lesquels sont liés à quoi ? Comment les créer ?

Après Oncle Bob, j’essaierai d’expliquer le flux de contrôle avec des diagrammes UML dans son article sur l’architecture propre...

Sans bus de commandes/requêtes
Dans le cas où nous n’utilisons pas de bus de commandes, les contrôleurs dépendront soit d’un Service d’application, soit d’un objet de requête.

[ ÉDIT – 2017-11-18 ] J’ai complètement raté le DTO que j’utilisais pour retourner les données de la requête, donc je l’ai ajouté maintenant. Merci à la morphine administrée, ce qui me fait penser.

Dans le schéma ci-dessus, nous utilisons une interface pour le Service d’application, mais nous pouvons soutenir que le Service d’application n’est pas vraiment nécessaire car il fait partie de notre code applicatif, et que nous ne voulons peut-être pas le modifier pour une autre application malgré son refactorisation. Du début à la fin.

L’objet de requête contiendra une requête optimisée qui retournera simplement des données brutes qui seront affichées à l’utilisateur. Ces données seront retournées dans un DTO, qui sera injecté dans un ViewModel. ThisViewModel peut avoir une logique de vue à l’intérieur, et elle sera utilisée pour remplir une View.

Le Service d’application, en revanche, contiendra la logique du cas d’usage que nous déclencherons lorsque nous voulons faire quelque chose dans le système, au lieu d’afficher simplement des données. Les services applicatifs dépendent de dépôts qui retourneront l’Entité contenant la logique à déclencher. De plus, la coordination d’un processus de domaine entre plusieurs entités peut dépendre d’un service de domaine, mais ce n’est presque jamais le cas.

Après avoir ouvert le cas d’usage, le Service d’application peut vouloir informer l’ensemble du système que ce cas d’utilisation s’est produit ; Dans ce cas, un événement dépendra également de l’expéditeur pour déclencher l’événement.

Il est intéressant de noter que nous avons placé les interfaces à la fois dans le moteur de persistance et dans les dépôts. Bien que cela puisse sembler inutile, ils ont des objectifs différents :

L’interface de persistance est une couche d’abstraction sur l’ORM afin que nous puissions modifier l’ORM utilisé sans modifier le noyau de l’application.
L’interface du dépôt est une abstraction du moteur de persistance lui-même. Disons que nous voulons migrer de MySQL vers MongoDB. L’interface de persistance peut être la même, et même l’adaptateur de persistance restera le même si nous voulons continuer à utiliser le même ORM. Cependant, le langage de requête est complètement différent, donc nous pouvons créer de nouveaux dépôts utilisant le même mécanisme de persistance, implémenter les mêmes interfaces de dépôt, mais générer des requêtes en utilisant le langage de requête MongoDB au lieu de SQL.
Avec un bus de commandes/requêtes
Si notre application utilise un bus de commandes/requêtes, le diagramme reste à peu près le même, sauf que le contrôleur est désormais connecté au bus et à une commande ou requête. Il lance la commande ou la requête et la transmet au bus, qui trouve le gestionnaire approprié pour recevoir et traiter la commande.

Dans le diagramme suivant, le gestionnaire de commandes utilise alors un service d’application. Cependant, cela n’est pas toujours nécessaire, en fait, dans la plupart des cas, le gestionnaire contiendra toute la logique du cas d’usage. Si nous devons réutiliser la même logique dans un autre manipulateur, il suffit d’extraire la logique du gestionnaire vers un Service d’application séparé.

[ ÉDIT – 2017-11-18 ] J’ai complètement raté le DTO que j’utilisais pour retourner les données de la requête, donc je l’ai ajouté maintenant. Merci à la morphine administrée, ce qui me fait penser.

Vous avez peut-être remarqué qu’il n’y a aucune dépendance entre le bus et les commandes, requêtes ou gestionnaires. Cela s’explique par le fait qu’ils doivent ignorer l’un de l’autre pour réellement parvenir à une bonne séparation. La façon dont le bus sait quel gestionnaire doit gérer quelle commande ou requête doit être configurée uniquement avec la configuration.

Comme vous pouvez le voir, dans les deux cas, toutes les flèches qui traversent la frontière du noyau de l’application sont des dépendances vers l’intérieur. Comme expliqué précédemment, c’est la règle générale de l’architecture Ports and Adapters, de l’architecture Onion et de l’architecture Clean.

Conclusion)
L’objectif, comme toujours, est d’avoir une base de code faiblement couplée et hautement cohérente afin que les changements soient faciles, rapides et sécurisés.

Les plans ne valent rien, mais planifier est primordiale.

Eisenhower

Cette infographie est une carte conceptuelle. Connaître et comprendre tous ces concepts nous aidera à planifier une architecture saine et une application saine.

Cependant :

La carte ne représente pas la région.

Alfred Korzybski

Ce ne sont donc que des directives ! La pratique est le territoire, la réalité, le cas d’usage concret auquel nous devons appliquer nos connaissances, et c’est ce qui définira à quoi ressemblera la véritable architecture !

Nous devons comprendre tous ces schémas, mais nous devons aussi toujours penser et comprendre exactement ce dont notre pratique a besoin, jusqu’où nous avons encore à parcourir pour la décomposition et l’adaptation. Cette décision peut dépendre de nombreux facteurs, à commencer par les exigences fonctionnelles du projet, mais elle peut aussi inclure des facteurs tels que le délai de construction de l’application, la durée de vie de l’application, l’expérience de l’équipe de développement, etc.

C’est tout, c’est comme ça que je comprends tout. C’est comme ça que je rationalise ça dans ma tête.

J’ai développé un peu plus ces idées dans un article de suivi : Plus que de simples couches concentriques.

Cependant, comment pouvons-nous rendre tout cela explicite dans la base de code ? C’est le sujet de l’un de mes prochains articles : comment refléter l’architecture et le domaine dans le code.

Enfin, merci à mon collègue Francesco Mastrogiacomo de m’avoir aidé à rendre mon infographie magnifique.
