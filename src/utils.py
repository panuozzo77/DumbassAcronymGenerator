import os
import fitz  # PyMuPDF
import random
import configparser
from pathlib import Path

# Determine the absolute path to the directory containing the script
def load_config():
    script_dir = Path(__file__).resolve().parent

    # Construct the path to the config.ini file
    config_path = script_dir / "config.ini"

    # Initialize the ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read(config_path)

    # Now you can access the values in the config.ini file
    num_words_to_search = config.getint('numbers', 'num_words_to_search')
    directory_path = config.get('paths', 'directory_path')
    return num_words_to_search, directory_path


def extract_words_from_random_page(pdf_path):
    doc = fitz.open(pdf_path)
    num_pages = doc.page_count
    random_page_number = random.randint(0, num_pages - 1)
    page = doc.load_page(random_page_number)
    text = page.get_text()
    return text

# Define words_found as a global variable
words_found = set()

def find_random_words_by_initial(letter, directory, num_words):
    global words_found  # Declare words_found as a global variable

    attempts = 0
    max_attempts = 10  # Set a maximum number of attempts

    # Continue looping until the number of unique words found reaches num_words or max_attempts is reached
    while len(words_found) < num_words and attempts < max_attempts:
        for filename in os.listdir(directory):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(directory, filename)
                text = extract_words_from_random_page(pdf_path)
                words = text.split()
                # Filter words that start with the specified letter and are longer than or equal to 4 characters
                words_filtered = [word for word in words if word.lower().startswith(letter) and len(word) >= 4 and word.isalpha()]

                if words_filtered:
                    # Pick a random number of words from this list
                    while len(words_found) < num_words:
                        random_index = random.randint(0, len(words_filtered) - 1)
                        random_word = words_filtered[random_index]

                        words_found.add(random_word)
                else:
                    attempts += 1
                    # Uncomment the following line if you want to print a message when no words are found
                    print("No words found for " + letter, "remaining attempts: " + str(max_attempts - attempts))

    # Convert the set to a list before returning
    words_found_list = list(words_found)
    # Clear words_found for the next iteration
    words_found.clear()

    return words_found_list

