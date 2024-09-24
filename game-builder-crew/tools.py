from langchain_experimental.utilities import PythonREPL
from crewai.tools import tool

@tool("Python REPL Tool")
def create_python_repl_tool():
    """A tool for running Python code."""
    return PythonREPL()

# Add more tools as needed