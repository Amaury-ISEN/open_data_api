# open_data_api
Api opendata avec utilisation de FastApi côté serveur


# Contexte du projet

Vous travaillez pour une ONG qui veut centraliser toutes les données open data sur l'environnement. L'objectif est double : retraiter ces données, trouver des corrélations, permettant de proposer des solutions pour l'environnement et mettre à disposition toutes ces données, le résultat de ces traitements, au plus grand nombre.

Votre mission est de vous consacrer au deuxième objectif : mettre à disposition les données au plus grand nombre. Pour ça vous aller développer et tester une API REST sur un premier dataset et proposer une ébauche de portail opendata. Ce premier test doit permettre de décider si cette solution est celle à retenir, avant d'investir dans des recrutements de dev et dans l'infrastructure.

# Modalités pédagogiques

Le brief est a réaliser en équipe de 2 ou 3 apprenants. Vous avez 3 jours pour :

créer une base Mongo à partir des données récupérer sur le portail open data de l'agence ORE (profiter en pour regarder ce que peut proposer un portail open data),
le dataset à récupérer est la Consommation annuelle d’électricité et gaz par IRIS et par code NAF pour 2019
Créer une API REST
Créer un portail de test avec quelques menus interactifs (par exemple, on clique sur une région pour afficher la consomation locale ou sur un fournisseur...)
Ce portail doit aussi afficher un graphique représentant la consommation des deux filières pour une région choisie.
Tous les endpoints de votre API doivent être testé avec un outil comme SWAGGER et vous devez utiliser un outil comme TRELLO pour vous répartir les tâches.

Les endpoints demandés sont :

  les données pour une filière (soit gaz, soit électricité),
  les données pour une région,
  les données pour une filière et une région,
  la consommation total pour une filière,
  supprimer un document précis,
  modifier un document précis,
  la consommation d'une filière pour un département
  
  
# Critères de performance

Tous les endpoints de l'API REST doivent fonctionner. Tous les endpoints doivent être testés. Le portail test doit afficher le graphique demandé et être dynamique. Le travaille doit être organisé sur un trello qui montre précisément les tâches réalisées par chaque membre de l'équipe.

# Modalités d'évaluation

Le brief sera défendu lors d'une présentation orale de 10 min, qui se compose en 3 parties :

  démonstration de l'API REST grâce à un outil comme SWAGGER,
  démonstration du portail test, pour montrer comment accéder à l'API REST,
  explication de l'organisation du travail à partir du trello.
  Livrables
  Lien vers le dépôt github qui contient le code pour les 2 appli, les captures d'écran des tests API et le lien vers le TRELLO utilisé pour le travail d'équipe.


