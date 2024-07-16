import os
from src.utils.config import load
from src.utils.extractor import get_pdf_page_count, extract_text_from_page
from src.analyzer.Connector import Connector
from src.utils.GrammarChecker import GrammarChecker


def process_pdfs():
    # Load configuration parameters
    num_words_to_search, directory_path = load()

    # Validate directory path
    if not directory_path.exists():
        print(f"The directory '{directory_path}' does not exist.")
        return

    # Initialize Connector for database interaction
    connector = Connector()
    if not connector.connect():
        print("Failed to connect to the database.")
        return

    grammar_checker = GrammarChecker()

    try:
        # Loop through all PDF files in the directory
        for filename in os.listdir(directory_path):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(directory_path, filename)
                print(f"Processing PDF: {pdf_path}")

                # Get number of pages in the PDF
                num_pages = get_pdf_page_count(pdf_path)
                print(f"Number of pages: {num_pages}")

                # Extract and process text from each page
                for page_number in range(num_pages):
                    text = extract_text_from_page(pdf_path, page_number)
                    print(f"Extracted text from page {page_number + 1}:")
                    print(text)
                    print("-" * 50)

                    # Split text into words
                    words = text.split()

                    # Analyze each word with GrammarChecker
                    for word in words:
                        analysis_results = grammar_checker.analyze(word)

                        # Insert words into respective tables based on type
                        for result in analysis_results:
                            type_ = result['type']
                            word_to_insert = result['word'].lower()
                            gender = result['gender']
                            number = result['number']
                            mode = result['mode']
                            tense = result['tense']
                            person = result['person']

                            # Check if the table exists for the type, create if not
                            if not connector.table_exists(type_):
                                connector.create_table(type_)

                            # Insert the word into the respective table
                            connector.insert_word(type_, word_to_insert, type_, gender, number, mode, tense, person)

    except Exception as e:
        print(f"Error processing PDFs: {e}")

    finally:
        # Disconnect from the database
        connector.disconnect()


if __name__ == "__main__":
    process_pdfs()
