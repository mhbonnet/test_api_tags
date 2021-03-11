# API de test - proposition de tags   
En fonction de la question posée par l'utilisateur (titre et corps de texte), l'API retournera une liste de tags correspondants.  
  
  
## Mode opératoire :   
1 - cloner ce repository sur votre ordinateur   
2 - aller à l'adresse https://tags-api.herokuapp.com   
5 - saisissez votre question (titre et corps de texte) et appuyer sur le bouton 'soumettre'   
6 - le navigateur affiche les tags proposés pour votre question   

## Note d'avancement :   
A ce jour, le modèle retourne seulement si on attribue le tag 'python' ou pas.


## Librairies (requirements.txt)  
beautifulsoup4==4.9.3  
bs4==0.0.1  
click==7.1.2  
Flask==1.1.2  
itsdangerous==1.1.0  
Jinja2==2.11.3  
joblib==1.0.1  
lxml==4.6.2  
MarkupSafe==1.1.1  
nltk==3.5  
numpy==1.19.5  
regex==2020.11.13  
scikit-learn==0.24.1  
scipy==1.5.4  
sklearn==0.0  
soupsieve==2.2  
threadpoolctl==2.1.0  
tqdm==4.59.0  
Werkzeug==1.0.1  
gunicorn==20.0.4  