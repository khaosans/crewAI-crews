from crewai_tools import tool
from langchain_experimental.utilities import PythonREPL
import os

@tool("Python REPL Tool")
def create_python_repl_tool():
    """A tool for running Python code."""
    return PythonREPL()

# Add more tools as needed
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

