# DumbassAcronymGenerator

## Description
The "dumbassAcronym" program is a Python application designed to generate acronyms based on user input words. It utilizes PDF documents to extract random words that match the initials of the input word, allowing users to interactively choose the best words to obtain creative acronyms.

## Project Focus
The primary objective of this project is to develop a software solution that operates seamlessly across languages utilizing the Latin alphabet. By leveraging the common characteristics of Latin-based languages, the "dumbassAcronym" program aims to provide a universal tool for generating acronyms that transcends linguistic barriers.


## Project Structure
- `pdfs/`: Directory containing PDF documents from which words are extracted.
- `README.md`: Markdown file containing information about the project.
- `requirements.txt`: Text file listing the Python dependencies required by the project.
- `src/`: Directory containing the source code of the program.
  - `executable/`: Directory containing executable Python scripts.
    - `AcronymMaker.py`: Python script for generating acronyms based on user input.
    - `WordGenerator.py`: Python script for extracting random words from PDF documents.
  - `GrammarChecker.py`: Python script for checking grammar.
  - `utils/`: Directory containing utility scripts and configuration files.
    - `config.ini`: Configuration file specifying parameters like the number of words to search, the directory path for PDFs and DB credentials
     [follow this](https://i_dont_know.io) for details.
    - `config.py`: Python script for loading configuration from `config.ini`.
    - `extractor.py`: Python script for extracting words from PDF documents.
    - `logger.py`: Python script for logging messages.

## Usage
1. Run `AcronymMaker.py` to initiate the program.
2. Enter a word for which an acronym will be generated.
3. Follow the prompts to select words starting with each letter of the input word.
4. Once all letters are processed, the program generates and displays the acronym.

## Dependencies
- PyMuPDF: A Python library for working with PDF files.
- watch also [requirements.txt](https://i_dont_know.io)

## Configuration
- Modify `config.ini` to change parameters like the number of words to search and the directory path for PDFs [follow this](https://i_dont_know.io).

## Notes
- If no other paths have been inserted into config.ini ensure that PDF documents are placed in the `pdfs/` directory for word extraction. 
- The program may require adjustments to handle cases where no words are found for certain letters.

