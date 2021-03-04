# contiendra le modèle préalablement entrainé
# à faire : importer le modèle et faire un predict

from joblib import load

def load_predict(text):
    """Loads the trained model 
    and predict tags from the text"""
    
    file_name = 'my_trained_model.model'
    print(file_name)
    #model = load(file_name)
    #tags = model.predict(text)
    tags = ['python', 'flask', 'nlp', 'summer']
    
    return tags