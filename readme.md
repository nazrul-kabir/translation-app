# English to Finnish Translation App

## Overview
A simple Flask web application that translates English to Finnish using Hugging Face's Transformers library.

## Prerequisites
- Python 3.9+
- pip
- Virtual Environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nazrul-kabir/translation-app.git
cd translation-app
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv translation_env
translation_env\Scripts\activate

# On macOS/Linux
python3 -m venv translation_env
source translation_env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application
```bash
python app.py
```

Navigate to `http://localhost:5000` in your web browser.

## Dependencies
- Flask
- Transformers
- SentencePiece
- Torch