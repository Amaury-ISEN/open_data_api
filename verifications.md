Pour vérifier nos endpoints, nous avons utilisé Swagger intégré à FastAPI via le /docs à ajouter après l'url de notre API. Cela s'est révélé efficace pour tester la majorité des endpoints à l'exception de ceux qui rendaient les JSON les plus volumineux, plus précisément ceux qui rendaient tous les documents pour une région ou pour une région et une filière. On a utilisé Insomnia pour ceux-là.

**Vérification pour la consommation d'une filière pour un département :**
![consodepfil](https://user-images.githubusercontent.com/73169069/109512014-f2669880-7aa3-11eb-8888-9d3c30da6ebf.png)

**Vérification pour la consommation d'une filière :**
![consofil](https://user-images.githubusercontent.com/73169069/109512084-01e5e180-7aa4-11eb-85bd-b26d62205269.png)

**Vérification pour le PUT :**
1) création d'un document dummy :
![dummy1pourPUT](https://user-images.githubusercontent.com/73169069/109512216-26da5480-7aa4-11eb-95ef-46fb141eff7f.png)
2) modification via swagger :
![put](https://user-images.githubusercontent.com/73169069/109512238-2e016280-7aa4-11eb-9eaf-197f4e78e858.png)
3) vérification que le dummy a changé :
![dummy2pourPUT](https://user-images.githubusercontent.com/73169069/109512262-348fda00-7aa4-11eb-8617-e0b959eb93ed.png)

**Supression d'un document :**
1) On regarde un document de test, il existe bien en base :
![test_suppr1](https://user-images.githubusercontent.com/73169069/109514106-f5fb1f00-7aa5-11eb-9110-874da688f4ec.png)
2) On le supprime avec l'endpoint via swagger :
![test_suppr2](https://user-images.githubusercontent.com/73169069/109514113-f693b580-7aa5-11eb-964f-fa33881a4c5a.png)
3) On vérifie en base, il a bien été supprimé :
![test_suppr3](https://user-images.githubusercontent.com/73169069/109514115-f72c4c00-7aa5-11eb-8233-80d701cede74.png)


Pour vérifier les endpoints qui rendent des documents en masse, nous avons dû essayer diverses solutions autres que Swagger, par exemple Postman. La seule assez robuste s'est révélée être Insomnia.

Il y a d'ailleurs un warning sur la taille du JSON de résultat mais il suffit de l'ignorer :
![insomniawarning](https://user-images.githubusercontent.com/73169069/109512324-45d8e680-7aa4-11eb-94a7-4173089907f9.png)

**Vérification pour les documents d'une filière et d'une région :**
![docs_filiere_et_region](https://user-images.githubusercontent.com/73169069/109512516-7882df00-7aa4-11eb-80b8-da41114991ae.png)

**Vérification pour les documents d'une région :**
![docs_region](https://user-images.githubusercontent.com/73169069/109512554-80428380-7aa4-11eb-92b2-1d7bd4f40e29.png)
