# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import re
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from joblib import load
nltk.download('stopwords')

def preprocess_words_lemm(text):
    """Cleans the text provided and
    returns a string containing all the meaningful words"""
    
    text1 = BeautifulSoup(text, 'lxml').get_text()
    text2 = text1.replace("c#", "csharp")
    text2 = text2.replace('c++','cplusplus')
    text2 = text2.replace('.net','dotnet')
    text3 = re.sub("[^a-zA-Z]", " ", text2) 
    words = text3.lower().split()                             

    list_sw = stopwords.words("english")
    list_sw.extend(['want', 'would', 'use', 'way', 'new', 'one', 'code', 'need',
                    'like' ,  'using', 'file', 'string', 'get', 'error' ])
    sw = set(list_sw)
    interest_words = [w for w in words if not w in sw]
    
    lemmatizer = WordNetLemmatizer() 
    words_lem = [lemmatizer.lemmatize(w) for w in interest_words]
    
    return( " ".join(words_lem))  

def get_main_tags(model, probas):
    """in case of a model returning the classes and their probabilities,
    returns the 5 most probable tags"""
    
    tags_out = model['clf'].classes_
    
    ind = np.argpartition(probas[0], -5)[-5:]
    best_tags = pd.DataFrame(columns=['indice', 'tag', 'proba'])
    best_tags.indice = ind
    best_tags.proba = np.round(probas[0][ind]*100, 1)
    best_tags.tag = [tags_out[i] for i in best_tags.indice] 
    best_tags.sort_values(by=['proba'], ascending=False, inplace=True)
    return best_tags.tag.tolist()

def load_predict(text, tag_string):
    """Loads the trained model 
    and predict tags from the text"""
    # preprocess text
    clean_text = preprocess_words_lemm(text)
        
    # model = pipeline tfidf vectorizer + classifier
    model = load('./model/pipeline_logistic_reg_multinom.joblib') 
    model_probas = True
    
    # prédictions
    if model_probas:
        probas = model.predict_proba([text])
        predicted = get_main_tags(model, probas)

    else:
        predicted = model.predict([text])
        predicted = predicted[0].tolist()

    return predicted