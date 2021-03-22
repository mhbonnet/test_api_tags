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
nltk.download('wordnet')


def convert_tags(text):
    """functions made to 'protect' tags from prepocess
    returns a word transformed to be preprocessed
    used especially pour tags presents in body"""
    
    text = text.replace("c#", "csharp")
    text = text.replace('c++','cplusplus')
    text = text.replace('.net','dotnet')
    text = text.replace('.js','dotjs')
    text = text.replace('js','jstag')
    text = text.replace('css','csstag')
    text = text.replace('ios','iostag')
    text = text.replace('windows','windowstag')
    return text

def reverse_convert_tags(text):
    """functions made to go back to original tags from words transformed
    returns the original tag before preprocess transformation """
    
    text = text.replace("csharp", "c#")
    text = text.replace('cplusplus', 'c++')
    text = text.replace('dotnet', '.net')
    text = text.replace('dotjs', '.js')
    text = text.replace('jstag', 'js')
    text = text.replace('csstag', 'css')
    text = text.replace('iostag', 'ios')
    text = text.replace('windowstag', 'windows')
    return text

def preprocess_words_lemm(text, list_sw):
    """The input is a single string
    the output is a single string = words concatenated"""

    text1 = convert_tags(text)
    text2 = BeautifulSoup(text1).get_text().lower()
    text3 = text2.replace('-', '')
    text3 = re.sub("[^a-zA-Z0-9]",   " ",  text3)  
    text3 = re.sub(r' \d*', ' ', text3)
    words = text3.split()                             

    sw = set(list_sw)
    interest_words = [w for w in words if not w in sw]
    
    lemmatizer = WordNetLemmatizer() 
    words_lem = [lemmatizer.lemmatize(w) for w in interest_words]
    return( " ".join(words_lem))

def get_main_tags(model, probas, prob_threshold=0):
    """in case of a model returning the classes and their probabilities,
    returns the 5 most probable tags with probability > threshold"""
    
    tags_out = model['clf'].classes_
    
    ind = np.argpartition(probas[0], -5)[-5:]
    best_tags = pd.DataFrame(columns=['indice', 'tag', 'proba'])
    best_tags.indice = ind
    best_tags.proba = np.round(probas[0][ind]*100, 1)
    best_tags.tag = [tags_out[i] for i in best_tags.indice] 

    # only keep tags with probas > threshold
    best_tags = best_tags[best_tags.proba > prob_threshold]
    best_tags.sort_values(by=['proba'], ascending=False, inplace=True)
    return best_tags

def load_predict(text, tag_string):
    """Loads the trained model 
    and predict tags from the text"""

    # build stopwords custom list
    list_sw = stopwords.words("english")
    list_sw.extend(['want', 'would', 'use', 'way', 'new', 'one', 'need',
                    'like', 'using', 'get'])

    # preprocess text
    clean_text = preprocess_words_lemm(text, list_sw)

    # load trained model
    model = load('./model/pipeline_logistic_reg_multinom.joblib')
    model_probas = True
    
    # predict with 'predict_proba' (multi value) or 'predict' (one value)
    if model_probas:
        probas = model.predict_proba([text])
        main_tags = get_main_tags(model, probas)
        predicted = main_tags.tag.tolist()
    else:
        predicted = model.predict([text])
        predicted = predicted[0].tolist()
    
    predicted = [reverse_convert_tags(w) for w in predicted]
    return predicted