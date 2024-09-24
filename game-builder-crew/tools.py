import os
import datetime
import sqlite3
import requests
import chromadb
from crewai.tools import tool
from langchain_experimental.utilities import PythonREPL

# Initialize ChromaDB client
client = chromadb.Client()

# Create a collection for storing knowledge in ChromaDB
knowledge_collection = client.create_collection("knowledge_base")


# --------- TOOL DEFINITIONS ---------

@tool("Python REPL Tool")
def create_python_repl_tool():
    """A tool for running Python code."""
    return PythonREPL()


@tool("Web Search Tool")
def web_search(query):
    """A tool for performing web searches using GitHub's repository search."""
    url = f"https://api.github.com/search/repositories?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [
            {"name": repo["name"], "description": repo["description"]}
            for repo in data["items"]
        ]
    return f"Error: {response.status_code} - {response.text}"


@tool("Database Connection Tool")
def create_database_connection(db_name):
    """A tool for connecting to a SQLite database."""
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        return f"Error connecting to database: {e}"


@tool("API Interaction Tool")
def api_interaction(url, method='GET', data=None):
    """A tool for making API calls (GET/POST)."""
    try:
        if method == 'GET':
            response = requests.get(url)
        elif method == 'POST':
            response = requests.post(url, json=data)
        else:
            return "Unsupported method"

        return response.json()
    except Exception as e:
        return f"Error: {str(e)}"


@tool("Logging Tool")
def logging_tool(message):
    """A tool for logging messages."""
    print(f"LOG: {message}")


@tool("Testing Framework Tool")
def run_tests(test_cases):
    """A tool for running tests on the code."""
    results = {}
    for test in test_cases:
        try:
            exec(test)
            results[test] = "Passed"
        except Exception as e:
            results[test] = f"Failed: {str(e)}"
    return results


@tool("RAG Tool")
def rag_tool(query):
    """A tool for retrieving knowledge using RAG (ChromaDB)."""
    return knowledge_collection.query(query)


@tool("Code Saver Tool")
def code_saver(filename, code):
    """A tool for saving code to a specified file."""
    save_path = "/Users/Sour/agent-code-folder"  # Ensure this path is correct
    try:
        os.makedirs(save_path, exist_ok=True)  # Ensure the directory exists
        file_path = os.path.join(save_path, filename)
        with open(file_path, 'w') as file:
            file.write(code)
        return f"Code saved to {filename}."
    except Exception as e:
        return f"Error saving code: {e}"
    
