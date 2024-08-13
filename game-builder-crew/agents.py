import logging
from textwrap import dedent
from crewai import Agent
from langchain_community.llms.ollama import Ollama

# Configure logging
logging.basicConfig(level=logging.INFO, filename='agent_logs.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class GameAgents():
    def __init__(self):
        self.Ollama = Ollama(model="Llama3.1")

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

    def senoir_devops_engineer_agent(self):
        logging.info("Creating Senior DevOps Engineer Agent")
        return Agent(
            role='DevOps Engineer',
            goal='Deploy the application using Docker.',
            backstory=dedent("""\
					You are a DevOps Engineer specialized in containerizing applications
					and deploying them using Docker. You ensure that the application 
					runs smoothly in isolated environments and manage the CI/CD pipeline.
				"""),
            allow_delegation=False,
            verbose=True
        )

    def senoir_devops_engineer_agent2(self):
        logging.info("Creating Senior DevOps Engineer Agent")
        return Agent(
            role='DevOps Engineer',
            goal='Deploy the application using Docker.',
            backstory=dedent("""\
					You are a DevOps Engineer specialized in containerizing applications
					and deploying them using Docker. You ensure that the application 
					runs smoothly in isolated environments and manage the CI/CD pipeline.
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

    def dev_ops_qa_agent2(self):
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


    def product_manager_agent(self):
        logging.info("Creating Product Manager Agent")
        return Agent(
            role='Product Manager',
            goal='Oversee the development and deployment of the application, delegating tasks as needed.',
            backstory=dedent("""\
                    You are a Product Manager responsible for overseeing the entire development process
                    of the application. Your role involves ensuring that the project stays on track, 
                    meets the business requirements, and is delivered on time. You delegate tasks to 
                    the appropriate team members, manage the timeline, and ensure that quality standards 
                    are met across all stages of development and deployment.
                """),
            allow_delegation=True,
            verbose=True
        )


    def dev_ops_qa_engineer_agent(self, name="DevOps QA Engineer"):
        logging.info(f"Creating {name} Agent")
        return Agent(
            role=name,
            goal='Ensure the application is production-ready by analyzing the code for errors and verifying deployment configurations.',
            backstory=dedent("""\
                You are a DevOps QA Engineer specializing in checking code for errors and ensuring 
                the application is deployment-ready. You have an eye for detail and a knack for 
                finding hidden bugs. You are proficient in identifying issues not only in the code 
                but also in deployment scripts and configurations. You check for missing imports, 
                variable declarations, mismatched brackets, syntax errors, security vulnerabilities, 
                and logic errors. Additionally, you review Dockerfiles, CI/CD pipeline scripts, 
                and other deployment configurations to ensure smooth deployment in production environments.
            """),
            allow_delegation=False,
            verbose=True
        )

    def qa_engineer_agent2(self):
        logging.info("Creating Chief Software Quality Control Engineer Agent")
        return Agent(
            role='Chief Software Quality Control Engineer2',
            goal='Ensure that the code does the job it is supposed to do',
            backstory=dedent("""\
                    You believe that programmers often do only half the job, so you are
                    dedicated to ensuring high-quality code.
                """),
            allow_delegation=True,
            verbose=True
        )
