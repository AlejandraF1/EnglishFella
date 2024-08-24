from flask import Flask, render_template, request, jsonify
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
    return render_template('synonyms.html', synonyms=synonyms, show_results=True)

@app.route('/api/search', methods=['GET'])
def search():
    search_query = request.args.get('q')
    synonyms = chatbot_synonyms(search_query)
    return jsonify(synonyms)

if __name__ == '__main__':
    app.run(debug=True)