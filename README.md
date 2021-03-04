# API de test - proposition de tags
En fonction de la question posée par l'utilisateur (titre et corps de texte), l'API retournera une liste de tags correspondants.

## Pré-requis
Installer python 3.8 et les librairies suivantes (dernières versions) : Flask, BeautifulSoup, NLTK, Spacy (ainsi que les librairies standard numpy et pandas).

## Mode opératoire :
1 - cloner ce repository sur votre ordinateur
2 - en ligne de commande, déplacez-vous dans le répertoire créé
3 - saisissez la commande 'python tags_api.py' (pour lancer le serveur en local)
4 - dans un navigateur, saisissez l'adresse "127.0.0.1:5000/tags_api"
5 - saisissez votre question (titre et corps de texte) et appuyer sur le bouton 'soumettre'
6 - le navigateur affiche les tags proposés pour votre question