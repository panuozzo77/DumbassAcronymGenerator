# DumbassAcronymGenerator

## Description
The "dumbassAcronym" program is a Python application designed to generate acronyms based on user input words. It utilizes PDF documents to extract random words that match the initials of the input word, allowing users to interactively choose the best words to obtain creative acronyms.

## Project Focus
The primary objective of this project is to develop a software solution that operates seamlessly across languages utilizing the Latin alphabet. By leveraging the common characteristics of Latin-based languages, the "dumbassAcronym" program aims to provide a universal tool for generating acronyms that transcends linguistic barriers.



## Project Structure
- `pdfs/`: Directory containing PDF documents from which random words are extracted.
- `src/`: Directory containing the source code of the program.
  - `AcronymMaker.py`: Python script for generating acronyms based on user input.
  - `WordGenerator.py`: Python script for extracting random words from PDF documents.
  - `utils.py`: Utility functions used by the program.
  - `config.ini`: Configuration file specifying parameters like the number of words to search and the directory path for PDFs.

## Usage
1. Run `AcronymMaker.py` to initiate the program.
2. Enter a word for which an acronym will be generated.
3. Follow the prompts to select words starting with each letter of the input word.
4. Once all letters are processed, the program generates and displays the acronym.

## Dependencies
- PyMuPDF: A Python library for working with PDF files.

## Configuration
- Modify `config.ini` to change parameters like the number of words to search and the directory path for PDFs.

## Notes
- Ensure that PDF documents are placed in the `pdfs/` directory for word extraction.
- The program may require adjustments to handle cases where no words are found for certain letters.

