# -*- coding: utf-8 -*-

import json
import requests
from flask import Flask, request

app = Flask(__name__)

# Avec Flask, les décorateurs sont utilisés pour 
# associer une URL à une fonction. Ici, on associe 
# donc la fonction  welcome  à l’URL /
@app.route("/")
def welcome():
    return "Welcome to the test api!"

@app.route('/tags_api', methods=['GET', 'POST'])
def form_extract():
    # POST request (après action submit)
    if request.method == 'POST':
        titre = request.form.get('title_input')
        question = request.form.get('body_input')
        tags = ['html', 'css', 'flask', 'json', 'api']
        return '''
                  <h3>Titre = {}</h3>
                  <p>{}</p>
                  <h1>Tags proposés :</h1>
                  <p>{}</p>'''.format(titre, question, tags)

    # GET request (formulaire)
    return '''
              <form method="POST">
                  <div>
                  <label>Titre: <input type="text" name="title_input" required
       minlength="2" maxlength="256" size="50"</label></div>
                  <div><label>Question:  <textarea name="body_input" rows="10" cols="100"></textarea></label></div>
                  <input type="submit" value="Soumettre">
              </form>'''

if __name__ == "__main__":
    app.run(debug=True)