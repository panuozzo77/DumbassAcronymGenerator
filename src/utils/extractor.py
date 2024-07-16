"""
extractor.py

Utility script for extracting random words from PDF documents.

Author: Cristian Porzio
License: MIT
"""

import os
import fitz  # PyMuPDF
import random
from src.utils.logger import log as log


def get_pdf_page_count(pdf_path):
    """
    Get the number of pages in a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        int: Number of pages in the PDF file.
    """
    try:
        doc = fitz.open(pdf_path)
        num_pages = doc.page_count
        return num_pages
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return 0


def extract_text_from_page(pdf_path, page_number):
    """
    Extract text from a specific page of a PDF document.

    Args:
        pdf_path (str): Path to the PDF document.
        page_number (int): Page number to extract text from.

    Returns:
        str: Text extracted from the specified page.
    """
    try:
        doc = fitz.open(pdf_path)
        if page_number < 0 or page_number >= doc.page_count:
            raise ValueError(f"Page number {page_number} is out of range for the document {pdf_path}.")
        page = doc.load_page(page_number)
        text = page.get_text()
        return text
    except Exception as e:
        print(f"Error extracting text from page {page_number} of {pdf_path}: {e}")
        return ""


def extract_words_from_random_page(pdf_path):
    """
    Extract words from a random page of a PDF document.

    Args:
        pdf_path (str): Path to the PDF document.

    Returns:
        str: Text extracted from the random page.
    """
    doc = fitz.open(pdf_path)
    random_page_number = random.randint(0, get_pdf_page_count(pdf_path) - 1)
    log(f"extracting from pdf:{os.path.basename(pdf_path)} at page {random_page_number}")
    page = doc.load_page(random_page_number)
    text = page.get_text()
    return text


# Define words_found as a global variable
words_found = set()


def filter_words_by_initial_and_length(words, letter, min_length=4):
    """
    Filter words by initial letter and minimum length.

    Args:
        words (list): List of words to filter.
        letter (str): Initial letter to filter by.
        min_length (int): Minimum length of words to include.

    Returns:
        list: Filtered list of words.
    """
    return [word for word in words if word.lower().startswith(letter) and len(word) >= min_length and word.isalpha()]


def extract_random_word(words_filtered):
    """
    Extract a random word from a list of filtered words.

    Args:
        words_filtered (list): List of filtered words.

    Returns:
        str: Random word from the list.
    """
    random_index = random.randint(0, len(words_filtered) - 1)
    return words_filtered[random_index]


def process_pdf_file(pdf_path, letter):
    """
    Process a PDF file and extract words starting with a given letter.

    Args:
        pdf_path (str): Path to the PDF file.
        letter (str): Initial letter to filter words by.

    Returns:
        list: List of words starting with the given letter.
    """
    text = extract_words_from_random_page(pdf_path)
    words = text.split()
    return filter_words_by_initial_and_length(words, letter)


def find_random_words_by_initial(letter, directory, num_words):
    """
   Find random words starting with a given letter from PDF documents in a directory.

   Args:
       letter (str): Initial letter to filter words by.
       directory (str): Path to the directory containing PDF documents.
       num_words (int): Number of words to find.

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
                    random_word = extract_random_word(words_filtered)
                    words_found.add(random_word)
                    log(f"added: '{random_word}' ({len(words_found)}/{num_words})")
                else:
                    attempts += 1
                    log(f"No words found for {letter.capitalize()} remaining attempts: {str(max_attempts - attempts)}")

    words_found_list = list(words_found)
    words_found.clear()

    return words_found_list
