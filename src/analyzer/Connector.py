import mysql.connector
from mysql.connector import Error
from src.utils.config import load_database_credentials


class Connector:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        """
        Create a database connection using credentials from config.ini.

        Returns:
            bool: True if connection successful, False otherwise.
        """
        try:
            username, ip, password, database = load_database_credentials()

            self.connection = mysql.connector.connect(
                host=ip,
                user=username,
                password=password,
                database=database
            )
            if self.connection.is_connected():
                print("Connected to the database")
                self.cursor = self.connection.cursor()
                return True
        except Error as e:
            print(f"Error connecting to the database: {e}")
            return False

    def disconnect(self):
        """
        Disconnect from the database.
        """
        try:
            if self.connection and self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                print("Disconnected from the database")
        except Error as e:
            print(f"Error disconnecting from the database: {e}")

    def table_exists(self, table_name):
        """
        Check if a table exists in the database.

        Args:
            table_name (str): Name of the table to check.

        Returns:
            bool: True if the table exists, False otherwise.
        """
        query = f"SHOW TABLES LIKE '{table_name}'"
        self.cursor.execute(query)
        return bool(self.cursor.fetchone())

    def create_table(self, table_name):
        """
        Create a new table in the database for storing words.

        Args:
            table_name (str): Name of the table to create.
        """
        try:
            query = f"CREATE TABLE {table_name} (word VARCHAR(255) PRIMARY KEY, type VARCHAR(50), gender VARCHAR(50), number VARCHAR(50), mode VARCHAR(50), tense VARCHAR(50), person VARCHAR(50), frequency INT DEFAULT 1)"
            self.cursor.execute(query)
            self.connection.commit()
            print(f"Table '{table_name}' created successfully")
        except Error as e:
            print(f"Error creating table '{table_name}': {e}")

    def insert_word(self, table_name, word, type_, gender, number, mode, tense, person):
        """
        Insert a word into the specified table in the database.

        Args:
            table_name (str): Name of the table to insert into.
            word (str): Word to insert.
            type_ (str): Type of the word (e.g., NOUN, VERB).
            gender (str): Gender of the word.
            number (str): Number of the word (e.g., Sing, Plur).
            mode (str): Mode of the word (for verbs).
            tense (str): Tense of the word (for verbs).
            person (str): Person of the word (for verbs).
        """
        try:
            query = f"INSERT INTO {table_name} (word, type, gender, number, mode, tense, person, frequency) VALUES (%s, %s, %s, %s, %s, %s, %s, 1) ON DUPLICATE KEY UPDATE frequency = frequency + 1"
            params = (word, type_, gender, number, mode, tense, person)
            self.cursor.execute(query, params)
            self.connection.commit()
            print(f"Inserted word '{word}' into table '{table_name}'")
        except Error as e:
            print(f"Error inserting word '{word}' into table '{table_name}': {e}")
