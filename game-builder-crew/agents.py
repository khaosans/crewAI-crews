import logging
from textwrap import dedent
from crewai import Agent
from langchain_community.llms.ollama import Ollama
import requests

from langchain_core.tools import Tool

from crewai import Agent
from crewai_tools import CodeInterpreterTool


from langchain_experimental.utilities import PythonREPL


from crewai_tools import FileWriterTool


# Initialize the tool
file_writer_tool = FileWriterTool()


# Define the code and libraries used
# Removed Streamlit import
# code = "import streamlit as st\nprint('Streamlit imported successfully')"
# libraries_used = ["streamlit"]

# Write content to a file in a specified directory
# Configure logging
logging.basicConfig(level=logging.INFO, filename='agent_logs.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

python_repl = PythonREPL()
# You can create the tool to pass to an agent

code_interpreter_tool = CodeInterpreterTool()
repl_tool = Tool(
    name="python_repl",
    description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
    func=python_repl.run,
)


class ChatbotAgents():
    def __init__(self):
        self.Ollama = Ollama(model="llama3.1")

    def chatbot_developer_agent(self):
        logging.info("Creating Chatbot Developer Agent")
        return Agent(
            role='Chatbot Developer',
            goal='Develop a chatbot that can interact with users.',  # Removed Streamlit reference
            backstory=dedent("""\
                You are a Chatbot Developer specializing in creating interactive chatbots.
                Your expertise is in natural language processing and user experience design.
                You strive to create chatbots that are engaging and helpful.
            """),
            llm=self.Ollama,
            allow_delegation=False,
            verbose=True
        )

    def qa_engineer_agent(self):
        logging.info("Creating Chatbot QA Engineer Agent")
        return Agent(
            role='Chatbot QA Engineer',
            goal='Ensure the chatbot functions correctly and provides accurate responses.',
            backstory=dedent("""\
                You are a QA Engineer specializing in testing chatbots.
                You have an eye for detail and a knack for finding hidden bugs.
                You check for response accuracy, user interaction flow, and overall performance.
                You are also a pro python developer.
            """),
            llm=self.Ollama,
            allow_delegation=False,
            verbose=True
        )

    def chief_qa_agent(self):
        logging.info("Creating Final QA Check Agent")
        return Agent(
            role='Final QA Check',
            goal='Perform the final quality assurance check before deployment.',
            backstory=dedent("""\
                You are responsible for the final quality assurance check of the chatbot.
                You are also a professional python developer.
            """),
            llm=self.Ollama,
            allow_delegation=True,
            verbose=True
        )
