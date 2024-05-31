import spacy
import argparse

# python -m spacy download it_core_news_sm

# Load the italian model
nlp = spacy.load("it_core_news_sm")

# Global verbosity toggle
verbose = True

def log(message):
    if verbose:
        print(message)

def analyze_word(word):
    doc = nlp(word)
    for token in doc:
        morph = token.morph.to_dict()
        type = token.pos_
        genre = morph.get('Gender', 'N/A')
        number = morph.get('Number', 'N/A')

        log(f"Parola: {token.text}")
        log(f"Tipo: {type}")
        if type == 'VERB':

            modo = morph.get('VerbForm', 'N/A')
            tempo = morph.get('Tense', 'N/A')
            persona = morph.get('Person', 'N/A')
            log(f"Modo: {modo}")
            log(f"Tempo: {tempo}")
            log(f"Persona: {persona}")
        log(f"Genere: {genre}")
        log(f"Numero: {number}")

        return type, genre, number

if __name__ == "__main__":
    #parser = argparse.ArgumentParser(description='Analizzatore morfologico per parole italiane.')
    #parser.add_argument('parola', type=str, help='La parola da analizzare')
    #args = parser.parse_args()
    analyze_word("rincorrere")
