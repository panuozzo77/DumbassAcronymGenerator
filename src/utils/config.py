import configparser
from pathlib import Path
from src.utils.logger import log

# Determine the absolute path to the directory containing the script
def load():
    script_dir = Path(__file__).resolve().parent

    # Navigate up one level from src to the project root
    project_root = script_dir.parent.parent

    # Construct the path to the pdfs directory in the project root
    directory_path = project_root / "pdfs"

    # Ensure the directory exists
    if not directory_path.exists():
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

    # Construct the path to the config.ini file
    config_path = script_dir / "config.ini"

    # Initialize the ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read(config_path)

    # Access the values in the config.ini file
    num_words_to_search = config.getint('numbers', 'num_words_to_search')

    # Get the directory path if provided, otherwise use the default path
    directory_path_config = config.get('paths', 'directory_path', fallback=None)
    if directory_path_config:
        directory_path = Path(directory_path_config)

    return num_words_to_search, directory_path
