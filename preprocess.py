import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import difflib

import pandas as pd
df_train = pd.read_csv('dataset/Testing.csv', delimiter=',')
vocab = df_train.columns.tolist()

def word_extractor(sentence):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens =tokenizer.tokenize(sentence)
    tokens=[token.lower() for token in tokens]
    tokens = [token for token in tokens if not token in stopwords.words()]
    return tokens

#Symptoms suggestion

def symptoms(symptoms):
    final_symptoms = []
    final_symptoms_flat = []
    df_train = pd.read_csv('dataset/Testing.csv', delimiter=',')
    vocab = df_train.columns.tolist()
    for symptom in symptoms:
        final_symptoms.append(difflib.get_close_matches(symptom, vocab, cutoff=0.6))
    for sublist in final_symptoms:
        for item in sublist:
            if item not in final_symptoms_flat :
                final_symptoms_flat.append(item)       
    return final_symptoms_flat


def confirm_symptom():
    confirm_symptom=[]
    data=str(input("Confirm your symptom:"))
    confirm_symptom=data.split(",")
    return confirm_symptom
            

#print(symptoms(input("Describe your symptoms: ")))

##print(symptoms(word_extractor(input("Symptoms:"))))
#from predict import predictor
#print(predictor((confirm_symptom())))

