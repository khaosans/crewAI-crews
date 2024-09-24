import sqlite3

import chromadb
import pandas as pd


class DataIngestion:
    def __init__(self, data_source, db_path='local.db'):
        self.data_source = data_source
        self.db_path = db_path
        self.chroma_db = chromadb.Client()

    def load_data(self):
        # Example: Load data from a CSV file
        return pd.read_csv(self.data_source)

    @staticmethod
    def preprocess_data(data):
        return data.dropna()

    def save_to_sqlite(self, data):
        with sqlite3.connect(self.db_path) as conn:
            data.to_sql('chatbot_data', conn, if_exists='replace', index=False)

    def save_to_chromadb(self, data):
        # Example: Save data to ChromaDB
        for _, row in data.iterrows():
            self.chroma_db.add_document(row.to_dict())

    def load_from_sqlite(self):
        with sqlite3.connect(self.db_path) as conn:
            data = pd.read_sql('SELECT * FROM chatbot_data', conn)

        return data

    def load_from_chromadb(self):
        # Example: Load data from ChromaDB
        return self.chroma_db.get_all_documents()