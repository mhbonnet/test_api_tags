# API de test - proposition de tags   
En fonction de la question posée par l'utilisateur (titre et corps de texte), l'API retournera une liste de tags correspondants.  
  
  
## Mode opératoire :   
Cloner ce repository sur votre ordinateur.    

Deux modes de test sont disponibles :  
1   - aller à l'adresse https://tags-api.herokuapp.com    
    - saisissez votre question (titre et corps de texte) et appuyer sur le bouton 'soumettre'   
    - le navigateur affiche les tags proposés pour votre question   
    
2   - dans le fichier direct_api.py, saisissez un titre et un texte à tester  
    - en ligne de commande, lancez python direct_api.py  
    - les tags attribués si visibles dans la console  

## Note d'avancement :   
A ce jour, le modèle retourne seulement si on attribue le tag 'python' ou pas.

## Librairies : voir requirements.txt