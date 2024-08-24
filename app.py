from flask import Flask, render_template, request
import nltk
from nltk.corpus import wordnet

app = Flask(__name__)

# Función para obtener sinónimos
def chatbot_synonyms(palabra):
    sinonimos = []
    synsets = wordnet.synsets(palabra)
    for synset in synsets:
        for lemma in synset.lemmas():
            sinonimos.append(lemma.name())
    return sinonimos

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/synonyms', methods=['POST'])
def get_synonyms():
    user_input = request.form['user_input']
    synonyms = chatbot_synonyms(user_input)
    return render_template('synonyms.html', synonyms=synonyms)

if __name__ == '__main__':
    app.run(debug=True)