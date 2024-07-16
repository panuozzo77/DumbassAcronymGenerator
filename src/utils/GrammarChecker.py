"""
GrammarChecker.py

Python script for analyzing the grammatical structure of Italian words using spaCy.

Author: Cristian Porzio
License: MIT
"""

import spacy
from logger import log, verbose

# python -m spacy download it_core_news_sm

# Load the Italian model
nlp = spacy.load("it_core_news_sm")

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
            list: A list of dictionaries containing the analysis results.
        """
        doc = nlp(word)
        analysis_results = []

        for token in doc:
            morph = token.morph.to_dict()
            type_ = token.pos_
            genre = morph.get('Gender', 'N/A')
            number = morph.get('Number', 'N/A')

            log(f"Parola: {token.text}")
            log(f"Tipo: {type_}")

            analysis_result = {
                'word': token.text,
                'type': type_,
                'gender': genre,
                'number': number,
                'mode': morph.get('VerbForm', 'N/A') if type_ == 'VERB' else 'N/A',
                'tense': morph.get('Tense', 'N/A') if type_ == 'VERB' else 'N/A',
                'person': morph.get('Person', 'N/A') if type_ == 'VERB' else 'N/A'
            }

            if type_ == 'VERB':
                log(f"Modo: {analysis_result['mode']}")
                log(f"Tempo: {analysis_result['tense']}")
                log(f"Persona: {analysis_result['person']}")

            log(f"Genere: {genre}")
            log(f"Numero: {number}")

            analysis_results.append(analysis_result)

        return analysis_results


if __name__ == "__main__":
    # Set verbosity
    verbose = True

    # Example usage
    gc = GrammarChecker()

    words_to_analyze = ["correre", "abaco", "Marco", "giallo", "del", "la", "uno", "di"]
    for word in words_to_analyze:
        analysis = gc.analyze(word)
        for result in analysis:
            print(result)
