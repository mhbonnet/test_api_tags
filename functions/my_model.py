# prediction tags à partir modèle pré entrainé
from joblib import load

def load_predict(clean_text, tag_string):
    
    """Loads the trained model 
    and predict tags from the text"""
    # récupération modele = pipeline tfidf vectorizer + modele
    model = load('./model/pipeline_forest.joblib') 
    
    # prédictions
    predicted = model.predict([clean_text])
    if predicted == 1:
        return 'Tag {} : oui'.format(tag_string)
    else:
        return 'Tag {} : non'.format(tag_string)