"""
connector.py

Utility script for interacting with MySQL database.

Author: Cristian Porzio
License: MIT
"""

import mysql.connector
from mysql.connector import Error
from src.utils.config import load_database_credentials


class Connector:
    def __init__(self):
        self.connection = None

    def connect(self):
        """
        Create a database connection using credentials from config.ini.

        Returns:
            bool: True if connection is successful, False otherwise.
        """
        username, ip, password, database = load_database_credentials()

        try:
            self.connection = mysql.connector.connect(
                host=ip,
                user=username,
                password=password,
                database=database
            )
            if self.connection.is_connected():
                print("Connected to the database")
                return True
        except Error as e:
            print(f"Error connecting to the database: {e}")
            return False

    def disconnect(self):
        """
        Disconnect from the database.
        """
        if self.connection:
            self.connection.close()
            print("Disconnected from the database")

if __name__ == "__main__":
    # Use to check if the connection to the database works

    Connector().connect()
