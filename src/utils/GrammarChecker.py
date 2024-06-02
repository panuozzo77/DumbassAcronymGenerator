"""
GrammarChecker.py

Python script for analyzing the grammatical structure of Italian words using spaCy.

Author: Cristian Porzio
License: MIT
"""

import spacy

# python -m spacy download it_core_news_sm

# Load the Italian model
nlp = spacy.load("it_core_news_sm")

# Global verbosity toggle
verbose = True

def log(message):
    """
    Log a message if verbosity is enabled.

    Args:
        message (str): The message to log.
    """
    if verbose:
        print(message)

class GrammarChecker:
    """
    Class for analyzing the grammatical structure of Italian words.
    """

    def analyze(self, word):
        """
        Analyze the grammatical structure of a given word.

        Args:
            word (str): The word to analyze.

        Returns:
            tuple: A tuple containing the type, genre, and number of the word.
        """
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
    # Example usage
    gc = GrammarChecker()
    type, genre, number = gc.analyze("correre")
    print(type == "VERB")
