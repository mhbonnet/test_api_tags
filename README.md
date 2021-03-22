# API de test - proposition de tags   
En fonction de la question posée par l'utilisateur (titre et corps de texte), l'API retournera une liste de tags correspondants.  
  
  
## Mode opératoire :   
Cloner ce repository sur votre ordinateur.    

Trois modes de test sont disponibles :  

1. Saisir manuellement un titre et une question via un formulaire : 
    - aller à l'adresse https://tags-api.herokuapp.com/
    - saisir la question (titre et corps de texte) et appuyer sur le bouton 'soumettre'   
    - le navigateur affiche les tags proposés sous forme de liste
    
2. Envoyer une requête POST directement à l'API : 
    - url = "https://tags-api.herokuapp.com/api/"
    - dict = {'title': a_title, 'body': a_body}
    - headers = {'Content-type': 'application/json'}
    - response = requests.post(url, json=dict, headers=headers)
    - les tags proposés se trouvent dans le champ 'text' de la réponse
    
    voir un exemple dans le fichier example_api.py (retour de l'API lisible dans la console)

3. Appeler le modèle directement sans passer par l'API :
    - importer la fonction : from functions import find_tags
    - définir les titres et corps de la question (texte libre) : a_title, a_body
    - appeler la fonction : tags = find_tags(a_title, a_body)

## Librairies nécessaires : voir requirements.txt