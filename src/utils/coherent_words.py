import os
from src.utils.GrammarChecker import GrammarChecker
from src.utils.extractor import process_pdf_file
from src.utils.logger import log as log


def extract_coherent_words(words_filtered, previous_word):
    checker = GrammarChecker()
    type, genre, number = checker.analyze(previous_word)
    if (type is not "VERB"):
        '''TODO words must be filtered matching the genre and number'''
    else:
        '''TODO words should not be verbs'''


def find_words(letter, directory, num_words, previous_word=None):
    """
   Find random words starting with a given letter from PDF documents in a directory.

   Args:
       letter (str): Initial letter to filter words by.
       directory (str): Path to the directory containing PDF documents.
       num_words (int): Number of words to find.
       previous_word (str): previous chosen word to filter words by.

   Returns:
       list: List of random words starting with the given letter.
   """
    global words_found  # Declare words_found as a global variable

    attempts = 0
    max_attempts = 10  # Set a maximum number of attempts

    # Continue looping until the number of unique words found reaches num_words or max_attempts is reached
    while len(words_found) < num_words and attempts < max_attempts:
        for filename in os.listdir(directory):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(directory, filename)
                words_filtered = process_pdf_file(pdf_path, letter)

                if words_filtered:
                    random_word = extract_coherent_words(words_filtered, previous_word)
                    words_found.add(random_word)
                    log(f"added: '{random_word}' ({len(words_found)}/{num_words})")
                else:
                    attempts += 1
                    log(f"No words found for {letter.capitalize()} remaining attempts: {str(max_attempts - attempts)}")

    words_found_list = list(words_found)
    words_found.clear()

    return words_found_list
