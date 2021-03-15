# -*- coding: utf-8 -*-

import json
from flask import Flask, request, render_template, jsonify
from functions import find_tags

app = Flask(__name__)

# Avec Flask, les décorateurs sont utilisés pour 
# associer une URL à une fonction. 
# Exemple : fonction welcome associée à l’URL /

@app.route('/', methods=['GET', 'POST'])
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

@app.route('/api/', methods=['POST'])
def analyse_text():
    
    data = json.loads(request.data)
    
    my_title = data['title']
    my_body = data['body']
    tags = find_tags(my_title, my_body)
    print(type(tags))
    
    return jsonify(status='ok', tags=tags)

   
if __name__ == "__main__":
    app.run(debug=True)