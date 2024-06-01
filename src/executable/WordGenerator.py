import functools
from src.utils import config as config
from src.utils import extractor as pdf
from src.utils.logger import log as log


def validate_letter(func):
    @functools.wraps(func)
    def wrapper(self, letter):
        # Check if the letter is a valid lowercase letter
        if not letter.isalpha():
            raise ValueError("Invalid character. Only letters are allowed.")
        if letter.isupper():
            return func(self, letter.lower())
        else:
            return func(self, letter)

    return wrapper


class WordGenerator:
    def __init__(self):
        self.num_words, self.path = config.load()
        log("Initializing WordGenerator from config.ini")
        log("Number of words for letter to search: {}".format(self.num_words))
        log("Path for scanning PDFs: {}".format(self.path))

    def get_max_words(self):
        return self.num_words

    @validate_letter
    def find_words_starting_with(self, letter):
        word_list = pdf.find_random_words_by_initial(letter, self.path, self.num_words)

        log(f"Words found starting with {letter.capitalize()}:")
        log(word_list)

        return word_list


