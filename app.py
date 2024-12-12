from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import traceback

# Initialize the translation pipeline
try:
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fi")
except Exception as e:
    print("Error loading translation model:")
    print(traceback.format_exc())
    translator = None

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    # Check if translator is loaded
    if translator is None:
        return jsonify({
            'success': False,
            'error': 'Translation model could not be loaded'
        }), 500

    # Get the text from the request
    data = request.json
    text = data.get('text', '')
    
    try:
        # Perform translation
        translation = translator(text)[0]['translation_text']
        return jsonify({
            'success': True,
            'translation': translation
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)