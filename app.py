from flask import Flask, render_template, request, url_for
from preprocess import word_extractor, symptoms
from predict import predictor
#import pyrebase
import pandas as pd



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/symp_check')
def sym():
    return render_template('symp_check.html')

@app.route('/ab')
def about():
    return render_template('about.html')

input_text = ''

@app.route('/your-disease', methods=['POST'])
def home_post():
    if request.method == 'POST':
        text = request.form.get('symptoms_input')
        words = word_extractor(text)
        final_symptoms = symptoms(words)
        global input_text
        input_text = text
    
    return render_template('confirm_symptoms.html', text = text, words=words,final_symptoms = final_symptoms)

@app.route('/your-disease-re', methods=['POST'])
def home_repost():
    if request.method == 'POST':
        final_symptoms = request.form.getlist('disease_checkbox')
        diseases = predictor(final_symptoms)
    return render_template('disease.html',final_symptoms = final_symptoms, diseases=diseases)

if __name__ == '__main__':
                 from waitress import serve
                 app.run()
