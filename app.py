from flask import Flask, render_template, request
import re
import nltk
from nltk.corpus import words
import textdistance
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('words')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

app = Flask(__name__)

english_vocab = set(words.words())

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return 'a'  # Adjective
    elif tag.startswith('V'):
        return 'v'  # Verb
    elif tag.startswith('N'):
        return 'n'  # Noun
    elif tag.startswith('R'):
        return 'r'  # Adverb
    else:
        return None

def correct_sentence(sentence):
    words_in_sentence = word_tokenize(sentence)
    pos_tags = pos_tag(words_in_sentence)
    
    corrected_sentence = []
    for word, tag in pos_tags:
        wordnet_pos = get_wordnet_pos(tag)
        if wordnet_pos and word not in english_vocab and tag != 'NNP':  # Exclude proper nouns
            similarities = [(w, textdistance.Jaccard(qval=2).distance(w, word)) for w in english_vocab]
            suggestions = sorted(similarities, key=lambda x: x[1])[:3]  # Get top 3 similar words
            best_suggestion = min(suggestions, key=lambda x: x[1])[0]  # Get the most similar word
            corrected_sentence.append(best_suggestion)
        else:
            corrected_sentence.append(word)  # Keep correct words as is
    return ' '.join(corrected_sentence)

def correct_paragraph(paragraph):
    sentences = nltk.sent_tokenize(paragraph)
    corrected_sentences = [correct_sentence(sentence) for sentence in sentences]
    return ' '.join(corrected_sentences)

@app.route('/')
def index():
    return render_template('index.html', suggestion=None)

@app.route('/suggest', methods=['POST'])
def suggest():
    paragraph = request.form.get('paragraph')  # Change 'sentence' to 'paragraph'
    if paragraph:
        corrected_paragraph = correct_paragraph(paragraph)
        return render_template('index.html', suggestion=corrected_paragraph)
    else:
        return render_template('index.html', suggestion="Please enter a paragraph.")

if __name__ == '__main__':
    app.run(debug=True)
