# Projet-info-2A

Lien vers le rapport : 
https://fr.overleaf.com/2923467794gxmkhbfwrvrt 

Remarques Laurène (20/10)
- J'ai ajouté un fichier requirement.txt comme dans les TP pour lister les modules utilisés
- regrouper les diagrammes (et les trier) dans un dossier UML ?
 
Retour du tuteurs:

14/10
- cas d'utilisation : limiter le nombre de granularités (ajouter/supprimer à regrouper)
- diagramme de classes : 
    - meta types : plutot une liste de types que d'id_types
    - manque attribut dictionnaire dans les classes
    - moins de fonctions : add/delete ça suffit
- rapport : id_meta_type à détailler un peu plus
- diag de package : une flèche dans le mauvais sens



[dimanche 22:42] BRUNETTI Antoine
Bonjour j'ai fait une revue un peu tardive de vos diagrammes :

## Diagramme de cas d'utilisation
- Definir des champs
Dans l'include, vous préciserez bien que "type" correspond a des valeurs brutes ou a des types renseignés en amont de la demande
- fournir un fichier de règle de base
Ceci n'est pas un cas d'utilisation, en effet le fichier est déjà chargé au démarrage de l'appli et donc il n'y a pas d'action de l'utilisateur en ce sens. Cela pourrait être un cas d'utilisation d'un acteur "système", mais pas nécessaire de le rajouter honnêtement. Il faut juste garder en tête que c'est effectivement un besoin pour la cible.
- Définir des schémas 
A part la typo sur l'espace, c'est bien
- Générer une table de données aléatoires
Ok, mais une question, lorsque vous générez des données est ce que vous avez prévu d'inclure l'accès a ces données dans le cas d'utilisation ou plutôt dans un autre? Si vous n'aviez pas prévu l'accès aux données dans ce cas il faut rajouter un autre
- Exporter des tables sous différents formats 
Ici c'est ok, mais que l'on soit bien d'accord, il s'agit d'exports sous format JSON ou CSV des jeux de données déjà générés. La consultation des données est en soi un prérequis et n'est pas un "export" vu que compris dans l'application.

## Diagramme de classes
Rappel : j'avais indiqué que je souhaitais globalement une modélisation objet, mais que j'acceptais que vous procédiez de manière itérative, en me présentant un diagramme de classes évolutives :).
### JSON dict builder
> Donc dans l'idée il s'agirait d'un catalogue de classe qui pourraient manipuler un dictionnaire (donc un champ dictionnaire manquant?). Ce dictionnaire correspondant aux métadonnées permettant la génération de données.
L'idée d'une classe, est d'organiser une forte cohésion et un faible couplage. Dans cette idée,  add_type, delete_type, add_modality, clear_dict, delete_modality ont du sens lorsqu'ils modifient et définissent un comportement interne, mais ne touchent pas a des objets externes (auquel cas l'on ne profite pas des propriétés de l'objet). En ce sens, ces classes ont plus de sens en tant que fonctions de la classe PrintDict.
Autre point : la gestion des types - ici il semble prévu d'ajouter une modalité a un type - str, je ne sais pas si vous avez prévu de gérer l'ajout de modalité a un type par référence au nom du type, mais c'est globalement plutôt pénible a gérer (surtout dans la compréhension et l'articulation du code). 
Point optionnel mais a retenir si vous changiez pour de l'objet : il faut se rappeler que les intéractions entre plusieurs objets seront préférablement gérées dans des classes de services a part, donc qu'il est profitable de mettre au maximum des types de haut niveau (encore une fois fort cohésion et bonnes propriétés de refactor).
### Import
Classe contenant un chemin et une méthode import_dict() => de part sa nature d'impact externe, cela est une classe de service donc la résultante est la création d'un objet PrintDict() 
### Export 
Pareil que pour import, c'est une bonne idée de variabiliser cela ainsi, du coup pour la partie interne, ici on pourra proposer 3 implémentations d'une classe abstraite, c'est effectivement une bonne manière de traiter de multiples implémentations d'un besoin. L'utilisation se fera donc au moyen d'un factory sur la demande de l'utilisateur.
### Generation de données
Je ne vois pas trop ce qu'est "mq" mais sinon dans l'idée il y a un dict (j'imagine schéma des données) et un nombre de lignes qu'on veut générer, et a partir des 2 on génère un autre dict jeu de données, cela peut effectivement se modéliser ainsi :). Pour le coup, si vous souhaitez sauvegarder vos jeux de données et y accéder il faudra potentiellement penser une gestion externe de cette partie. (via un DAO qui associe un id a un JSON ça se stocke en bdd)






