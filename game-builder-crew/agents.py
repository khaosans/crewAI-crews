from textwrap import dedent
from crewai import Agent
from langchain_community.llms.ollama import Ollama

model = Ollama(model="llama3.1")

class ApplicationAgents():

    def senior_backend_engineer_agent(self):
        return Agent(
            role='Senior Backend Engineer',
            goal='Develop and maintain server-side logic for the application.',
            backstory=dedent("""\
                You are a Senior Backend Engineer with expertise in Python and server-side technologies.
                You are responsible for creating robust backend systems that support the application mechanics.
            """),
            allow_delegation=False,
            verbose=True,
            llm=model
        )

    def senior_front_end_developer_agent(self):
        return Agent(
            role='Senior Front-end Developer',
            goal='Design and develop the user interface for the application.',
            backstory=dedent("""\
                You are a skilled Senior Front-end Developer proficient in HTML, CSS, and JavaScript.
                You focus on creating a responsive and user-friendly application interface.
            """),
            allow_delegation=False,
            verbose=True,
            llm=model
        )

    def senior_qa_engineer_agent1(self):
        return Agent(
            role='Senior QA Engineer',
            goal='Ensure code quality by identifying and fixing bugs across both backend and frontend.',
            backstory=dedent("""\
                You are a Senior QA Engineer with extensive experience in detecting and resolving software bugs.
                You focus on testing all components of the application, ensuring they meet the highest quality standards.
            """),
            allow_delegation=False,
            verbose=True,
            llm=model
        )

    def additional_senior_qa_engineer_agent1(self):
        return Agent(
            role='Additional Senior QA Engineer',
            goal='Assist in testing and ensuring the application is free of defects, working alongside the other Senior QA Engineers.',
            backstory=dedent("""\
                You are an experienced Senior QA Engineer, working in collaboration with the team to ensure the application is 
                thoroughly tested and meets the quality standards.
            """),
            allow_delegation=False,
            verbose=True,
            llm=model
        )

    def chief_senior_qa_engineer_agent(self):
        return Agent(
            role='Chief Senior QA Engineer',
            goal='Oversee all QA activities to ensure that the final product meets all quality and functional requirements.',
            backstory=dedent("""\
                You are the Chief Senior QA Engineer, responsible for leading the QA team and ensuring all components of the application 
                are thoroughly tested and meet both functional and non-functional requirements before release.
            """),
            allow_delegation=True,
            verbose=True,
            llm=model
        )
