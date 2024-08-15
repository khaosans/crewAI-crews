import sqlite3
import csv
import random
from datetime import datetime, timedelta

from langchain_core.tools import tool


class SqlLite:

    @tool("Create TradingData table")
    def create_table(db_name="trading_data.db"):
        """
        Create the TradingData table in the specified SQLite database.

        Args:
            db_name (str): The name of the SQLite database file. Defaults to "trading_data.db".

        Returns:
            None
        """
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS TradingData (
                            id INTEGER PRIMARY KEY,
                            symbol TEXT,
                            date TEXT,
                            open REAL,
                            high REAL,
                            low REAL,
                            close REAL,
                            volume INTEGER)''')
        conn.commit()
        conn.close()

    @tool("Insert trading data")
    @staticmethod
    def insert_trading_data(id, symbol, date, open, high, low, close, volume, db_name="trading_data.db"):
        """
        Insert a new trading record into the TradingData table.

        Args:
            id (int): The unique identifier for the trading record.
            symbol (str): The trading symbol.
            date (str): The date of the trading record.
            open (float): The opening price.
            high (float): The highest price.
            low (float): The lowest price.
            close (float): The closing price.
            volume (int): The trading volume.
            db_name (str): The name of the SQLite database file. Defaults to "trading_data.db".

        Returns:
            None
        """
        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO TradingData (id, symbol, date, open, high, low, close, volume) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (id, symbol, date, open, high, low, close, volume))
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()


    @tool("Query database")
    def query_database(query: str, file_name: str, db_name="trading_data.db"):
        """
        Execute an SQL query and save the results to a CSV file.

        Args:
            query (str): The SQL query to execute.
            file_name (str): The name of the CSV file to save the results.
            db_name (str): The name of the SQLite database file. Defaults to "trading_data.db".

        Returns:
            list: A list of tuples containing the query results.
        """
        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]
            conn.close()

            with open(file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(column_names)  # Write the column headers
                writer.writerows(results)

            return results
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []