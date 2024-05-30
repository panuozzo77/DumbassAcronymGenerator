import functools

import utils as util


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
        self.num_words, self.path = util.load_config()
        print("Initializing WordGenerator from config.ini")
        print("Number of words for letter: {}".format(self.num_words))
        print("Path for scanning PDFs: {}".format(self.path))

    def get_max_words(self):
        return self.num_words

    @validate_letter
    def find_words_starting_with(self, letter):
        word_list = util.find_random_words_by_initial(letter, self.path, self.num_words)

        print("Words found starting with", letter.capitalize(), ":")
        print(word_list)

        return word_list


#gen = WordGenerator()
#gen.find_words_starting_with('A')
