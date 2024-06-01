"""
logger.py

Utility script for logging messages.

Author: Cristian Porzio
License: MIT
"""

# Global verbosity toggle
verbose = False


# Helper function for logging
def log(message):
    """
    Log a message if verbosity is enabled.

    Args:
        message (str): Message to log.
    """
    if verbose:
        print(message)