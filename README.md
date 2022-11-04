`Python : Exemples illustrant l'usage contextuel des patrons de conception`

# Creational Design Patterns - Patron de conception créative
Les patrons de création fournissent divers mécanismes de création d'objets, qui augmentent la `flexibilité` et la 
`réutilisation` du code existant d'une manière adaptée à la situation. Cela donne au programme plus de flexibilité pour 
décider quels objets doivent être créés pour un cas d'utilisation donné.
- [ ] `Abstract Factory - Usine abstraite`
  + Dans ce modèle, une interface crée des ensembles ou des familles d'objets connexes sans spécifier le nom de la classe.
- [ ] `Builder - Constructeur`
  + Il permet la production de différents types et représentations d'un objet en utilisant le même code de construction. 
  + Il est utilisé pour la création étape par étape d'un objet complexe en combinant des objets simples. La création finale 
  des objets dépend des étapes du processus de création mais est indépendante des autres objets.
- [ ] `Factory - Usine`
  + Fournit une interface pour la création d'objets dans une superclasse mais permet aux sous-classes de modifier le type 
  d'objets créés. Fournit l'instanciation implicite d'objets à travers des interfaces communes. 
- [ ] `Prototype`
  + Il vous permet de copier des objets existants sans faire dépendre votre code de leurs classes. Il est utilisé pour 
  limiter les opérations de mémoire/base de données en gardant la modification au minimum en utilisant des copies d'objets.
- [ ] `Singleton`
  + Ce modèle de conception limite l'instanciation d'une classe à un seul objet. 

# Structural Design Patterns - Patron de conception structurel
Ils fournissent des solutions efficaces et des normes sur les compositions de classes et les structures d'objets. 
Le concept d'héritage est utilisé pour composer des interfaces et définir des façons de composer des objets pour 
obtenir de nouvelles fonctionnalités.

- [ ] `Adapter - Adaptateur`
  + Il est utilisé pour relier deux interfaces qui ne sont pas compatibles et utiliser leurs fonctionnalités. 
  + L'adaptateur permet aux classes de travailler ensemble d'une manière qu'elles ne pourraient pas faire puisqu'il 
    s'agit d'interfaces incompatibles.
- [ ] `Bridge - Pont`
  + Dans ce patron, il y a une modification structurelle des classes principale et d'implémentation d'interface sans 
    qu'il y ait d'effet entre elles. Ces deux classes peuvent être développées indépendamment et ne sont connectées 
    qu'en utilisant une interface comme pont.
- [ ] `Composite`
  + Il est utilisé pour regrouper des objets en un seul objet. Il permet de composer des objets en arborescence et de 
    travailler ensuite avec ces structures comme s'il s'agissait d'objets individuels. 
- [ ] `Decorator - Décorateur`
  + Ce motif limite la modification de la structure de l'objet tout en lui ajoutant de nouvelles fonctionnalités. 
  + La classe initiale reste inchangée, tandis qu'une classe décoratrice fournit des capacités supplémentaires. 
- [ ] `Facade - Façade`
  + Fournit une interface simplifiée à une bibliothèque, un framework ou tout autre ensemble complexe de classes.
- [ ] `Flyweight`
  + Le modèle Flyweight est utilisé pour réduire l'utilisation de la mémoire et améliorer les performances en réduisant 
    la création d'objets. 
  + Le modèle recherche des objets similaires qui existent déjà pour les réutiliser au lieu de créer de nouveaux objets similaires. 
- [ ] `Proxy`
  + Il est utilisé pour créer des objets qui peuvent représenter des fonctions d'autres classes ou objets, et 
    l'interface est utilisée pour accéder à ces fonctionnalités. 

# Behavioral Design Patterns - Patrons de conception du comportement
- [ ] `Chain of Responsability - Chaîne de responsabilité`
  + Le design pattern Chaîne de responsabilité est un pattern de comportement qui évite de coupler l'émetteur d'une requête 
    à son récepteur, donnant ainsi à plusieurs objets la possibilité de répondre à une requête.
- [ ] `Command - Commande`
  + Transforme une requête en un objet distinct qui contient toutes les informations relatives à la requête. Cette 
    transformation vous permet de paramétrer des méthodes avec différentes requêtes, de retarder ou de mettre en file 
    d'attente l'exécution d'une requête, et de prendre en charge des opérations qui ne peuvent pas être annulées. 
- [x] [`Depedency injection - Injection de dépendance`](https://en.wikipedia.org/wiki/Dependency_injection) 
  + En génie logiciel, l'injection de dépendances est un modèle de conception dans lequel un objet ou une fonction 
    reçoit d'autres objets ou fonctions dont il dépend. 
  + Ce modèle garantit qu'un objet ou une fonction qui souhaite utiliser un service donné ne doit pas savoir comment 
    construire ces services. 
  + Au lieu de cela, le "client" récepteur (objet ou fonction) reçoit ses dépendances par un code externe (un "injecteur"), 
    dont il n'a pas connaissance :
    - Comment une classe peut-elle être indépendante de la création des objets dont elle dépend ?
    - Comment une application, et les objets qu'elle utilise, peuvent-ils supporter différentes configurations ?
    - Comment modifier le comportement d'un morceau de code sans l'éditer directement ?
  + Il y a 5 façons principales, en Python, dont un client peut recevoir des services injectés :
    - [x] `Injection de constructeur`, où les dépendances sont fournies par le constructeur de classe d'un client.
    - [x] `Injection de function par typage des canards`, où le client expose une méthode qui accepte la dépendance sans
           se soucier de savoir s'il est un canard, mais se soucie uniquement de savoir s'il fait coin-coin.
    - [x] `Injection de classe de base`, où la classe de base de la dépendance fournit une méthode d'injection que la 
      dépendance utilisera par héritage.
    - [x] `Injection d'interfaces ou de classe de base abstraite`, où l'interface ou a classe de base abstraite de la 
      dépendance fournit une signature d'injection que la dépendance implémentera
    - [x] `Sans injection de dépendance`, où le client construit et contrôle directement le Service dans le constructeur
          créant ainsi une dépendance codée en dur.
- [ ] `Interpreter - Interprète`
  + Utilisé pour évaluer un langage ou une expression lors de la création d'une interface qui indique le contexte pour l'interprétation. 
- [ ] `Iterator - Itérateur`
  + Son utilité permet d'accéder de manière séquentielle à de nombreux éléments présents dans un objet de collection 
    sans effectuer d'échange d'informations pertinent. 
- [ ] `Mediator - Médiateur`
  + Ce patron permet de communiquer facilement à travers votre classe, ce qui permet la communication entre plusieurs classes. 
- [ ] `Memento`
  + Le motif Memento vous permet de parcourir en boucle les éléments d'une collection sans exposer leur représentation sous-jacente. 
- [ ] `Observer`
  + Il permet de définir un mécanisme d'abonnement pour notifier divers objets de tout événement survenant à l'objet observé. 
- [ ] `State - État`
  + Dans le pattern state, le comportement d'une classe varie en fonction de son état et est donc représenté par l'objet context. 
- [ ] `Strategy - Stratégie`
  + Il permet de définir une famille d'algorithmes, mais ceux-ci se trouvent dans une classe distincte et rendent leurs 
    objets interchangeables. 
- [ ] `Template Method - Méthode modèle`
  + Utilisé avec des composants qui ont des similitudes où vous pouvez mettre en œuvre un modèle de code pour tester 
    les deux composants. Le code peut être changé avec des modifications mineures. 
- [ ] `Visitor - Visiteur`
  + Un pattern Visitor vise à définir une nouvelle opération sans apporter de modifications à une structure d'objet existante.  
