# -*- coding: utf-8 -*-

import re
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from joblib import load
nltk.download('stopwords')

tag_string = 'python'

def preprocess_words(text):
    """Cleans the text provided and
    returns a string containing all the meaningful words"""
    sw = set(stopwords.words("english"))   
    
    text1 = BeautifulSoup(text, 'lxml').get_text()    
    text2 = re.sub("[^a-zA-Z]", " ", text1) 
    words = text2.lower().split()                                     
    interest_words = [w for w in words if not w in sw]

    return( " ".join(interest_words))  


def load_predict(text, tag_string):
    """Loads the trained model 
    and predict tags from the text"""
    # preprocess text
    clean_text = preprocess_words(text)
        
    # model = pipeline tfidf vectorizer + classifier
    model = load('./model/pipeline_forest.joblib') 
    
    # prédictions
    predicted = model.predict([text])
    if predicted == 1:
        return 'Tag {} : oui'.format(tag_string)
    else:
        return 'Tag {} : non'.format(tag_string)