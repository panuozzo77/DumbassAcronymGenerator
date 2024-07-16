"""
config.py

Utility script for loading configuration parameters from config.ini file.

Author: Cristian Porzio
License: MIT
"""

import configparser
from pathlib import Path
from src.utils.logger import log


def get_script_dir():
    """Return the absolute path to the directory containing the script."""
    return Path(__file__).resolve().parent


def get_project_root(script_dir):
    """Return the project root directory."""
    return script_dir.parent.parent


def get_config_path(script_dir):
    """Return the path to the config.ini file."""
    return script_dir / "config.ini"


def load_config(config_path):
    """Load and return the configuration parser object."""
    config = configparser.ConfigParser()
    config.read(config_path)
    return config


def get_pdf_directory(project_root, config):
    """Return the path to the PDF directory."""
    directory_path = project_root / "pdfs"
    if not directory_path.exists():
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

    directory_path_config = config.get('paths', 'directory_path', fallback=None)
    if directory_path_config:
        directory_path = Path(directory_path_config)

    return directory_path


def load():
    """
    Load general configuration parameters from config.ini file.

    Returns:
        num_words_to_search (int): Number of words to search for.
        directory_path (Path): Path to the directory containing PDF documents.
    """
    script_dir = get_script_dir()
    project_root = get_project_root(script_dir)
    config_path = get_config_path(script_dir)
    config = load_config(config_path)

    num_words_to_search = config.getint('numbers', 'num_words_to_search')
    directory_path = get_pdf_directory(project_root, config)

    return num_words_to_search, directory_path


def load_database_credentials():
    """
    Load database credentials from config.ini file.

    Returns:
        username (str): Username for the database.
        ip (str): IP address of the database.
        password (str): Password for the database.
    """
    script_dir = get_script_dir()
    config_path = get_config_path(script_dir)
    config = load_config(config_path)

    username = config.get('database', 'username')
    ip = config.get('database', 'ip')
    password = config.get('database', 'password')

    return username, ip, password
