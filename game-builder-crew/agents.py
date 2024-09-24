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

code_interpreter_tool = CodeInterpreterTool()

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
            tools=[CodeInterpreterTool()],  # Ensure tools are correctly passed
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
            """),
            llm=self.Ollama,
            tools=[CodeInterpreterTool()],
            allow_delegation=False,
            verbose=True
        )

    def product_manager_agent(self):
        logging.info("Creating Chatbot Product Manager Agent")
        return Agent(
            role='Chatbot Product Manager',
            goal='Oversee the development and deployment of the chatbot, delegating tasks as needed.',
            backstory=dedent("""\
                You are a Product Manager responsible for overseeing the entire development process
                of the chatbot. Your role involves ensuring that the project stays on track, 
                meets the business requirements, and is delivered on time. You delegate tasks to 
                the appropriate team members, manage the timeline, and ensure that quality standards 
                are met across all stages of development and deployment.
            """),
            llm=self.Ollama,
            tools=[CodeInterpreterTool(), file_writer_tool],
            allow_delegation=True,
            verbose=True
        )

    def data_engineer_agent(self):
        logging.info("Creating Chatbot Data Engineer Agent")
        return Agent(
            role='Chatbot Data Engineer',
            goal='Prepare and manage data for the chatbot interactions.',
            backstory=dedent("""\
                You are a Data Engineer specializing in preparing datasets for chatbots.
                You ensure that the data used for training and responses is accurate and relevant.
            """),
            llm=self.Ollama,
            tools=[CodeInterpreterTool()],
            allow_delegation=False,
            verbose=True
        )

    def deployment_engineer_agent(self):
        logging.info("Creating Chatbot Deployment Engineer Agent")
        return Agent(
            role='Chatbot Deployment Engineer',
            goal='Deploy the chatbot to production environments.',
            backstory=dedent("""\
                You are a Deployment Engineer responsible for deploying chatbots.
                You ensure that the chatbot is accessible to users and runs smoothly in production.
            """),
            llm=self.Ollama,
            tools=[CodeInterpreterTool()],
            allow_delegation=False,
            verbose=True
        )

    def integration_tester_agent(self):
        logging.info("Creating Integration Tester Agent")
        return Agent(
            role='Integration Tester',
            goal='Run the application and verify its functionality.',  # Removed Streamlit reference
            backstory=dedent("""\
                You are an Integration Tester specializing in running applications and verifying their functionality.
                You ensure that the application works as expected and provides a seamless user experience.
            """),
            llm=self.Ollama,
            tools=[CodeInterpreterTool()],
            allow_delegation=False,
            verbose=True
        )

    def database_engineer_agent(self):
        logging.info("Creating Database Engineer Agent")
        return Agent(
            role='Database Engineer',
            goal='Set up and manage the database for the chatbot project.',
            backstory=dedent("""\
                You are a Database Engineer specializing in setting up and managing databases.
                You ensure that the data is stored securely and efficiently, and that the database is optimized for performance.
            """),
            llm=self.Ollama,
            tools=[CodeInterpreterTool()],
            allow_delegation=False,
            verbose=True
        )

# Ensure the following libraries are installed
# pip install crewai langchain-community requests langchain-tools chromadb sqlite3 pandas
