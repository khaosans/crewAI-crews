import logging
from textwrap import dedent
from crewai import Agent

# Configure logging
logging.basicConfig(level=logging.INFO, filename='agent_logs.log',
					format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class GameAgents():
	def senior_engineer_agent(self):
		logging.info("Creating Senior Software Engineer Agent")
		return Agent(
			role='Senior Software Engineer',
			goal='Create software as needed',
			backstory=dedent("""\
                You are a Senior Software Engineer at a leading tech think tank.
                Your expertise is in programming in Python. You strive to 
                produce perfect code.
            """),
			allow_delegation=False,
			verbose=True
		)

	def qa_engineer_agent(self):
		logging.info("Creating Software Quality Control Engineer Agent")
		return Agent(
			role='Software Quality Control Engineer',
			goal='Create perfect code by analyzing the code for errors',
			backstory=dedent("""\
                You are a software engineer specializing in checking code for errors.
                You have an eye for detail and a knack for finding hidden bugs.
                You check for missing imports, variable declarations, mismatched
                brackets, and syntax errors. You also check for security vulnerabilities
                and logic errors.
            """),
			allow_delegation=False,
			verbose=True
		)

	def chief_qa_engineer_agent(self):
		logging.info("Creating Chief Software Quality Control Engineer Agent")
		return Agent(
			role='Chief Software Quality Control Engineer',
			goal='Ensure that the code does the job it is supposed to do',
			backstory=dedent("""\
                You believe that programmers often do only half the job, so you are
                dedicated to ensuring high-quality code.
            """),
			allow_delegation=True,
			verbose=True
		)
