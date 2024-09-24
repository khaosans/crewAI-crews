import logging
import os
from textwrap import dedent

from crewai import Agent  # Ensure crewai is installed
from crewai_tools import CSVSearchTool, RagTool  # Ensure crewai-tools is installed
from langchain_community.llms.ollama import Ollama  # Ensure langchain-community is installed
from langchain_core.tools import Tool  # Ensure langchain-core is installed
from langchain_experimental.utilities import PythonREPL  # Ensure langchain-experimental is installed

# Hardcoded path for saving code
CODE_SAVE_PATH = "/Users/Sour/agent-code-folder"

# Ensure the directory exists
os.makedirs(CODE_SAVE_PATH, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename='agent_logs.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


class ChatbotAgents:
    def __init__(self):
        self.Ollama = Ollama(model="Llama3.1")  # Ensure Ollama is initialized
        self.python_repl = PythonREPL()
        self.repl_tool = Tool(
            name="python_repl",
            description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
            func=self.python_repl.run,
        )
        self.csv_search_tool = CSVSearchTool()
        self.knowledge_retriever_tool = RagTool()

    def lead_developer_agent(self):
        logging.info("Creating Lead Developer Agent")
        return Agent(
            role='Lead Developer',
            goal='Design and architect software systems, including file structure and necessary files.',
            backstory=dedent(
                rf"""\
                A seasoned architect with a deep understanding of modern software development.
                You lead the team in making scalable and maintainable decisions.
                All code will be saved to the hardcoded path: {CODE_SAVE_PATH}. Do not change this path.
                """
            ),
            llm=self.Ollama,
            tools=[self.repl_tool, self.csv_search_tool, self.knowledge_retriever_tool, self.code_saver_tool],
            allow_delegation=False,
            verbose=True,
        )

    def code_reviewer_agent(self):
        logging.info("Creating Code Reviewer Agent")
        return Agent(
            role='Code Reviewer',
            goal='Ensure code quality and adherence to best practices',
            backstory=dedent(
                r"""\
                You have an eye for detail and are relentless in your pursuit of clean, efficient code.
                """
            ),
            llm=self.Ollama,
            tools=[self.repl_tool, self.csv_search_tool, self.code_saver_tool],
            allow_delegation=False,
            verbose=True,
        )

    def debugger_agent(self):
        logging.info("Creating Debugger Agent")
        return Agent(
            role='Debugger',
            goal='Find and fix bugs quickly',
            backstory=dedent(
                r"""\
                You're a detective in the world of code, tracking down bugs and eliminating them with precision.
                """
            ),
            llm=self.Ollama,
            tools=[self.repl_tool, self.csv_search_tool, self.code_saver_tool],
            allow_delegation=False,
            verbose=True,
        )

    def documentation_specialist_agent(self):
        logging.info("Creating Documentation Specialist Agent")
        return Agent(
            role='Documentation Specialist',
            goal='Ensure all code is well-documented for future reference',
            backstory=dedent(
                r"""\
                You’re a master communicator, translating complex technical information into clear documentation.
                """
            ),
            llm=self.Ollama,
            tools=[self.repl_tool, self.csv_search_tool, self.code_saver_tool],
            allow_delegation=False,
            verbose=True,
        )

    def knowledge_retriever_agent(self):
        logging.info("Creating Knowledge Retriever Agent")
        return Agent(
            role='Knowledge Retriever',
            goal='Retrieve relevant knowledge and resources for the crew',
            backstory=dedent(
                r"""\
                You're a digital librarian, always retrieving the right resource at the right time.
                """
            ),
            llm=self.Ollama,
            tools=[self.repl_tool, self.csv_search_tool, self.knowledge_retriever_tool, self.code_saver_tool],
            allow_delegation=False,
            verbose=True,
        )

    def database_engineer_agent(self):
        logging.info("Creating Database Engineer Agent")
        return Agent(
            role='Database Engineer',
            goal='Set up and manage the database for the chatbot project',
            backstory=dedent(
                r"""\
                You ensure that the data is stored securely and efficiently, and that the database is optimized for performance.
                """
            ),
            llm=self.Ollama,
            tools=[self.repl_tool],  # Assuming database connection tool is handled elsewhere
            allow_delegation=False,
            verbose=True,
        )

# Ensure the following libraries are installed
# pip install crewai langchain-community requests langchain-core langchain-experimental