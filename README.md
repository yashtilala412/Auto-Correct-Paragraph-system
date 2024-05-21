# Sentence Correction Flask App

This Flask application corrects sentences by suggesting the most similar words from the English vocabulary based on Levenshtein distance. It uses NLP techniques to tokenize and tag parts of speech in sentences and suggests corrections for misspelled words.

## Features

- Tokenizes and tags parts of speech in sentences.
- Uses Levenshtein distance to suggest corrections for misspelled words.
- Ignores proper nouns to avoid incorrect suggestions.
- Provides a web interface to input paragraphs and receive corrected text.

## Requirements

- Python 3.8+
- Flask
- NLTK
- textdistance

## Installation
#import nltk
#nltk.download('words')
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/yourusername/sentence-correction-flask-app.git
cd sentence-correction-flask-app
