"""
AcronymMaker.py

Python script for generating acronyms based on user input words.

Author: Cristian Porzio
License: MIT
"""

from src.executable.WordGenerator import WordGenerator


class AcronymMaker:
    """
    Class for generating acronyms based on user input words.
    """

    def __init__(self, generator):
        """
        Initialize AcronymMaker with a WordGenerator instance.

        Args:
            generator (WordGenerator): WordGenerator instance to find words starting with given letters.
        """
        self.word_generator = generator

    def make_acronym(self):
        """
        Create an acronym based on user input words.

        Prompts the user to input a word, finds words starting with each letter of the word,
        and constructs an acronym from the chosen words.
        """
        word = input("Enter a word to make an acronym with: ").lower()

        acronym = []
        for letter in word:
            valid_word = False
            words_found = self.word_generator.find_words_starting_with(letter)
            while not valid_word:
                if words_found:
                    print(f"Words found starting with '{letter.capitalize()}':")
                    for i, word in enumerate(words_found, 1):
                        print(f"{i}. {word}")
                    choice = input(f"Choose a word for letter '{letter.capitalize()}': ")
                    if choice.isdigit() and 1 <= int(choice) <= len(words_found):
                        chosen_word = words_found[int(choice) - 1]
                        acronym.append(chosen_word)
                        acronym.append(" ")
                        valid_word = True
                    else:
                        print("Invalid choice. Please choose a valid number.")
                else:
                    print(f"No words found starting with '{letter.capitalize()}'. Please choose another letter.")
                    break

        if acronym:
            print(f"This acronym stands for:", ''.join(acronym).upper())
        else:
            print("No words found to create an acronym.")


# Example usage
word_generator = WordGenerator()
acronym_maker = AcronymMaker(word_generator)
acronym_maker.make_acronym()
