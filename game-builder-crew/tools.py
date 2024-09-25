from crewai_tools import tool
from langchain_experimental.utilities import PythonREPL
import os

@tool("Python REPL Tool")
def create_python_repl_tool():
    """A tool for running Python code."""
    return PythonREPL()
#