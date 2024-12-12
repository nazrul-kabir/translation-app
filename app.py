from flask import Flask, render_template, request, jsonify
from transformers import pipeline

# Initialize the translation pipeline
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fi")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    # Get the text from the request
    data = request.json
    text = data.get('text', '')
    
    # Perform translation
    translation = translator(text)[0]['translation_text']
    return jsonify({
        'translation': translation
    })

if __name__ == '__main__':
    app.run(debug=True)