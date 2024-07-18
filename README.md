# DumbassAcronymGenerator

## Description
DumbassAcronym is a Python application designed for generating creative acronyms based on user-input words. The application leverages PDF documents to extract random words matching the initials of the input word, enabling users to select suitable words interactively.

In addition to its core functionality, the application includes a feature for analyzing the frequency of words found within loaded PDFs. Future plans for the project involve assigning scores to words, potentially highlighting those deemed more humorous or suitable for generating entertaining acronyms.

The application is currently tailored for use with the Italian language.

## Project Focus
The primary objective of this project is to develop a software solution that operates seamlessly across languages utilizing the Latin alphabet. By leveraging the common characteristics of Latin-based languages, the "dumbassAcronym" program aims to provide a universal tool for generating acronyms that transcends linguistic barriers.

## Features
- Acronym Generation: Generate acronyms using randomly extracted words from PDF documents given a word.
- Word Frequency Analysis: Analyze and count the occurrence of words within PDF files.
- Interactive Selection: Users can interactively choose words to form acronyms based on their chosen word.

# work in progress, the informations down below are not yet updated 

## Project Structure
- `pdfs/`: Directory containing PDF documents from which words are extracted.
- `README.md`: Markdown file containing information about the project.
- `requirements.txt`: Text file listing the Python dependencies required by the project.
- `src/`
  - `analyzer/`: Directory containing analysis-related scripts.
    - `Connector.py`: Python script for connecting to databases or other services.
    - `wordCounter.py`: Python script for counting occurrences of words in text.
  - `executable/`: Directory containing executable Python scripts.
    - `AcronymMaker.py`: Python script for generating acronyms based on user input.
    - `WordGenerator.py`: Python script for extracting random words from PDF documents.
    - `GrammarChecker.py`: Python script for checking grammar.
  - `utils/`: Directory containing utility scripts and configuration files.
    - `coherent_words.py`: Python script for determining coherence between words.
    - `config.ini`: Configuration file specifying parameters like the number of words to search, the directory path for PDFs, and database credentials.
    - `config.py`: Python script for loading configuration from config.ini.
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
- If no other paths have been inserted into config.ini ensure that PDF documents are placed in the `dumbassAcronym/pdfs/` directory for word extraction. 
- The program may require adjustments to handle cases where no words are found for certain letters.

