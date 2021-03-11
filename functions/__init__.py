# -*- coding: utf-8 -*-

import re
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from functions.my_model import load_predict

nltk.download('stopwords')

def preprocess_words(text):
    """Cleans the text provided and
    returns a string containing all the meaningful words"""

    # 1. enlever html
    text1 = BeautifulSoup(text, 'lxml').get_text() 
    
    # 2. on ne garde que lettres (pas ponctuation/chiffres)     
    text2 = re.sub("[^a-zA-Z]", " ", text1) 

    # 3. minuscules et découpage en mots
    words = text2.lower().split()                             
    
    # 4. stopwords : conversion set (rapidité) + enlever
    sw = set(stopwords.words("english"))                  
    interest_words = [w for w in words if not w in sw]
    
    # 6. Join the words back into one string separated by space, 
    # and return the result.
    return( " ".join(interest_words))  


def find_tags(title=None, body=None):
    """Process the title and body provided
    Returns the proposed tags"""
    clean_title = preprocess_words(title)
    clean_body = preprocess_words(body)

    tags = load_predict(clean_title + clean_body, 'python')
    return tags