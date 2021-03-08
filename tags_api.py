# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from functions import find_tags

app = Flask(__name__)

# Avec Flask, les décorateurs sont utilisés pour 
# associer une URL à une fonction. 
# Exemple : fonction welcome associée à l’URL /
@app.route("/")
def welcome():
    return "Welcome to the test api!\
    <p>Type the address : http://127.0.0.1:5000/tags_api\
     or click here : <a href=\"http://127.0.0.1:5000/tags_api\">Test</a>"

@app.route('/tags_api', methods=['GET', 'POST'])
def form_extract():
    # POST request
    if request.method == 'POST':
        titre = request.form.get('title_input')
        question = request.form.get('body_input')      
        tags = find_tags(titre, question)
        
        return render_template('tags_answer.html',
                               title=titre,
                               body=question,
                               tags=tags)

    # GET request ou erreur
    return render_template('tags_form.html')
   
if __name__ == "__main__":
    app.run(debug=True)